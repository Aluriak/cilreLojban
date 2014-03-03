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
from settings.settings import DB_NAME, SOURCE_DICT

def crossref_building(dbh):
    """ Create crossrefs """

    cf_regex = re.compile('\(cf\. ([^\)]+)\)')
    gismu_regex = re.compile(' (\w{5})')

    c = dbh.cursor()
    all_gismu = c.execute("SELECT rowid,gismu,comment FROM dico;").fetchall()

    # then create a dict of dict :
    gismu_list = {_[1]:{'id':_[0], 'comment':_[2]} for _ in all_gismu}

    for gismu,dic in gismu_list:
        print('Processing {}'.format(gismu))
        referenced = gismu_regex.findall(cf_regex.search(dic['comment']).groups()[0])

        map(
            lambda g: c.execute('INSERT INTO crossref(src,ref) VALUES(?,?)', (dic['id'], gismu_list.get(g)['id'])),
            referenced
        )


def main():

    # first, clean Db and regenerate it
    db = sqlite3.connect(DB_NAME)
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
            'INSERT INTO dico(gismu,rafsi,english,globalenglish,definition,unknown,comment) VALUES (?,?,?,?,?,?,?);', p)

    c.close()

    crossref_building(db)

    db.close()

if __name__=='__main__': main()
