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

def get_multiclass_args():
    parser = argparse.ArgumentParser()
    parser.add_argument("--model", type=str, default="gpt-3.5-turbo-16k-0613", choices=["gpt-3.5-turbo-16k-0613", "gpt-4-0613", "gpt-4-1106-preview", 'clova'])
    parser.add_argument("--random_seed", type=int, default=42)
    parser.add_argument("--debug", type=lambda x : str2bool(x), default=False)
    args = parser.parse_args()

    return args
