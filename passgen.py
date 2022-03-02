from random import sample
from string import ascii_letters, ascii_lowercase, ascii_uppercase, punctuation, digits
from datetime import datetime
All = (ascii_letters + ascii_lowercase + ascii_uppercase + punctuation + digits)

userName = input("Adınızı Giriniz: ")

if(userName == ""):
 userName += "None"
 
val = int(input("İşlem Türünü seçiniz! (Oluşturana ekle - 1 | Düz oluştur - 2 | Şifreleri Göster - 3): "))

fileName = "lastCreatedPassword-log.js"
file = open(fileName, "w", encoding = "utf-8")

fileName2 = "allCreatedPassword-logs.txt"
file2 = open(fileName2, "a", encoding = "utf-8")

# İçerikleri oku
def readCreatedPasswords(readFile):
   with open(readFile) as i:
    print(i.read())
    print("Sistem uygulamayı başarılı bir şekilde çalıştırdı!")

if(val == 3):
 print("Sistem uygulamayı başlatmayı deniyor...")
 readCreatedPasswords(fileName2);

else:
 keyLength = int(input("Uzunluk Sayısını Giriniz: "))

 if(keyLength >= 100):
  print("Sistem Hatası, Max 100 uzunlukta şifre oluşturabilirsiniz.")

 today = datetime.today()
 time = """{ "Year": "%(year)s", "Ay": "%(month)s", "Day": "%(day)s", "Saat": "%(hour)s:%(minute)s:%(second)s" }""" % { "year": today.year, "month": today.month, "day": today.day, "hour": today.hour, "minute": today.minute, "second": today.second } 

 security = ""

 if(keyLength == 0):
  print("0 yazılamaz")
 
 if(keyLength <= 4):
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
"Durum": '%(sts)s', 
"Tarih": %(trh)s

};

 """ % { "sts": security, "nm": userName, "trh": time, "gen": passw + i})

  file2.write(
 """
Password: '%(gen)s'
Name: '%(nm)s'
Durum: '%(sts)s'
Tarih: %(trh)s
 """ % { "sts": security, "nm": userName, "trh": time, "gen": passw + i})
  print("Şifreniz: %(gen)s \n\nSistem: Şifreniz '%(name)s' ve '%(name2)s' dosyasına kaydedildi!" % { "name2": fileName2, "name": fileName, "gen": data})
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
 "Durum": "%(sts)s", 
 "Tarih": %(trh)s

};

 """ % { "sts": security, "nm": userName, "trh": time, "gen": passw})
  file2.write(
 """
Password: '%(gen)s'
Name: '%(nm)s'
Durum: '%(sts)s'
Tarih: %(trh)s

 """ % { "sts": security, "nm": userName, "trh": time, "gen": passw})
  print("Şifreniz: %(gen)s \n\nSistem: Şifreniz '%(name)s' ve '%(name2)s' dosyasına kaydedildi!" % { "name2": fileName2, "name": fileName, "gen": data})
  file.close()
 
 if(val == 1): 
  print("Sistem uygulamayı başlatmayı deniyor...")
  addToCreated(keyLength);

 elif(val == 2):
  print("Sistem uygulamayı başlatmayı deniyor...")
  createPlainPassword(keyLength);

 else:
  print("Geçersiz işlem!")