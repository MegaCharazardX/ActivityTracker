from customtkinter import *
from pathlib import Path
from CONSTANTS import *
import json
import datetime
import SessionIDGenerator 
# "2026-02-14 23:35:42.932780"
# print(type(datetime.datetime(2025,2,14,0,0,0,0) - datetime.datetime.now()))
# print(datetime.datetime.now())

class __App__ :
    
    def __init__(self):
        pass
    
    def AppFileExists(self):
        if Path(f"{DOCUMENTS_DIR}\\ActivityTracker.json").is_file(): # Change To Documents Directory : f"{DOCUMENTS_DIR}\\ActivityTracker.json"
            print(f"File exists")
            if self.IsSessionValid():
                self.UpdateLogin()
                return True
            else:
                self.UpdateSession()
                return False
            
        else:
            with open(f"{DOCUMENTS_DIR}\\ActivityTracker.json", "w") as file: # Change To Documents Directory : f"{DOCUMENTS_DIR}\\ActivityTracker.json"
                INIT_DATA_FILE_VALUES["ActivityTracker"]["LastLogIn"] = str(datetime.datetime.now())
                INIT_DATA_FILE_VALUES["ActivityTracker"]["SessionID"] = SessionIDGenerator.Gen_Code()
                
                json.dump(INIT_DATA_FILE_VALUES, file)
        
    def IsSessionValid(self):
        
        with open(f"{DOCUMENTS_DIR}\\ActivityTracker.json", "r") as file: # Change To Documents Directory : f"{DOCUMENTS_DIR}\\ActivityTracker.json"
            ActivityTrackerFile = json.load(file)
            SessionDate = ActivityTrackerFile["ActivityTracker"]["LastLogIn"]
                #print(int(SessionDate[0:4]), int(SessionDate[5:7]), int(SessionDate[8:10]), int(SessionDate[10:13]), int(SessionDate[14:16]), int(SessionDate[17:19]), int(SessionDate[20:-1]))
            timeDiff = (datetime.datetime(int(SessionDate[0:4]), int(SessionDate[5:7]), int(SessionDate[8:10]), int(SessionDate[10:13]), int(SessionDate[14:16]), int(SessionDate[17:19]), int(SessionDate[20:-1])) - datetime.datetime.now()).days
            if timeDiff < -7 :
                return False
            else:
                return True
                
    def UpdateSession(self):
        with open(f"{DOCUMENTS_DIR}\\ActivityTracker.json", "r+") as file: # Change To Documents Directory : f"{DOCUMENTS_DIR}\\ActivityTracker.json"
            ActivityTrackerFile = json.load(file)
            ActivityTrackerFile["ActivityTracker"]["SessionID"]= SessionIDGenerator.Gen_Code()
            print(ActivityTrackerFile)
            file.seek(0)
            json.dump(ActivityTrackerFile,file)
        
    def UpdateLogin(self):
        with open(f"{DOCUMENTS_DIR}\\ActivityTracker.json", "r+") as file: # Change To Documents Directory : f"{DOCUMENTS_DIR}\\ActivityTracker.json"
            ActivityTrackerFile = json.load(file)
            ActivityTrackerFile["ActivityTracker"]["LastLogIn"]=  str(datetime.datetime.now())
            print(ActivityTrackerFile)
            file.seek(0)
            json.dump(ActivityTrackerFile,file)
        
__App__().AppFileExists()

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
    
set_appearance_mode("System")  # Modes: "System" (standard), "Dark", "Light"
set_default_color_theme(r"CTkThemesPack-main\CTkThemesPack-main\themes\rime.json")  # Themes: "blue" (standard), "green", "dark-blue"


class App(CTk):
    def __init__(self):
        super().__init__()

        # configure window
        self.title("CustomTkinter complex_example.py")
        self.geometry(f"{1100}x{580}")

        # configure grid layout (4x4)
        self.grid_columnconfigure(1, weight=1)
        self.grid_columnconfigure((2, 3), weight=0)
        self.grid_rowconfigure((0, 1, 2), weight=1)

        # create sidebar frame with widgets
        self.sidebar_frame = CTkFrame(self, width=140, corner_radius=0)
        self.sidebar_frame.grid(row=0, column=0, rowspan=4, sticky="nsew")
        self.sidebar_frame.grid_rowconfigure(4, weight=1)
        self.logo_label = CTkLabel(self.sidebar_frame, text="CustomTkinter", font=CTkFont(size=20, weight="bold"))
        self.logo_label.grid(row=0, column=0, padx=20, pady=(20, 10))
        self.sidebar_button_1 = CTkButton(self.sidebar_frame) #, command=self.sidebar_button_event
        self.sidebar_button_1.grid(row=1, column=0, padx=20, pady=10)
        

if __name__ == "__main__":
    app = App()
    app.mainloop()
        
