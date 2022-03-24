# IMPORT MODULES
from random import *;
from string import *;
from datetime import datetime
# IMPORT MODULES

# IMPORT METHODS
from methods.ClearCache import *; # Clear logs
from methods.CreateNewPassword import *; # create a new password
from methods.OverwriteCreatedPassword import *; # write to created password
from methods.ReadCreatedPasswords import *; # read passwords
from methods.Error import *; # send private custom Error message
from methods.Application import *; # Application messages
from methods.Exit import *; # Stop program 
# IMPORT METHODS


# GENERATOR CODES
allChars = (ascii_letters + ascii_lowercase + ascii_uppercase + punctuation + digits)

# File One
fileName = "lastCreatedPassword-log.js"
file = open(fileName, "w", encoding="utf-8")

# File Two
fileName2 = "allCreatedPassword-logs.txt"
file2 = open(fileName2, "a", encoding="utf-8")

# Get user, User Name
userName = input("Enter username: ")

# get Date
today = datetime.today()
time = """{ "Year": "%(year)s", "Month": "%(month)s", "Day": "%(day)s", "Hour": "%(hour)s:%(minute)s:%(second)s" }""" % { "year": today.year, "month": today.month, "day": today.day, "hour": today.hour, "minute": today.minute, "second": today.second }

if(userName == ""):
 userName += "None!"

else:
 userName = userName;

security = ""


try:
  val = int(input("""
+ Please type case number!

|---------------------|
| 1 - Add to Created  |
|---------------------|
| 2 - Create New Pass |
|---------------------|
| 3 - Read Passwords  |
|---------------------|
| 0 - Clear Passwords |
|---------------------|
| 9 - Stop App        |
|---------------------|

> Case: """))
 
  if(val == 1):
   desc = input("What will you use this password for: ")
   length = int(input("Enter password length: "))

   if(length <= 8):
    security += "Not Safe!"

   elif(length > 8):
    security += "Safe!"

   OverwriteCreated(sample, length, desc, security, userName, file, file2, fileName, fileName2, time, allChars, Error, Application);

  elif(val == 2):
   desc = input("What will you use this password for: ")
   length = int(input("Enter password length: "))

   if(length <= 8):
    security += "Not Safe!"
  
   elif(length > 8):
    security += "Safe!"
   
   CreateNew(sample, length, desc, security, userName, file, file2, fileName, fileName2, time, allChars, Error, Application);

  if(val == 3):
   ReadAll(fileName2, fileName);

  elif(val == 0): 
   ClearCache(fileName2, fileName);
 
  elif(val == 9):
   Stop(Application);

except Exception as message:
  Error(message)