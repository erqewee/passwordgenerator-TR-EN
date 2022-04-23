from methods.Error import Error;
from methods.Application import App;

def NewPassword(sample, passwordLength, desc, security, userName, file, file2, fileName, fileName2, time, chars):
  print("Şifreniz oluşturuluyor, biraz bekleyin...")



  
  if(passwordLength <= 16):
    passwordLength = 16

    App("Şifre uzunluğu '16' sayısının altında olduğu için '16' olarak ayarlandı!")
    
  else:
    passwordLength = passwordLength

  if(passwordLength <= 0):
   App(Error("\"0\" Sayısını ve \"-\" negatif sayılar giremezsiniz."))

  else:
   create = sample(chars, passwordLength)
   passw = "".join(create)
   
   data = [];
   data.clear()
   data.append(passw)

   file.write("""const pass = {

 "Şifre": ['%(data)s'], 

 "Ad": "%(nm)s",
 "Açıklama": '%(d)s',
 "Durum": "%(sts)s", 
 "Tarih": %(trh)s

};

module.exports = pass;""" % { "d": desc, "sts": security, "nm": userName, "trh": time, "data": passw})

   file2.write(
 """
|---------------------|
| > Şifre: '%(gen)s'
|---------------------|
| İsim: '%(nm)s'
| Durum: '%(sts)s'
| Açıklama: '%(d)s'
| Tarih: %(trh)s
|---------------------|
 """ % { "d": desc, "sts": security, "nm": userName, "trh": time, "gen": passw})
   App(
    """
    Şifreniz: %(gen)s 
    
    Şifreniz '%(name)s' ve '%(name2)s' dosyalarına kaydedildi! \n""" % { "name2": fileName2, "name": fileName, "gen": data})
   
   file.close();
   file2.close();