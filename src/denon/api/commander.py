import serial

class commander(object):
    """
        This class will handle all interfaces with the denon serial port.

    """
    def __init__(self):
        pass #for now

    def sendCommand(self, command, options={}):
        """ 
            handles passing commands to the serial port.
            @param command: rs232 command to send
            @param options: dictionary of otional parameters
            @return: boolean
        """
        pass

    def readBuffer(self, amount=None):
        """
            handles reading the rs232 buffer
            @param amount - how many chars to read from the buffer, default: None (all chars)
        """
        pass

