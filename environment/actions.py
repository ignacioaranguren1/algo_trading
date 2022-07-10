from enum import Enum


class Actions(Enum):
    """
    Action class defines the available actions for the environment to interact with the trader
    """
    KILL_STRGY = 0
    ADD_STRGY = 1
    KILL_GEN = 2
    ADD_GEN = 3
