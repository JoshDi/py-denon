#!/usr/bin/python
import serial
import sys
from optparse import OptionParser
try:
	denSerial = serial.Serial('/dev/tty.usbserial', 9600, timeout=1)
except serial.serialutil.SerialException:
	print 'Error cannot open Serial Connection.'
	sys.exit(0)

def sendCommand( serialConnection, passcommand ):
	print passcommand
	print serialConnection.write( passcommand )
	print serialConnection.readline()
	return

p = OptionParser()
p.add_option("-c", "--command", dest="command", help="Denon Command to use", metavar="COMMAND")
(options, args) = p.parse_args()

if len(options.command) > 0:
	sendCommand( denSerial, options.command + '\r' )
else:
	print "Menu of commands soon to come"

denSerial.close()
sys.exit(0)
