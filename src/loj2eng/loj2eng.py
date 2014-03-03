# -*- coding: utf-8 -*-
#########################
#       LOJ             #
#########################


#########################
# IMPORTS               #
#########################
import sys
from gismu import Gismu 



#########################
# PRE-DECLARATIONS      #
#########################







#########################
# TREATMENT             #
#########################
arg = sys.argv
print(arg)


gismu = Gismu(argv[1])
if gismu.founded:
    print(gismu)
else:
    print("No gismu founded !")



