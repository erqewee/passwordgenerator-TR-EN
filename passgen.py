# IMPORT MODULES
from random import *
from string import *
from datetime import datetime
# IMPORT MODULES

# IMPORT METHODS
from methods.ClearLogs import ClearLogs
from methods.createNewPassword import createNewPassword
from methods.overwriteCreatedPassword import overwriteCreatedPassword
from methods.readCreatedPasswords import readCreatedPasswords
# IMPORT METHODS

allChars = (ascii_letters + ascii_lowercase + ascii_uppercase + punctuation + digits)

fileName = "lastCreatedPassword-log.js"
file = open(fileName, "w", encoding="utf-8")

fileName2 = "allCreatedPassword-logs.txt"
file2 = open(fileName2, "a", encoding="utf-8")

userName = input("Adınızı Giriniz: ")

today = datetime.today()
time = """{ "Year": "%(year)s", "Month": "%(month)s", "Day": "%(day)s", "Hour": "%(hour)s:%(minute)s:%(second)s" }""" % { "year": today.year, "month": today.month, "day": today.day, "hour": today.hour, "minute": today.minute, "second": today.second }

if(userName == ""):
 userName += "Belirtilmedi!"

security = ""

Array = [];
Array.append([0, 1, 2, 3, 9])
Array.remove("[")
Array.remove("]")


while True:
  val = int(input("""
+ İşlem Türünü seçiniz!

|---------------------|
| 1 - Oluşturana ekle |
|---------------------|
| 2 - Düz oluştur     |
|---------------------|
| 3 - Şifreleri Oku   |
|---------------------|
| 0 - Temizle         |
|---------------------|
| 9 - Programı Kapat  |
|---------------------|

> İşleminiz: """))
 
  if(val == 1):
   desc = input("Bu şifreyi ne için kullanacaksınız: ")
   length = int(input("Uzunluğu giriniz: "))

   if(length <= 8):
    security += "Not Safe!"

   elif(length > 8):
    security += "Safe!"

   overwriteCreatedPassword(sample, length, desc, security, userName, file, file2, fileName, fileName2, time, allChars);

  elif(val == 2):
   desc = input("Bu şifreyi ne için kullanacaksınız: ")
   length = int(input("Uzunluğu giriniz: "))

   if(length <= 8):
    security += "Not Safe!"
  
   elif(length > 8):
    security += "Safe!"
   
   createNewPassword(sample, length, desc, security, userName, file, file2, fileName, fileName2, time, allChars);

  if(val == 3):
   readCreatedPasswords(fileName2, fileName);

  elif(val == 0): 
   ClearLogs(fileName2, fileName);
 
  elif(val == 9):
   print("[Uygulama] Program başarıyla durduruldu!")
   break