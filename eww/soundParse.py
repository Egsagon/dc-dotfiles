# ====================================== #
# Hands the ouptut of pa_volume to eww   #
# (https://github.com/rhaas80/pa_volume) #
# ====================================== #

# Note:
# Is meant to check wether each application is currently running
# but it's too hard for me maybe i'll come back on this #TODO

import os
import json

EXCLUDE = ['RiotClientUx.exe',
           'LeagueClientUX.exe',
           'python3.10',
           'FMOD',
           'FMOD Ex App',
           'ShooterGame',
           'SDL']

windows = [' '.join(win.split()[3:]) for win in os.popen('wmctrl -l').readlines()]
res = os.popen('pa_volume').read().replace('client: ', '').split('\n')[:-1]

apps = []

for app in res:
   els = app.split()
   
   name = ' '.join(els[:-1])
   
   rep = (name + ' ' * 20)[:17]
   
   if name in EXCLUDE: continue
   
   vol = int(els[-1].replace('%', ''))
   
   for win in windows:
      if name.lower() in win.lower():
         apps.append({'name': name, 'vol': vol, 'rep': rep})

print(json.dumps(apps))