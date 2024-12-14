from pathlib import Path
import random
import asyncio
import time
from tqdm import tqdm
from string import Template
from loguru import logger
from pandas import read_csv

from hw4.utils.file_utils import read_yaml, read_jsonl, append_jsonl, write_yaml
from hw4.models.openai.async_inference import request_chatgpt

from hw4.async_exp.exp_utils.schema import ModelResponse
from hw4.async_exp.exp_utils.args_config import get_args

MODEL_PARAMS = read_yaml('config/config.yaml')

async def inference_single_datum(datum, user_prompt, exp_name, model, model_params):
    t0 = time.time()
    _, result, _, usage, _, _ = await request_chatgpt(
        model=model,
        system="",
        user=user_prompt,
        **model_params,
    )
    inference_time = time.time() - t0
    # Save result as model_response
    model_response = ModelResponse(
        model=model,
        inference_parameters=model_params,
        inference_time=inference_time,
        num_token=usage,
        raw_output = result,
    )
    datum["inferences"][exp_name] = model_response.model_dump()

    if DEBUG:
        logger.debug(f"\n{user_prompt}{result}\n")

    return datum


async def main(filename, model="o1-mini-2024-09-12"):
    # Set variables
    model_params = MODEL_PARAMS[model]
    # Experiment name
    experiment_name = "test"
    result_dir = Path(__file__).parent / "result" / experiment_name
    logger.debug(f"Running experiment: {experiment_name}") #NOTE: experiment_name

    # Prompt
    prompts = read_yaml(Path(__file__).parent / "config" /"prompts.yaml")
    user_template = prompts["machine_annotation_prompt"]

    # Save condition
    condition = {
        "filename": filename,
        "model_params": MODEL_PARAMS,
    }
    write_yaml(condition, result_dir / "condition.yaml")
    # Data
    data = read_csv(Path(__file__).parents[1] / "generated_writings" / filename)
    data = data.iloc[:, 1]
    # Make id
    data = [{"id": i, "text": text} for i, text in enumerate(data)]

    # Debug
    if DEBUG:
        data = random.sample(data, 1)
    completed_data = read_jsonl(result_dir / "result.jsonl")
    completed_ids = set([datum["id"] for datum in completed_data])
    current_tasks = set()
    inference_data = []
    # Run all data
    for datum in tqdm(data):
        if datum["id"] in completed_ids:
            continue
        # Generate user prompt
        user_prompt = Template(user_template).safe_substitute(
            model_input=datum["text"]
        )
        # Run single data
        task = asyncio.create_task(
            inference_single_datum(datum, user_prompt, experiment_name, model, model_params)
            )
        current_tasks.add(task)
        # Async worker queue
        if len(current_tasks) >= 10:
            done, current_tasks = await asyncio.wait(current_tasks, return_when=asyncio.FIRST_COMPLETED)
            for task in done:
                inference_datum = task.result()
                if not DEBUG:
                    append_jsonl(inference_datum, result_dir / "result.jsonl")
                inference_data.append(inference_datum)
    # Wait for remaining tasks    
    if len(current_tasks) > 0:
        logger.debug(f"Wait for remaining tasks : {len(current_tasks)}")
        done, current_tasks = await asyncio.wait(current_tasks, return_when=asyncio.ALL_COMPLETED)
        for task in done:
            inference_datum = task.result()
            if not DEBUG:
                append_jsonl(inference_datum, result_dir / "result.jsonl")
            inference_data.append(inference_datum)
    
    return inference_data

if __name__ == "__main__":
    # Get args
    args = get_args()
    # Debug
    global DEBUG
    DEBUG = args.debug

    asyncio.run(main(filename="clova_sample_science_results.csv"))