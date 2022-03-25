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
onlyLetters = ascii_letters

# File One
fileName = "lastCreatedPassword-log.js"
file = open(fileName, "w", encoding = "UTF-8")

# File Two
fileName2 = "allCreatedPassword-logs.txt"
file2 = open(fileName2, "a", encoding = "UTF-8")

# Get user, User Name
userName = input("Adınızı giriniz: ")

# get Date
today = datetime.today()
month = ""

if(today.month == 1):
  month += "0%(i)s" % { "i": today.month }

elif(today.month == 2):
  month += "0%(i)s" % { "i": today.month }
  
elif(today.month == 3):
  month += "0%(i)s" % { "i": today.month }
  
elif(today.month == 4):
  month += "0%(i)s" % { "i": today.month }

elif(today.month == 5):
  month += "0%(i)s" % { "i": today.month }

elif(today.month == 6):
  month += "0%(i)s" % { "i": today.month }

elif(today.month == 7):
  month += "0%(i)s" % { "i": today.month }

elif(today.month == 8):
  month += "0%(i)s" % { "i": today.month }

elif(today.month == 9):
  month += "0%(i)s" % { "i": today.month }

else:
  print(today.month)
  
time = """{ "": "%(day)s.%(month)s.%(year)s | %(hour)s:%(minute)s:%(second)s" }""" % { "year": today.year, "month": month, "day": today.day, "hour": today.hour, "minute": today.minute, "second": today.second }

if(userName == ""):
 userName += "Girilmedi!"

else:
 userName = userName;

security = ""


try:
  val = int(input("""
+ Yapılacak işlemi giriniz.

|-------------------------|
| 1 - Oluşturulana Ekle   |
|-------------------------|
| 2 - Yeni Şifre Oluştur  |
|-------------------------|
| 3 - Şifreleri Oku       |
|-------------------------|
| 0 - Şifre Geçmişini Sil |
|-------------------------|
| 9 - Uygulamayı Durdur   |
|-------------------------|

> İşlem: """))
 
  if(val == 1):
   desc = input("Bu şifreyi ne için kullanacaksınız: ")
   length = int(input("Şifre uzunluğunu giriniz: "))

   if(length <= 8):
    security += "Güvenli Değil!"

   elif(length > 8):
    security += "Güvenli!"

   OverwriteCreated(sample, length, desc, security, userName, file, file2, fileName, fileName2, time, allChars, Error, Application);

  elif(val == 2):
   desc = input("Bu şifreyi ne için kullanacaksınız: ")
   length = int(input("Şifre uzunluğunu giriniz: "))

   if(length <= 8):
    security += "Güvenli Değil!"

   elif(length > 8):
    security += "Güvenli!"
   
   CreateNew(sample, length, desc, security, userName, file, file2, fileName, fileName2, time, allChars, Error, Application);

  if(val == 3):
   ReadAll(Application, fileName2, fileName);

  elif(val == 0): 
   ClearCache(Application, fileName, fileName2);
  
  elif(val == 9):
   Stop(Application);

except Exception as message:
  Error(message)