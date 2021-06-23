import sqlite3
from sqlite3 import Error

class DatabaseConnection():

    def __init__(self, db_file):
        self.conn = None

        try:
            self.conn=sqlite3.connect(db_file)
        except Error as e:
            print(e)

    def getallceos(self):
        cur = self.conn.cursor()
        cur.execute("SELECT * FROM ceos;")
        ceos = cur.fetchall()

        return ceos

    ##############################################
    #   bætum inn nýjum aðgerðum á grunninn hér  #
    ##############################################
