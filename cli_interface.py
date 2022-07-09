import argparse
from environment.environment import Environment

parser = argparse.ArgumentParser()
parser.add_argument("strategies", help="select the number of strategies",
                    type=int)
parser.add_argument("generators", help="select the number of generators",
                    type=int)
parser.add_argument("--verbose", help="increase output verbosity",
                    action="store_true")
args = parser.parse_args()

if args.verbose:
    env = Environment(args.strategies, args.generators, verbose=True)
else:
    env = Environment(args.strategies, args.generators, verbose=False)

