# -*- coding: utf-8 -*-
#########################
#       LOJ2ENG         #
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
    print("usage: <lojban word>")
else:
    gismu = Gismu(arg[1])
    if gismu.found:
        print(gismu)
    else:
        print("No gismu founded !")



