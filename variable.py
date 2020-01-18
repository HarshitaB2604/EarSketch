# python code
#
# script_name: Variables
#
# author: The EarSketch Team
#
# description: Using variables to store clips and simplify edits
#
#
#

#Setup
from earsketch import *
init()
setTempo(200)

#Music
# Try assigning different clips to "synth1" and "synth2" for a new sound.
#synth1 = HIPHOP_SYNTHPLUCKLEAD_005 # Assigns a clip to the variable "synth1"
synth1 = CIARA_MELANIN_THEME_TUBA_1
synth2 = RD_CINEMATIC_SCORE_STRINGS_4
drums = CIARA_SET_DRUMBEAT_1

# fitMedia adds the clip "synth1" is holding to the DAW
fitMedia(synth1, 1, 1, 2)

# synth1 and synth2 are used many times
fitMedia(synth2, 1, 2, 9)
fitMedia(synth1, 2, 2, 8)

fitMedia(drums, 3, 1, 9)

setEffect(1, VOLUME, GAIN, -30, 1.5, 0, 7.5)
setEffect(2, VOLUME, GAIN, 0, 3, -10, 5)
setEffect(2, VOLUME, GAIN, -10, 5, 0, 7)
setEffect(3, VOLUME, GAIN, -20)

#Finish
finish()
