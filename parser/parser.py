# coding: utf-8


class Parser(object):

    def __init__(self, mapping):
        self.file_path = mapping["file_path"]
        self.cloumns = mapping["cloumns"]
        self.start = mapping["start"]
        self.table = mapping["table"]
        self.seq = mapping["seq"]

    # def __init__(self, **mapping):
    #     for key in mapping:
    #         self.__dict__[key] = mapping[key]

    def parse_txt(self):
        values = []
        with open(self.file_path) as file:
            for line in file.readlines()[self.start:]:
                rows = tuple([line.strip().split(self.seq)[col] for col in self.cloumns])
                values.append(rows)
        return values

    def parse_excel(self):

        pass

    def get_values(self):

        pass





    def parse_excel(self, path):
        pass
