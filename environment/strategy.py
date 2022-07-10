from threading import Thread
from .generator import Generator
from termcolor import colored

import time
import logging

UPDATE_FREQUENCY = 60

class Strategy(Thread):
    def __init__(self, generators, strgy_id, cnnr):
        Thread.__init__(self)
        self.generators = generators
        self.strgy_id = strgy_id
        self.connector = cnnr
        self.gen_dict = {}
        self.logger = logging.getLogger('logger')
        self.decision = None

    def run(self):
        """
        Run method from parent overridden.
        :return:
        """
        # Initialize generators
        for generator_id in range(self.generators):
            self.gen_dict[f'GEN_{generator_id}'] = Generator(generator_id)
        # Loop every UPDATE_FREQUENCY seconds
        while True:
            decision = self.get_latest_decision()
            self.connector.post_decision(self.strgy_id, decision)
            time.sleep(UPDATE_FREQUENCY - time.time() % UPDATE_FREQUENCY)

    def get_latest_decision(self) -> int:
        """
        Get the latest decision of each generator.
        :return:
        """
        decision = 0
        for generator in self.gen_dict.keys():
            decision += self.gen_dict[generator].gen_random()
        return decision

    def set_connector(self, cnnr):
        self.connector = cnnr

    def add_generator(self):
        """
        Add generator to strategy.
        :return:
        """
        self.gen_dict[f'GEN_{self.generators}'] = Generator(self.generators)
        self.logger.info(colored(f'GEN_{self.generators} added', 'green'))
        self.generators += 1

    def kill_generator(self, gen):
        """
        Kill generator of current strategy.
        :param gen:
        :return:
        """
        if f'GEN_{gen}' in self.gen_dict.keys():
            self.gen_dict.pop(f'GEN_{gen}', None)
            self.logger.info(colored(f'GEN_{gen} killed', 'green'))
        else:
            self.logger.info(colored(f'Failed to kill generator. Unknown GENERATOR {gen}', 'red'))


