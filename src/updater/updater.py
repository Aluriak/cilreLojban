# -*- coding: utf-8 -*-
#########################
#       UPDATER         #
#########################


#########################
# IMPORTS               #
#########################
import sys

import sqlite3
import tempfile
from urllib2 import urlopen

from sourceparser import Parser

from settings import DBNAME, SOURCE_DICT

if __name__ == '__main__':

    # first, clean Db and regenerate it
    db = slqite3.connect_db(DBNAME)
    db.execute("DROP TABLE dico     IF EXISTS;")
    db.execute("DROP TABLE crossref IF EXISTS;")
    with open('schema.sql') as f:
        db.execute(f.read())

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
