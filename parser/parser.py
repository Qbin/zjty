# coding: utf-8
import xlrd
from utils.get_file_type import filetype


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
        values = []

        import xlrd
        data = xlrd.open_workbook(self.file_path)
        table = data.sheet_by_index(0)
        for index in range(table.nrows - self.start):
            values.append(tuple([table.cell(index + self.start, col) for col in self.cloumns]))
        return values

    def get_values(self, map):

        if filetype(map["path"]) in ("xls", "xlsx"):
            return self.parse_excel(map)

        else:
            return self.parse_txt(map)

    def parse_excel(self, path):
        pass
