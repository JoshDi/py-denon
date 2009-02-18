import sys
sys.path.insert(0, 'path here')

from denon.api.commander import commander

d = commander()
d.connect()
d.sendCommand(command)