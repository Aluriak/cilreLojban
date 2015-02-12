# -*- coding: utf-8 -*-
#########################
#       ENG2LOJ         #
#########################


#########################
# IMPORTS               #
#########################
import sys
from gismu.gismuFinder import GismuFinder



#########################
# PRE-DECLARATIONS      #
#########################







#########################
# TREATMENT             #
#########################
if __name__ == '__main__':
    arg = sys.argv

    if len(arg) < 2:
        print("usage: <english word>")
    else:
        inter = "\n--------------------------------------------------------\n"
        print(inter.join((str(gismu) for gismu in GismuFinder(gismu_english=arg[1]))))



