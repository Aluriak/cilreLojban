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
arg = sys.argv

if len(arg) < 2:
    print("usage: <english word>")
else:
    for gismu in GismuFinder(gismu_english=arg[1]):
        print(gismu)
        print("\n\n")
    # if no gismu: 
    else: 
        print("END")



