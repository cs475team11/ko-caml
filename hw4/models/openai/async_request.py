import asyncio
import json
import os
from typing import Any, Dict, List, Optional, Union

from loguru import logger
import openai
from openai import AsyncOpenAI


def read_json(filepath: str) -> Dict[Any, Any]:
    with open(filepath, encoding="utf-8") as f:
        return json.load(f)


config = read_json(os.path.join(os.path.dirname(__file__), "openai_config.json"))
#openai.api_key = config["api_key"]
client = AsyncOpenAI(api_key = config["api_key"])

async def api_query(
    model: str,
    prompt: Union[str, List[Dict[str, str]]],
    temperature: float = 0.0,
    seed: int = 42,
    top_p: float = 1.0,
    max_completion_tokens: Optional[int] = None,
    presence_penalty: float = 0.0,
    frequency_penalty: float = 0.0,
    stop: Optional[str] = None,
    return_text: str = "",
    return_texts: str = "",
    finish_reason: str = "",
    return_usages: int = 0,
    return_prompt_usages: int = 0,
    return_completion_usages: int = 0,
    n: int = 1,
) -> Any:
    try:
        if model in [
            "gpt-4o-2024-11-20",
            "gpt-4o-mini-2024-07-18",
            "o1-mini-2024-09-12"
        ]:
            #response = await openai.ChatCompletion.acreate(
            response = await client.chat.completions.create(
                model=model,
                messages=prompt,
                # temperature=temperature,
                seed=seed,
                top_p=top_p,
                max_completion_tokens=max_completion_tokens,
                presence_penalty=presence_penalty,
                frequency_penalty=frequency_penalty,
                n=n,
            )
            # from functools import reduce
            # return_text = reduce(lambda x, y: x + y, [choice["message"]["content"] for choice in response["choices"]], '')
            response = response.model_dump_json(indent=2)
            response = json.loads(response)
            
            return_text = response["choices"][0]["message"]["content"]
            return_texts += return_text
            finish_reason = response["choices"][0]["finish_reason"]
            return_usages += response["usage"]["total_tokens"]
            return_prompt_usages += response["usage"]["prompt_tokens"]
            return_completion_usages += response["usage"]["completion_tokens"]
        else:
            raise ValueError("Not supported model.")

    except openai.error.InvalidRequestError as e:  # number of tokens > 4097
        logger.error(e)
        logger.error("Number of tokens > 4097")
        return (
            return_text,
            return_texts,
            finish_reason,
            return_usages,
            return_prompt_usages,
            return_completion_usages,
        )
    except (
        openai.error.ServiceUnavailableError,
        openai.error.RateLimitError,
        openai.error.APIError,
        openai.error.Timeout,
    ) as e:
        logger.warning(e)
        logger.warning("Try again in 30 seconds.")
        await asyncio.sleep(30)
        (
            return_text,
            return_texts,
            finish_reason,
            return_usages,
            return_prompt_usages,
            return_completion_usages,
        ) = await api_query(
            model,
            prompt,
            temperature=temperature,
            top_p=top_p,
            max_completion_tokens=max_completion_tokens,
            presence_penalty=presence_penalty,
            frequency_penalty=frequency_penalty,
            stop=stop,
            return_text=return_text,
            return_texts=return_texts,
            finish_reason=finish_reason,
            return_usages=return_usages,
            return_prompt_usages=return_prompt_usages,
            return_completion_usages=return_completion_usages,
            n=n,
        )

    if finish_reason == "stop":
        return (
            return_text,
            return_texts,
            finish_reason,
            return_usages,
            return_prompt_usages,
            return_completion_usages,
        )
    elif model in [
        "text-davinci-003",
        "text-curie-001",
        "text-babbage-001",
        "text-ada-001",
    ]:
        return (
            return_text,
            return_texts,
            finish_reason,
            return_usages,
            return_prompt_usages,
            return_completion_usages,
        )
    else:
        logger.warning(f"finish_reason is not stop. finish_reason: {finish_reason}")
        prompt.append({"role": "user", "content": return_text})
        return await api_query(
            model,
            prompt,
            temperature=temperature,
            top_p=top_p,
            max_completion_tokens=max_completion_tokens,
            presence_penalty=presence_penalty,
            frequency_penalty=frequency_penalty,
            stop=stop,
            return_text=return_text,
            return_texts=return_texts,
            finish_reason=finish_reason,
            return_usages=return_usages,
            return_prompt_usages=return_prompt_usages,
            return_completion_usages=return_completion_usages,
            n=n,
        )
