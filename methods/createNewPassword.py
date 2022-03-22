def createNewPassword(sample, passwordLength, desc, security, userName, file, file2, fileName, fileName2, time, chars):
  print("Şifre oluşturuluyor, biraz bekleyin.")

  create = sample(chars, passwordLength)

  passw = "".join(create)
  data = [];
  data.clear()
  data.append(passw)

  file.write("""const i = {

 "Password": "%(gen)s", 

 "Name": "%(nm)s",
 "Description": '%(d)s',
 "Status": "%(sts)s", 
 "Date": %(trh)s

};

module.exports = i;""" % { "d": desc, "sts": security, "nm": userName, "trh": time, "gen": passw})

  file2.write(
 """
|---------------------|
| Password: '%(gen)s'
|---------------------|
| Name: '%(nm)s'
| Status: '%(sts)s'
| Description: '%(d)s'
| Date: %(trh)s
|---------------------|
 """ % { "d": desc, "sts": security, "nm": userName, "trh": time, "gen": passw})
  print("Şifreniz: %(gen)s \n\n[Uygulama] Şifreniz '%(name)s' ve '%(name2)s' dosyasına kaydedildi!\n" % { "name2": fileName2, "name": fileName, "gen": data})