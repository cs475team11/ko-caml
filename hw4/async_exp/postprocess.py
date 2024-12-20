import json
import pandas as pd
from pathlib import Path

def load_jsonl(file_path):
    with open(file_path, 'r', encoding='utf-8') as f:
        return [json.loads(line) for line in f]

def main(text_type, input_dir_name):
    input_path = Path(__file__).parent / "result" / text_type / input_dir_name / "result.jsonl"
    data = load_jsonl(input_path)

    # sort by id
    data.sort(key=lambda x: x['id'])
    
    # count instances for every text
    rows = []
    for datum in data:
        text = datum['text']
        num_token = datum['inferences']['num_token']
        count = datum['inferences']['raw_output'].count('[')
        rows.append({'text': text, 'num_token': num_token, 'count': count})
    output = pd.DataFrame(rows)

    print("Output DataFrame:", output)
    output.to_csv(Path(__file__).parent / "result" / text_type / input_dir_name / "result.csv", index=False)

    total_token_K = output['num_token'].sum() / 1000
    total_count = output['count'].sum()
    avg_occur = total_count / total_token_K
    print(f"avg_token_K: {total_token_K/len(data)}")
    print(f"avg_count: {total_count/len(data)}")
    print(f"avg_occur: {avg_occur}")

if __name__ == "__main__":
    main(text_type="novel", input_dir_name="qwen/qwen_neutral_novel")