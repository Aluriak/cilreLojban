# -*- coding: utf-8 -*-
#########################
#       ENG2LOJ         #
#########################


#########################
# IMPORTS               #
#########################
import sys
from gismu.gismu import Gismu 



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
    gismu = Gismu(english=argv[1])
    if gismu.founded:
        print(gismu)
    else:
        print("No gismu founded !")



