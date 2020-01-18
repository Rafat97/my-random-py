import os
import socket
import re
import uuid
import logging
from datetime import datetime
# C:/ProgramData/Anaconda3/python.exe c:/Users/rafat/OneDrive/Desktop/server/server.py

def serverModule(net_type='', port=0, buffer=1024):
    blu = MyServer(net_type, port, buffer)
    blu.creatServer()

class MyServer:

    PC_NAME = "null"
    HOST = "localhost"
    PORT = 2564
    MAC = ':'.join(re.findall('..', '%012x' % uuid.getnode()))
    SOCKET = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    ETHERNET_HOST = ""
    BUFFER_SIZE = 1024
    LOGGER = None

    def __init__(self, net_type='', port=0, buffer=1024):
        self.BUFFER_SIZE = buffer
        self.PC_NAME = socket.gethostname()
        self.HOST = socket.gethostbyname(self.PC_NAME)
        addresses = os.popen(
            'IPCONFIG | FINDSTR /R "Ethernet adapter Local Area Connection .* Address .*[0-9][0-9]*\.[0-9][0-9]*\.[0-9][0-9]*\.[0-9][0-9]*"')
        first_eth_address = re.search(
            r'\b\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}\b', addresses.read()).group()

        self.ETHERNET_HOST = first_eth_address

        if net_type == "e":
            self.HOST = self.ETHERNET_HOST

        self.SOCKET.bind((self.HOST, 0))
        self.PORT = self.SOCKET.getsockname()[1]

        if port != 0:
            self.PORT = port
            
        now = datetime.now()

        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as soc:
            soc.bind((self.HOST, self.PORT))
        pass

        fileName = "_SERVER_LOG_"+str(now.strftime("%d-%m-%Y__%H-%M-%S")) + ".log"

        logging.basicConfig(filename= fileName, 
                    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', 
                    filemode='w')
        #Creating an object 
        logger=logging.getLogger() 
        
        #Setting the threshold of logger to DEBUG 
        logger.setLevel(logging.DEBUG) 
        self.LOGGER = logger

        

    def creatServer(self):
        print("PC Name : ", self.PC_NAME)
        print("host : ", self.HOST)
        print("port : ", self.PORT)
        print("buffer size : ", self.BUFFER_SIZE)
        self.LOGGER.info(self.PC_NAME)
        self.LOGGER.info(self.HOST)
        self.LOGGER.info(self.PORT)
        self.LOGGER.info(self.BUFFER_SIZE)

        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as soc:

            soc.bind((self.HOST, self.PORT))
            while True:
                soc.listen()
                conn, addr = soc.accept()
                with conn:
                    print(addr)
                    self.LOGGER.info("*** Start Connection ***")
                    self.LOGGER.info(addr)
                    while True:
                        data = conn.recv(self.BUFFER_SIZE)
                        if not data:
                            self.LOGGER.info("*** Close Connection ***")
                            self.LOGGER.info(addr)

                            break

                        self.LOGGER.info(str(data.decode("utf-8")))
                        conn.sendall("*** done data ***".encode('utf-8'))

        pass


if __name__ == "__main__":
    blu = MyServer('e', 28280)
    blu.creatServer()
