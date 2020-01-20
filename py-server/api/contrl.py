import json
import os ,sys
import logging

class controller(object):

    ALL_CONTROLLER = None
    CURRENT_DIR = None
    CODE_SEND = None
    LOG_FILE_NAME = os.path.dirname(os.path.realpath(__file__))+"/uno_serial_class.log"

    def __init__(self,send) : 
        try:
            self.CODE_SEND = str(send)
            self.CURRENT_DIR = os.path.dirname(os.path.realpath(__file__))

            with open(self.CURRENT_DIR + '/controller.json', 'r') as json_file:
                self.ALL_CONTROLLER = json.load(json_file)

            self.getresponse()
            pass

        except Exception as  e:
            self.log(str(e))
            pass
       
    
    ### log file genarate ###
    def log(self,message="Log is added with default message"):
        logging.basicConfig(filename= self.LOG_FILE_NAME, 
                    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', 
                    filemode='a'
                    )
        logger=logging.getLogger() 
        
        logger.setLevel(logging.DEBUG) 
        logger.info(message)
        pass



    def validate(self):
        isOk = True
        try:
            self.ALL_CONTROLLER[self.CODE_SEND]
        except Exception:
            isOk = False
            
        return isOk


    ### All the response of every code in controller.json file ###
    def getresponse(self, cod=""):
        try:
            if self.validate():
                cod = self.CODE_SEND
                print(self.OutputGood(message="Data is accepted"))
            
            else:
                print(self.OutputError(message="Not find data into "+self.CURRENT_DIR + '/controller.json'))
                self.log(message="Not find data into "+self.CURRENT_DIR + '/controller.json')

        except Exception as  e:
            print(self.OutputError(message=str(e)))
            self.log(str(e))
            pass
        

    ### occur any exception or error ###
    def OutputError(self,message="Something wrong occurred"):
        data = {
            "result": {
                "status": "error",
                "Message": message
            }
        }
        json_string = json.dumps(data)
        return json_string

    ### Not occur any exception or error ###
    def OutputGood(self,message=""):

        data = {
            "result": {
                "status": "success",
                "Message": message
            }
        }
        json_string = json.dumps(data)
        return json_string
        

if __name__ == "__main__":
    controller("s")
    pass