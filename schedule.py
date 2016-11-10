# coding: utf-8


from parser.parser import Parser
from conf import db_config, dt_mappings


class Scheduler(object):
    def __init__(self, config, mapping):
        self.db_config = config
        self.dt_mapping = mapping

    def schedule(self):
        self.insert()

    def insert(self):
        for mapping in self.dt_mapping:
            parser = Parser(mapping)
            module = __import__(self.db_config["type"])
            db = getattr(module, self.db_config["type"])
            db.create(parser.get_values())


if __name__ == "__main__":
    S = Scheduler(db_config, dt_mappings)
    S.schedule()
