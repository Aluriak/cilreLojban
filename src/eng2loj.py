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
    gismu = Gismu(english=arg[1])
    if gismu.found:
        print(gismu)
    else:
        print("No gismu founded !")



