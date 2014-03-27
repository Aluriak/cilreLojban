#! /usr/bin/env python
# -*- coding:utf8 -*-
#
# gismuFinder.py
#
# Copyright © 2014 Mathieu Gaborit (matael) <mathieu@matael.org>
#
#
# Distributed under WTFPL terms
#
#            DO WHAT THE FUCK YOU WANT TO PUBLIC LICENSE
#                    Version 2, December 2004
#
# Copyright (C) 2004 Sam Hocevar <sam@hocevar.net>
#
# Everyone is permitted to copy and distribute verbatim or modified
# copies of this license document, and changing it is allowed as long
# as the name is changed.
#
#            DO WHAT THE FUCK YOU WANT TO PUBLIC LICENSE
#   TERMS AND CONDITIONS FOR COPYING, DISTRIBUTION AND MODIFICATION
#
#  0. You just DO WHAT THE FUCK YOU WANT TO.
#

from settings.settings import DBNAME
import sqlite3
from gismu.gismu import Gismu


#########################
# CLASS GISMU FINDER    #
#########################
class GismuFinder(object):
    """
Definition of a finder of Gismu.
Search in dbutils.settings for name of database 
    """

# CONSTRUCTOR #################################################################
    def __init__(self, gismu_name=None, gismu_english=None):
        self.gismu_name = gismu_name
        self.gismu_english = gismu_english
        self.gismu_list = []
        self._db_lookup()


# PROTECTED METHODS ###########################################################
    def _db_lookup(self):
        """ Look up through database to find the right definition and references """
        # INIT
        db = sqlite3.connect(DBNAME)
        req_result = db.cursor()

        # TREATMENT
        if self.gismu_name is not None:
            req_result.execute("SELECT * FROM dico WHERE gismu LIKE ?", 
                      ("%"+self.gismu_name+"%",))
        elif self.gismu_english is not None:
            req_result.execute("SELECT * FROM dico WHERE english LIKE ?", 
                      (self.gismu_english,))
        else:
            print("ERROR: gismu name or english word must be given")


        # for each result
        for gismu in req_result:
            # decode into utf8
            gismu = [v.decode('utf-8') for v in gismu]
            # creat and add new gismu
            self.gismu_list.append(Gismu(
                gismu[0], gismu[1], gismu[2], # name, rafsi, english
                gismu[3], gismu[4], # globenglish, definition
                gismu[5], gismu[6]  # unknow, comment
            ))

        # END
        req_result.close()
        db.close()


# BUILTIN   ###################################################################
    def __iter__(self):
        return self.gismu_list.__iter__()








if __name__ == '__main__':
    s = 'besna'
    g = Gismu(s)
    if not g.founded:
        print(s+" not found in DB")
        exit(1)

    print(g)



    e = 'run'
    g = Gismu(english=e)
    if not g.founded:
        print(s+" not found in DB")
        exit(1)

    print(g)



