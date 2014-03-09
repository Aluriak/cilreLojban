# -*- coding: utf-8 -*-
#########################
#       UPDATER         #
#########################


#########################
# IMPORTS               #
#########################
import sys

import sqlite3
import re
import tempfile
from urllib.request import urlopen

from updater.sourceparser import Parser

from settings.settings import DBNAME, SOURCE_DICT, SCHEMA_SQL

if __name__ == '__main__':

    # first, clean Db and regenerate it
    db = sqlite3.connect(DBNAME)
    #db.execute("DROP TABLE dico IF EXISTS;") # don't like this syntaxe sqlite3.OperationalError: near "IF": syntax error
    #db.execute("DROP TABLE crossref IF EXISTS;") # idem
    with open(SCHEMA_SQL) as f:
        for command in f:
            db.execute(command)

    c = db.cursor()

    # then grab the file
    try:
        distant_dict = urllopen(SOURCE_DICT)
    except URLError as err:
        sys.stderr.write("Well... urllopen just didn't work: {}".format(err))

    with tempfile.TemporaryFile() as f:
        print('Writing distant dic content to tempfile....')
        f.write(distant_dict.read())

        p = Parser(f)
        c.executemany(
            'INSERT INTO dico(gismu,rafsi,english,globalenglish,definition,unknown,comment) values (?,?,?,?,?,?,?);', p)

    c.close()
    db.close()
