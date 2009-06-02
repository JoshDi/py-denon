import os as _os
import logging as _logging
import datetime as _datetime

# server settings
serverAddress = "0.0.0.0"

# serial settings
serialPort = 'COM1'
baudRate = 9600
timeout = 1

# log settings
logLevel = _logging.DEBUG
logDirectory = "c:\\"
logFilename = "%s\\denon-%s-%d.txt" % (logDirectory, _datetime.datetime.now().strftime("%Y%m%d%H%M%S"), _os.getpid())
logEmail = True
logEmailLevel = _logging.CRITICAL
logEmailHost = "localhost"
logEmailFrom = "email@host.com"
logEmailTo = "email@host.com"

print 'here we go...'