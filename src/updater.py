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
from urllib.error import URLError

from updater.sourceparser import Parser

from settings.settings import DBNAME, SOURCE_DICT, SCHEMA_SQL

def crossref_building():
    """ Create crossrefs """

    dbh = sqlite3.connect(DBNAME)

    cf_regex = re.compile('\(cf\. ([^\)]+)\)')
    gismu_regex = re.compile(' (\w{5})')

    c = dbh.cursor()
    all_gismu = c.execute("SELECT rowid,gismu,comment FROM dico;").fetchall()

    # then create a dict of dict :
    gismu_list = {_[1].decode('utf8'):{'id':_[0], 'comment':_[2].decode('utf8')} for _ in all_gismu}

    for gismu,dic in gismu_list.items():
        print('Processing {}'.format(gismu))
        cfs = cf_regex.search(dic['comment'])
        if cfs:
            referenced = gismu_regex.findall(cfs.groups()[0])
            for r in referenced:
                if gismu_list.get(r):
                    c.execute('INSERT INTO crossref(src,ref) VALUES(?,?)', (dic['id'], gismu_list.get(r)['id']))

    dbh.commit()
    dbh.close()


def main():

    # first, clean Db and regenerate it
    db = sqlite3.connect(DBNAME)
    with open(SCHEMA_SQL) as f:
        db.executescript(f.read())

    c = db.cursor()

    # then grab the file
    try:
        distant_dict = urlopen(SOURCE_DICT)
    except URLError as err:
        sys.stderr.write("Well... urllopen just didn't work: {}".format(err))

    with tempfile.TemporaryFile() as f:
        print('Writing distant dic content to tempfile....')
        f.write(distant_dict.read())

        p = Parser(f)
        c.executemany(
            'INSERT INTO dico(gismu,rafsi,english,globalenglish,definition,unknown,comment) VALUES (?,?,?,?,?,?,?);', p)

    db.commit()
    db.close()

    crossref_building()


if __name__=='__main__': main()
