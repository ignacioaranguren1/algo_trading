from .connector import Connector
from .strategy import Strategy
from statistics import median
from threading import Thread
from termcolor import colored

import logging


class Trader(Thread):
    """
        Trader class defines the Trader object. The Trader object inherits from thread class. Thus, concurrency is added
        to the system to make it possible for the main thread to interact with the strategies and generators
    """
    def __init__(self, strategies, generators):
        Thread.__init__(self)
        # class variables definition
        self.strategies = strategies
        self.generators = generators
        self.strat_dict = {}
        for strategy in range(self.strategies):
            self.strat_dict[f'STRGY_{strategy}'] = None
        # connector object builds an interface between the trader thread and every thread of each strategy
        self.cnnr = Connector(self.strat_dict.keys())
        self.logger = logging.getLogger('logger')

    def run(self):
        for strategy in range(self.strategies):
            # Launch every strategy thread
            new_strgy = Strategy(self.generators, f'STRGY_{strategy}', self.cnnr)
            new_strgy.start()
            # Save strategy
            self.strat_dict[f'STRGY_{strategy}'] = new_strgy
        self.logger.info(colored(f'{self.strategies} strategies have been initiated', 'green'))
        while True:
            # Wait to every strategy thread to post a decision
            if self.cnnr.check_posted():
                # If every thread has posted a decision get decisions
                self.logger.info(colored(f'Output decision: {self.get_decisions()}', 'green'))
                # update connectors
                self.update_cnnrs()

    def update_cnnrs(self):
        # Whenever every strategy has posted a decision, we need to override the connector with a new one with initial
        # values
        self.cnnr = Connector(self.strat_dict.keys())
        for strategy in self.strat_dict.keys():
            # update connector for every strategy
            self.strat_dict[strategy].set_connector(self.cnnr)

    def get_decisions(self):
        # Get the decisions of each strategy posted in the connector
        decisions = []
        for strategy in self.strat_dict.keys():
            decisions += [self.cnnr.gen_dict[strategy]]
        self.logger.info(colored(f'Decisions: {decisions} ', 'green'))
        return median(decisions)

    def kill_strategy(self, strgy):
        try:
            if f'STRGY_{strgy}' in self.strat_dict.keys():
                self.strat_dict.pop(f'STRGY_{strgy}', None)
                self.logger.info(colored(f'STRGY_{strgy} killed', 'green'))
                self.update_cnnrs()
            else:
                raise KeyError
        except KeyError as e:
            self.logger.info(colored(e, 'red'))

    def add_strategy(self, gen):
        new_strgy = Strategy(gen, f'STRGY_{self.strategies}', self.cnnr)
        new_strgy.start()
        self.strat_dict[f'STRGY_{self.strategies}'] = new_strgy
        self.logger.info(colored(f'New strategy STRGY_{self.strategies} created', 'green'))
        self.update_cnnrs()
        self.strategies += 1

    def add_generator(self, strgy):
        if f'STRGY_{strgy}' in self.strat_dict.keys():
            self.strat_dict[f'STRGY_{strgy}'].add_generator()
            self.logger.info(colored(f'New generator created for  STRGY_{strgy}', 'green'))

    def kill_generator(self, strgy, gen):
        try:
            if f'STRGY_{strgy}' in self.strat_dict.keys():
                self.strat_dict[f'STRGY_{strgy}'].kill_generator(gen)
            else:
                raise KeyError
        except KeyError as e:
            self.logger.info(colored(e, 'red'))

