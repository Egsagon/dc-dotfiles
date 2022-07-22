# =============================================== #
# When resize mod is on, will toggle the keyboard #
# to slot 2 (see eruptionctl). if you don't have  #
# Eruption, you may use the resizer popup in      #
# eww/popups.yuck.                                #
# =============================================== #

import os

mode = os.popen('i3-msg -t get_binding_state').read()
os.system(f"eruptionctl switch slot {int('resize' in mode) + 1}")