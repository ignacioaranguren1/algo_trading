class Connector(object):
    def __init__(self, strgs):
        self.strategies = strgs
        self.gen_dict = {}
        for strgy in self.strategies:
            self.gen_dict[strgy] = None

    def post_decision(self, strgy, decision):
        self.gen_dict[strgy] = decision

    def check_posted(self) -> bool:
        return None not in self.gen_dict.values()


