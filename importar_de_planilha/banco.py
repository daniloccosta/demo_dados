import psycopg2
from psycopg2.extensions import make_dsn

class Banco(object):
    _db = None
    def __init__(self):
        dsn = make_dsn("dbname='logisticawms' user='postgres' password='pg275248m' host='localhost' port=5432")
        self._db = psycopg2.connect(dsn)

    def execSql(self, sql):
        try:
            print(sql)
            cur = self._db.cursor()
            cur.execute(sql)
            cur.close()
            self._db.commit()
        except Exception as e:
            print("Error:", e)
            return False
        return True

    def consultar(self, sql):
        rs = None
        try:
            cur = self._db.cursor()
            cur.execute(sql)
            rs = cur.fetchall()
        except Exception as e:
            print("Error:", e)
            return None
        return rs

    def fechar(self):
        self._db.close()