import argparse

def str2bool(v):
    if isinstance(v, bool):
        return v
    if v.lower() in ('yes', 'true', 't', 'y', '1'):
        return True
    elif v.lower() in ('no', 'false', 'f', 'n', '0'):
        return False
    else:
        raise argparse.ArgumentTypeError('Boolean value expected.')

def get_args():
    parser = argparse.ArgumentParser()
    parser.add_argument("--debug", type=lambda x : str2bool(x), default=False)
    parser.add_argument("--text_type", type=str, default="novel")
    parser.add_argument("--input_model", type=str, default="qwen")
    parser.add_argument("--filename", type=str, default="_neutral_novel.csv")
    args = parser.parse_args()

    return args


# python3 async_exp/run_inference.py --input_model qwen --filename _korean_novel.csv