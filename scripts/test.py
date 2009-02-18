import sys
sys.path.insert(0, '/Users/chenry/Desktop/denon/src')

from denon.api.commander import commander
command = 'PWON'

d = commander()
d.connect()
d.sendCommand(command)
print d.readBuffer()
