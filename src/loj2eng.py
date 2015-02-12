# -*- coding: utf-8 -*-
#########################
#       LOJ2ENG         #
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
        print("usage: <lojban word>")
    else:
        inter = "\n--------------------------------------------------------\n"
        print(inter.join((str(gismu) for gismu in GismuFinder(gismu_name=arg[1]))))

