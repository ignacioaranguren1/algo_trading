from .trader import Trader
from .config import LOGGING_CONFIG, LOGGING_CONFIG_UNSET
from termcolor import colored

import logging.config


class Environment(object):
    """
        Environment class. Defines the environment in which trader, strategies and generators run.
        After being instantiated, a trader thread is launch. Concurrency makes it possible to asynchronously interact
        with the trader.
    """

    def __init__(self, strategies, generators, verbose):
        self.num_strategies = strategies
        self.num_generators = generators
        self.verbose = verbose
        self.trader = None
        if verbose:
            # If verbose option defined in CLI, used logging interface.
            logging.config.dictConfig(LOGGING_CONFIG)
        else:
            logging.config.dictConfig(LOGGING_CONFIG_UNSET)
        self.logger = logging.getLogger('logger')
        self.init_trader()
        self.init_interface()

    def init_trader(self):
        self.trader = Trader(self.num_strategies, self.num_generators)
        self.trader.start()
        while None in self.trader.strat_dict.values():
            # Main thread needs to wait for strat_dict to be able to obtain the information to be displayed in the interface
            # below
            pass
        # stract_dict initialized in trader thread. Launch main interface
        self.init_interface()

    def init_interface(self):
        self.logger.info(colored('main interface initiated', 'green'))
        while True:
            self.print_output()
            try:
                print(colored('Type action:', 'blue'))
                option = input()
                if option == 'q' or option == 'Q':
                    continue
                elif int(option) not in [1, 2, 3, 4]:
                    print('Option not available')
                elif int(option) == 1:
                    print(f"Select the strategy to be killed: {list(self.trader.strat_dict.keys())}")
                    strgy = int(input())
                    if 'STRGY_' + str(strgy) in self.trader.strat_dict.keys():
                        self.trader.kill_strategy(strgy)
                    else:
                        print('Incorrect strategy')
                elif int(option) == 2:
                    print('Select number of generators: ')
                    num_gen = int(input())
                    self.trader.add_strategy(num_gen)
                elif int(option) == 3:
                    print(f"Select strategy: {list(self.trader.strat_dict.keys())}")
                    strgy = int(input())
                    if 'STRGY_' + str(strgy) in self.trader.strat_dict.keys():
                        print(f"Select generator: {list(self.trader.strat_dict['STRGY_' + str(strgy)].gen_dict.keys())}")
                        gen = int(input())
                        if 'GEN_' + str(gen) in self.trader.strat_dict['STRGY_' + str(strgy)].gen_dict.keys():
                            self.trader.kill_generator(strgy, gen)
                        else:
                            print('Generator not found in strategy.')
                    else:
                        print('Incorrect strategy')
                else:
                    print(f"Select the strategy to be modfied: {list(self.trader.strat_dict.keys())}")
                    strgy = int(input())
                    if 'STRGY_' + str(strgy) in self.trader.strat_dict.keys():
                        self.trader.add_generator(strgy)
                    else:
                        print('Incorrect strategy')
            except ValueError as e:
                self.logger.info(colored(e, 'red'))

    def print_output(self):
        # Formaters definition and header
        format_string = "{:<25}{:<15}"
        format_header = colored("{:<25}{:<15}", 'blue')
        header = ['STRATEGY ID', 'NUMBER OF GENERATORS']

        # Output layout definition
        print(f"\n----------------------------------------------------------------")
        print(f'Number of strategies: {self.num_strategies}')
        print(f'Default number of generators: {self.num_generators}')
        print("----------------------------------------------------------------\n")
        print(colored('#######################', 'blue'))
        print(f"{colored('#', 'blue')} DEPLOYED STRATEGIES {colored('#', 'blue')} ")
        print(colored('#######################\n', 'blue'))
        print(format_header.format(*header))
        # Print info about every strategy deployed
        for strgy in self.trader.strat_dict.keys():
            out = [strgy, len(self.trader.strat_dict[strgy].gen_dict)]
            print(format_string.format(*out))
        print(
            f"\n {colored('Available actions: ', 'blue')}\n\n"
            f"    - {colored('(1)', 'blue')} Kill current strategy\n"
            f"    - {colored('(2)', 'blue')} Add new strategy \n"
            f"    - {colored('(3)', 'blue')} Kill a strategy's generator\n"
            f"    - {colored('(4)', 'blue')} Add new generator to current strategy.\n"
            f"    - {colored('(q)', 'blue')} Print output\n")





