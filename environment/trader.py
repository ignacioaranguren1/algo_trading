from .actions import Actions
from .connector import Connector
from .strategy import Strategy
from statistics import median
from threading import Thread
from enum import Enum
from termcolor import colored

import logging


class States(Enum):
    """
    The definition of states helps to prevent inconsistencies when updating strategies. If an action is executing,
    strategies might be updated and a inconsistent state may arise if a thread is working with an outdated version.
    """
    BUSY = 0
    IDLE = 1


class Trader(Thread):
    """
    Trader class defines the Trader object. The Trader object inherits from thread class. Thus, concurrency is added
    to the system to make it possible for the main thread to interact with the strategies and generators
    """

    CURRENT = States.IDLE

    def __init__(self, strategies, generators):
        Thread.__init__(self)
        # class variables definition
        self.strategies = strategies
        self.generators = generators
        self.strat_dict = {}
        for strategy in range(self.strategies):
            self.strat_dict[f'STRGY_{strategy}'] = None
        self.logger = logging.getLogger('logger')
        # Instantiate connector object
        self.cnnr = Connector(self.strat_dict.keys())

    def run(self):
        """
        Run method from parent overridden.
        :return: None
        """
        for strategy in range(self.strategies):
            # Init strategy
            new_strgy = Strategy(self.generators, f'STRGY_{strategy}', self.cnnr)
            # Launch strategy thread
            new_strgy.start()
            # Save strategy
            self.strat_dict[f'STRGY_{strategy}'] = new_strgy
        self.logger.info(colored(f'{self.strategies} strategies have been initiated', 'green'))
        while True:
            # If thread is busy executing some action continue to next iteration
            if self.CURRENT is States.IDLE:
                # Wait to every strategy thread to propose a decision
                if self.cnnr.check_posted():
                    # If every thread has proposed a decision, get decisions
                    self.logger.info(colored(f'Output decision: {self.get_decisions()}', 'green'))
                    self.update_cnnrs()

    def update_cnnrs(self):
        """
        Whenever every strategy has posted a decision, we need to override the connector with a new one with all initial
        decisions set to None. A None value means that a strategy has not posted any value yet. Updating the decisions in
        this way makes that check_posted() always finds a consistent set of strategies even when an add/kill action has
        modified the number of strategies in strat_dict
        :return:
        """
        self.cnnr = Connector(self.strat_dict.keys())
        for strategy in self.strat_dict.keys():
            # update connector for every strategy
            self.strat_dict[strategy].set_connector(self.cnnr)

    def get_decisions(self):
        """
        Once a update of decision has been made in every strategy, we need to collect the new values
        :return: None
        """
        # Get the decisions of each strategy posted in the connector
        decisions = []
        for strategy in self.cnnr.gen_dict.keys():
            decisions += [self.cnnr.gen_dict[strategy]]
        self.logger.info(colored(f'Decisions: {decisions} ', 'green'))
        return median(decisions)

    def interaction_manager(self, action, strgy=None, gen=None):
        """
        The interaction manager oversees the interactions of the environment with the strategies.
        :param action:
        :param strgy:
        :param gen:
        :return: None
        """
        # Lock state
        self.CURRENT = States.BUSY
        if action is Actions.ADD_STRGY:
            self._add_strategy(gen)
        elif action is Actions.KILL_STRGY:
            self._kill_strategy(strgy)
        elif action is Actions.ADD_GEN:
            self._add_generator(strgy)
        elif action is Actions.KILL_GEN:
            self._kill_generator(strgy, gen)
        # Release state
        self.CURRENT = States.IDLE

    def _kill_strategy(self, strgy):
        try:
            if f'STRGY_{strgy}' in self.strat_dict.keys():
                self.strat_dict.pop(f'STRGY_{strgy}', None)
                self.logger.info(colored(f'STRGY_{strgy} killed', 'green'))
                self.update_cnnrs()
            else:
                raise KeyError
        except KeyError as e:
            self.logger.info(colored(e, 'red'))

    def _add_strategy(self, gen):
        new_strgy = Strategy(gen, f'STRGY_{self.strategies}', self.cnnr)
        new_strgy.start()
        self.strat_dict[f'STRGY_{self.strategies}'] = new_strgy
        self.logger.info(colored(f'New strategy STRGY_{self.strategies} created', 'green'))
        self.update_cnnrs()
        self.strategies += 1

    def _add_generator(self, strgy):
        if f'STRGY_{strgy}' in self.strat_dict.keys():
            self.strat_dict[f'STRGY_{strgy}'].add_generator()
            self.logger.info(colored(f'New generator created for  STRGY_{strgy}', 'green'))

    def _kill_generator(self, strgy, gen):
        try:
            if f'STRGY_{strgy}' in self.strat_dict.keys():
                self.strat_dict[f'STRGY_{strgy}'].kill_generator(gen)
            else:
                raise KeyError
        except KeyError as e:
            self.logger.info(colored(e, 'red'))
