import serial
import logging
import sys,glob,os




class unoSerial(object):

    SERIAL_PORT = None
    LOG_FILE_NAME = os.path.dirname(os.path.realpath(__file__))+"/uno_serial_class.log"

    def __init__(self,serial_port="") : 
        try:
         
            if serial_port == "":
                self.SERIAL_PORT = self.get_serial_ports()[0]
            else:
                self.SERIAL_PORT = serial_port

            print(self.SERIAL_PORT)
            pass
        except Exception :
            print(sys.exc_info())
            self.log(sys.exc_info())
            pass
       
       
    
    def log(self,log="Log is added with default message"):
        logging.basicConfig(filename= self.LOG_FILE_NAME, 
                    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', 
                    filemode='a'
                    )
        logger=logging.getLogger() 
        
        logger.setLevel(logging.DEBUG) 
        logger.info(log)
        pass

    ### static method for get the serial port list ### 
    @staticmethod
    def get_serial_ports():

        if sys.platform.startswith('win'):
            ports = ['COM%s' % (i + 1) for i in range(256)]
        elif sys.platform.startswith('linux') or sys.platform.startswith('cygwin'):
            # this excludes your current terminal "/dev/tty"
            ports = glob.glob('/dev/tty[A-Za-z]*')
        elif sys.platform.startswith('darwin'):
            ports = glob.glob('/dev/tty.*')
        else:
            raise EnvironmentError('Unsupported platform')

        result = []
        for port in ports:
            try:
                s = serial.Serial(port)
                s.close()
                result.append(port)
            except (OSError, serial.SerialException):
                pass
        return result

        

if __name__ == "__main__":
    unoSerial("COM4")
    pass