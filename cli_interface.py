from environment.environment import Environment
import argparse


def check_int_positive(value):
    ivalue = int(value)
    if ivalue <= 0:
        raise argparse.ArgumentTypeError(f"{value} is an invalid positive int value")
    return ivalue


parser = argparse.ArgumentParser()
parser.add_argument("strategies", help="select the number of strategies",
                    type=check_int_positive)
parser.add_argument("generators", help="select the number of generators",
                    type=check_int_positive)
parser.add_argument("--verbose", help="enable output verbosity",
                    action="store_true")
args = parser.parse_args()

if args.verbose:
    env = Environment(args.strategies, args.generators, verbose=True)
else:
    env = Environment(args.strategies, args.generators, verbose=False)


