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
arg = sys.argv

if len(arg) < 2:
    print("usage: <lojban word>")
else:
    for gismu in GismuFinder(gismu_name=arg[1]):
        print(gismu)
        print("\n\n")
    # if no gismu: 
    else: 
        print("END")



