import os
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent
DOCUMENTS_DIR = os.path.expanduser('~\Documents\\')
INIT_DATA_FILE_VALUES = { 
                            "ActivitTraker" : {
                            "IsInit" : ["False", 0],
                            "User" : "",
                            "Theme" : "rime",
                            "AppearanceMode" : "System"
                            }
                        }

print(BASE_DIR)