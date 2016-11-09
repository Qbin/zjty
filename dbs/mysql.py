# coding: utf-8
import MySQLdb


class Mysql(object):
    def __init__(self, **kwargs):
        try:
            self.conn = MySQLdb.connect(kwargs)
            self.cur = self.conn.cursor()
        except MySQLdb.Error as e:
            print "WARNING: Mysql error %s" % str(e)

    def insert(self, table, *args, **kwargs):
            values = None
            query = "INSERT INTO %s " % table
            if kwargs:
                keys = kwargs.keys()
                values = tuple(kwargs.values())
                query += "(" + ",".join(["`%s`"] * len(keys)) % tuple(keys) + ") VALUES (" + ",".join(
                    ["%s"] * len(values)) + ")"
            elif args:
                values = args
                query += " VALUES(" + ",".join(["%s"] * len(values)) + ")"

    def update(self):
        pass






