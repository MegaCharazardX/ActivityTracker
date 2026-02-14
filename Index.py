from customtkinter import *
from pathlib import Path
from CONSTANTS import *
import json


class __App__ :
    def AppExists():
        if Path(f"{DOCUMENTS_DIR}\\ActivityTraker.json").is_file(): 
            print(f"File exists")
        else:
            with open(f"{DOCUMENTS_DIR}\\ActivityTraker.json", "w") as file:
                json.dump(INIT_DATA_FILE_VALUES, file)
                
__App__.AppExists()
class User:
    
    def __init__(self, _User = "", IsAdmin = False, IsSignedIn = False):
        self.__User = _User
        self.IsAdmin = IsAdmin
        self.IsSignedIn = IsSignedIn
        
    def isAdmin(self):
        if self.IsAdmin == True :
            return True
        else:
            return False
        
    def isSignedIn(self):
        if self.IsAdmin == True :
            return True
        else:
            return False
    
    def User(self):    
        if self.__User != "":
            return self.__User
        else:
            return None
        