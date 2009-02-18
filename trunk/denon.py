#!/usr/bin/env python
import serial
import sys
from optparse import OptionParser

if __name__ == '__main__':
    p = OptionParser()
    p.add_option("-c", "--command", dest="command", help="Denon Command to use", metavar="COMMAND")
    p.add_option("-p", "--port", dest="port", help="Serial Port dev to use", metavar="PORT")
    (options, args) = p.parse_args()

    if options.port:
        dev = options.port
    else: 
        dev = "/dev/tty.usbserial"

    try:
        denSerial = serial.Serial('/dev/tty.usbserial', 9600, timeout=1)
    except serial.serialutil.SerialException:
        print 'Error cannot open Serial Connection.'
        sys.exit(0)

    if options.command:
        sendCommand( denSerial, options.command + '\r' )
    else:	
        print "Menu of commands soon to come"
        sys.exit(0)

    denSerial.close()
    sys.exit(0)


def sendCommand( serialConnection, passcommand ):
	serialConnection.write( passcommand )
	print serialConnection.readline()
	return