import serial

class commander(object):
    """
        This class will handle all interfaces with the denon serial port.

    """
    def __init__(self):
        # @todo: move these settings to a configuration file
        self.serialPort = '/dev/null'
        self.baudRate = 9600
        self.timeout = 1
        self.__conn = None

    def connect(self):
        self.__conn = serial.Serial(self.serialPort, self.baudRate, timeout=self.timeout)
        return self.__conn

    def sendCommand(self, command, cr=r'\r', options={}):
        """ 
            handles passing commands to the serial port.
            @param command: rs232 command to send
            @param options: dictionary of optional parameters
            @return: boolean
        """
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
        return self.__conn.readline()