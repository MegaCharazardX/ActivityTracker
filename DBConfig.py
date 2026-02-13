import os
from pathlib import Path
import sqlite3
import CONSTANTS


class DBOperation:
    def __init__(self, Database = f"{CONSTANTS.BASE_DIR}/ActivityTracker.db"):
        self.SelectQuery = "SELECT {} FROM {}"
        self.UpdateQuery = "UPDATE {} SET {}"
        self.InsertQuery = "INSERT INTO {} VALUES {}"
        self.con = sqlite3.connect(Database)
        self.cur = self.con.cursor()

    def initDB(self):
        
        self.cur.execute("""
                            CREATE TABLE "Gender" (
                            "GenderID"	INTEGER,
                            "Gender"	TEXT,
                            "GenderName"	TEXT,
                            PRIMARY KEY("GenderID" AUTOINCREMENT)
                            );
                        """)
        
        self.cur.execute("""
                            CREATE TABLE "Master" (
                            "MasterID"	INTEGER,
                            PRIMARY KEY("MasterID" AUTOINCREMENT)
                            );
                        """)
        
        self.cur.execute("""
                            CREATE TABLE "User" (
                            "UserID"	INTEGER UNIQUE,
                            "UserName"	TEXT NOT NULL UNIQUE,
                            "UserFirstName"	TEXT NOT NULL,
                            "UserLastName"	TEXT,
                            "UserDOB"	INTEGER NOT NULL,
                            "UserPassword"	TEXT NOT NULL,
                            "UserGmail"	TEXT NOT NULL,
                            "UserGender"	NUMERIC,
                            "UserIsActive"	NUMERIC DEFAULT 1,
                            "UserIsAdmin"	NUMERIC DEFAULT 0,
                            PRIMARY KEY("UserID" AUTOINCREMENT),
                            FOREIGN KEY("UserGender") REFERENCES "Gender"("GenderID")
                            );
                        """)
        
    # def ScanForMusic(self, Dir = r"E:/Dhejus/Songs"):
    #     for root, _ , files in os.walk(Dir):
    #         for file in files :
    #             print(file)
    #             if file.endswith((".mp3", ".wav", "m4a")):
    #                 file_path = os.path.join(root, file)
    #                 title = os.path.splitext(file)[0]
    #                 self.cur.execute("INSERT INTO Music (MName, MPath) VALUES(?, ?)", (title, file_path))
    #     self.con.commit()            
                
    def Select(self, Table, Condition = "", Feilds = "*"):
        if Condition :
            tempSelectQuery = self.SelectQuery + " WHERE {}"
            tempQry = tempSelectQuery.format(Feilds, Table, Condition)
            #print(tempQry)
            result = self.cur.execute(tempQry)
            return result
            for i in result:
                print(i)
        else:
            tempQry = self.SelectQuery.format(Feilds, Table)
            result = self.cur.execute(tempQry)
            return result
            for i in result:
                print(i)
    
    def Update(self, Table, assignment, Condition = ""):
        if Condition:
            tempUpdateQuery = self.UpdateQuery + " WHERE {}"
            tempQuery = tempUpdateQuery.format(Table,assignment, Condition)
            self.cur.execute(tempQuery)
        else: 
            tempQuery = self.SelectQuery.format(Table, assignment )
            self.cur.execute(tempQuery)
    
            
                
        


    