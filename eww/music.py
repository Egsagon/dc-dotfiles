# ========================================================= #
# Small script that fetch the current played track and the  #
# author, and cuts if it is bigger than MAX.                #
# ========================================================= #

from os import popen
from json import dumps

# Settings #
MAX = 12
SHOW = False
# -------- #

meta = popen('playerctl metadata').readlines()

title = meta[1].split(':title')[1].strip()
auth = meta[3].split(':artist')[1].strip()

if len(title) > MAX: title = title[:MAX - 3] + '..'
if len(auth) > MAX: auth = auth[:MAX - 3] + '..'

if SHOW: print(dumps({'title': title, 'author': auth}))
else: print(dumps({'title': 'None', 'author': 'None'}))