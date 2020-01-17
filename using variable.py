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
drums = RD_WORLD_PERCUSSION_BASSWOODENTONE_1

# fitMedia adds the clip "synth1" is holding to the DAW
fitMedia(synth1, 1, 1, 2)

# synth1 and synth2 are used many times
fitMedia(synth2, 1, 2, 5)
fitMedia(synth1, 2, 3, 8)
fitMedia(synth2, 1, 4, 5)
#fitMedia(synth1, 1, 5, 6)
#fitMedia(synth2, 1, 6, 7)
#fitMedia(synth1, 1, 7, 8)
fitMedia(synth2, 1, 8, 9)

fitMedia(drums, 3, 1, 9)

#Finish
finish()
