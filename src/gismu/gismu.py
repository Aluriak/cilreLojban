#! /usr/bin/env python
# -*- coding:utf8 -*-
#
# gismu.py
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

class Gismu(object):
    """
Definition of a Gismu, with rafsi, translation in english, definition, 
references to another gismu,...
Search in dbutils.settings for name of database 
    """

# CONSTRUCTOR #################################################################
    def __init__(self, gismu=None, english=None):
        self.gismu = gismu
        self.english = english


# PROTECTED METHODS ###########################################################
    def _db_lookup(self):
        """ Look up through database to find the right definition and references """
        # INIT
        db = sqlite3.connect(DBNAME)
        c = db.cursor()

        # TREATMENT
        if self.gismu is not None:
            gismul = c.execute("SELECT * FROM dico WHERE gismu=?", self.gismu)
        elif self.english is not None:
            gismul = c.execute("SELECT * FROM dico WHERE english=?", self.english)
        print("DEBUG: " + str(gismul))
        if len(requestResult) > 0: 
            # take the first one
            gismu = requestResult[0]
            # assign values as self's attributes 
            self.gismu, self.rafsi, self.english = gismu[0], gismu[1], gismu[2]
            self.synenglish, self.definition = gismu[3], gismu[4]
            self.unknow, self.comment = gismu[5], gismu[6]
        else:
            # set attributes to None
            self.gismu, self.rafsi, self.english = None, None, None
            self.synenglish, self.definition = None, None
            self.unknow, self.comment = None, None

        # END
        c.close()
        db.close()



# PREDICATS ###################################################################
    @property
    def founded(self):
        """True if gismu was found when search in DB"""
        return self.gismu is not None



# CONVERSION ##################################################################
    def __str__(self):
        return (self.gismu 
              + "\nrafsi: " + self.rafsi
              + "\nenglish: " + self.english
              + "\ndefinition" + self.definition
              + "\nunknow: " + self.unknow
              + "\ncomment: " + self.comment
            )





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



