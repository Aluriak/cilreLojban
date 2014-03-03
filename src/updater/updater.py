# -*- coding: utf-8 -*-
#########################
#       UPDATER         #
#########################


#########################
# IMPORTS               #
#########################
import sqlite3
import parse



#########################
# PRE-DECLARATIONS      #
#########################
SOURCE_DICT = "http://www.lojban.org/publications/wordlists/gismu.txt"
DB_NAME = "data/db"
LOCAL_DICT_NAME = "data/dict"




#########################
# FUNCTIONS             #
#########################
def creatDB(dbDescriptor):
        """Destroy existing DB, and creat nex ones, empty and ready to use.
        Wait for a DB descriptor opened with sqlite3.connect() function"""
        db.execute("DROP TABLE dico     IF EXISTS;")
        db.execute("DROP TABLE crossref IF EXISTS;")
        #TODO: creat DB
        return None


def getDataFile(source=SOURCE_DICT, filename=LOCAL_DICT_NAME):
        """Search data file on the web, at SOURCE_DICT by default, and save it in LOCAL_DICT_NAME"""
        #TODO
        return None


def dataRow2dict(line):
        """
        Return a string as "gismu varchar(8), rafsi varchar(32), english varchar(32), etc"
        values can be used in a INSERT SQL query, and readed in line. 
        line must be format as this example : 
 gismu [rafsi] english [english2] definition number1 number2 precision; reference
        """
        parser = parse.compile("{}\t{}\t{}\t{}\t{}\t{}\t{}\t{};\t{}")
        print(parser.parse(line))
        return "TODO"


def getRefFor(line):
        """
        Return gismu referenced in given line ("cf..." tag)
        """
        #TODO
        return "TODO"




if __name__ == '__main__':
        # INIT
        #getDataFile()
        #db = sqlite3.connect(DB_NAME)
        #creatDB(db)

        ## TREATMENT
        #cursor = db.cursor()
        #try:
                #f = open(LOCAL_DICT_NAME, "r")
                #for line in f.readlines():
                        #sqline = dataRow2dict(line)
                        #c.execute("INSERT INTO dico VALUES(" + sqline + ");")

                        
        #except:
                #print("FILE ERROR: " + LOCAL_DICT_NAME)

        
        ## END
        #cursor.close()
        #db.close()




