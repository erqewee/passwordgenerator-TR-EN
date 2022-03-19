from random import *
from string import *
from datetime import *

All = (ascii_letters + ascii_lowercase + ascii_uppercase + punctuation + digits)
fileName = "lastCreatedPassword-log.js"
file = open(fileName, "w", encoding = "utf-8")

fileName2 = "allCreatedPassword-logs.txt"
file2 = open(fileName2, "a", encoding = "utf-8")

userName = input("Adınızı Giriniz: ")
desc = input("Bu şifreyi ne için kullanacaksınız: ")

if(userName == ""):
 userName += "Belirtilmedi!"
 
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

> İşleminiz: """))

def ClearLogs():
 with open(fileName, "w") and open(fileName2, "w") as i:
  print("'%(fileOne)s' ve '%(fileTwo)s' Temizlendi!" % { "fileOne": fileName, "fileTwo": fileName2})


def readCreatedPasswords(nameOne, nameTwo):
  with open(nameOne) and open(nameTwo) as datas:
   print(datas.read())


# İçerikleri oku
if(val == 3):
 readCreatedPasswords(fileName2, fileName);

elif(val == 0): 
 ClearLogs();


else:

 keyLength = int(input("Uzunluk Sayısını Giriniz: "))

 if(keyLength >= 100):
  print("[Uygulama Hatası] Max 100 uzunlukta şifre oluşturabilirsiniz.")

 today = datetime.today()
 time = """{ "Year": "%(year)s", "Month": "%(month)s", "Day": "%(day)s", "Hour": "%(hour)s:%(minute)s:%(second)s" }""" % { "year": today.year, "month": today.month, "day": today.day, "hour": today.hour, "minute": today.minute, "second": today.second } 

 security = ""

 if(keyLength == 0):
  print("0 yazılamaz")
 
 if(keyLength < 8):
  security += "Guvenli Degil!"

 elif(keyLength >= 8):
  security += "Guvenli!"


# FONKSİYON / 1
 def addToCreated(dataLength):
  i = input("Eklenmesini istediğiniz şifreyi girin: ")
  print("Şifre oluşturuluyor, biraz bekleyin.")

  create = sample(All, dataLength)

  passw = "".join(create)
  data = [];
  data.clear()
  data.append(passw + i)

  file.write("""const i = {
 
"Password": "%(gen)s",
"Name": '%(nm)s',
"Açıklama": '%(d)s',
"Durum": '%(sts)s', 
"Tarih": %(trh)s

};

module.exports = i; """ % { "d": desc, "sts": security, "nm": userName, "trh": time, "gen": passw + i})

  file2.write(
 """
|-----------------------|
| Password: '%(gen)s'
| Name: '%(nm)s'
| Description: '%(d)s'
| Durum: '%(sts)s'
| Tarih: %(trh)s
|-----------------------|
 """ % { "d": desc, "sts": security, "nm": userName, "trh": time, "gen": passw + i})
  print("Şifreniz: %(gen)s \n\n[Uygulama] Şifreniz '%(name)s' ve '%(name2)s' dosyasına kaydedildi!\n" % { "name2": fileName2, "name": fileName, "gen": data})
  file.close()
  file2.close()


# FONKSİYON / 2
 def createPlainPassword(dataLength):
  print("Şifre oluşturuluyor, biraz bekleyin.")

  create = sample(All, dataLength)

  passw = "".join(create)
  data = [];
  data.clear()
  data.append(passw)

  file.write("""const i = {

 "Password": "%(gen)s", 
 "Name": "%(nm)s",
 "Açıklama": '%(d)s',
 "Durum": "%(sts)s", 
 "Tarih": %(trh)s

};

module.exports = i;""" % { "d": desc, "sts": security, "nm": userName, "trh": time, "gen": passw})

  file2.write(
 """
|---------------------|
| Password: '%(gen)s'
| Name: '%(nm)s'
| Durum: '%(sts)s'
| Description: '%(d)s'
| Tarih: %(trh)s
|---------------------|
 """ % { "d": desc, "sts": security, "nm": userName, "trh": time, "gen": passw})
  print("Şifreniz: %(gen)s \n\n[Uygulama] Şifreniz '%(name)s' ve '%(name2)s' dosyasına kaydedildi!\n" % { "name2": fileName2, "name": fileName, "gen": data})
  file.close()
  file2.close()
 

 if(val == 1): 
  addToCreated(keyLength);


 elif(val == 2):
  createPlainPassword(keyLength);


 else:
  print("Geçersiz işlem!")