import serial

class commander(object):
    """
        This class will handle all interfaces with the denon serial port.

    """
    def __init__(self):
        # @todo: move these settings to a configuration file
        self.serialPort = '/dev/tty.usbserial'
        self.baudRate = 9600
        self.timeout = 1
        self.__conn = None

    def connect(self):
        if not self.__conn or not self.__conn._isOpen:
            try:
                self.__conn = serial.Serial(self.serialPort, self.baudRate, timeout=self.timeout)
            except:
                return None            
            return self.__conn
        if self.__conn._isOpen:
            return self.__conn
        else:
            return None
        
    def disconnect(self):
        if self.__conn and self.__conn._isOpen:
            self.__conn.close()
        return True

    def sendCommand(self, command, cr='\r', options={}):
        """ 
            handles passing commands to the serial port.
            @param command: rs232 command to send
            @param options: dictionary of optional parameters
            @return: boolean
        """
        self.__conn.flushInput()
        if not self.__conn:
            return False
        self.__conn.write(str(command))
        self.__conn.write(cr)
        return True

    def readBuffer(self, amount=0):
        """
            handles reading the rs232 buffer
            @param amount - how many chars to read from the buffer, default: 0 (all chars)
        """
        if not self.__conn:
            return False
        if amount:
            return self.__conn.read(amount)
        else:
            return self.__conn.readline()

    def getConn():
        return self.__conn
