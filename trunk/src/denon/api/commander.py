import serial

class commander(object):
    """
        This class will handle all interfaces with the denon serial port.

    """
    def __init__(self):
        # @todo: move these settings to a configuration file.
        self.serialPort = '/dev/tty.usbserial'
        self.baudRate = 9600
        self.timeout = 1
        self.__conn = None

    def connect(self):
        """
            Establishes a connection to the serial port using self.serialPort, self.baudRate, self.timeout.
            @return: serial connection object.

        """
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
        """
            Disconnects the serial port connection.
        """
        if self.__conn and self.__conn._isOpen:
            self.__conn.close()
        return True

    def sendCommand(self, commands, cr='\r', options={}):
        """ 
            handles passing commands to the serial port.
            @param commands: list of rs232 commands to send.
            @param options: dictionary of optional parameters.
            @return: boolean
        """
        self.__conn.flushInput()
        if not self.__conn:
            return False
        for c in commands:
            self.__conn.write(str(c))
            self.__conn.write(cr)
        return True

    def readBuffer(self, amount=0):
        """
            Handles reading the rs232 buffer.
            @param amount - how many chars to read from the buffer, default: 0 (all chars).
        """
        if not self.__conn:
            return False
        if amount:
            return self.__conn.read(amount)
        else:
            return self.__conn.readline()

    def getConn():
        """
            get method to access __conn.
            @return: serial connection object.
        """
        return self.__conn
