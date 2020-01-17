# python code
#
# script_name: Intro Script
#
# author: Harshita
#
# description: This code adds one audio clip to the DAW
#
#
#

#Setup Section
from earsketch import *
init()
setTempo(150)

#Music Section
fitMedia(RD_UK_HOUSE__ACIDLINE_1, 1, 1, 9)

fitMedia(Y23_BELL_1, 2, 2, 5)

fitMedia(YG_NEW_FUNK_CLAV_1, 3, 1, 3)
fitMedia(YG_NEW_FUNK_CLAV_1, 3, 5, 7)

#Finish Section
finish()
