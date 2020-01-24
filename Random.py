#		python code
#		script_name:Random
#
#		author: Harshita
#		description:
#

from earsketch import *

init()
setTempo(120)

#****instruments****#
beat = ELECTRO_DRUM_MAIN_BEAT_007
paino = HIPHOP_DUSTYPIANOLEAD_003
brake = RD_EDM_DRUMROLL_BREAK_5

#****Music****#
fitMedia(beat, 1, 1, 7)

#piano and symbol clash
fitMedia(paino, 2, 1, 5)
fitMedia(brake, 2, 5, 6)

#*****effects******#
#volume
setEffect(1, VOLUME, GAIN, -10)
setEffect(2, VOLUME, GAIN, 6, 5, 6, 6)

finish()
