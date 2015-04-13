__author__ = 'yuczhou'


class Enum(dict):
    def __getattr__(self, name):
        if name in self:
            return self[name]
        raise AttributeError


settings = Enum({"RANDOM_RANGE": (0.9, 1.1),
                 "TEST_MODE": True})