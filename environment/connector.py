class Connector(object):
    """
    A connector object is used to link all the strategy threads and the trader thread. The main reason of using
    this object is to prevent the size of strat_dict in the trader thread to change in the middle of an iteration
    process. If the dictionary changes an exception will be raised indicating that the dictionary has changed in
    middle of an iteration.
    """

    def __init__(self, strgs):
        self.strategies = strgs
        self.gen_dict = {}
        for strgy in self.strategies:
            self.gen_dict[strgy] = None

    def post_decision(self, strgy, decision):
        self.gen_dict[strgy] = decision

    def check_posted(self) -> bool:
        return None not in self.gen_dict.values() and bool(self.gen_dict)


