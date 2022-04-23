from methods.Error import Error;
from methods.Application import App;

def OverwriteCreated(sample, passwordLength, desc, security, userName, file, file2, fileName, fileName2, time, chars):
  i = input("Oluşturulan şifreye eklenecek şeyi giriniz: ")
  App("Şifreniz oluşturuluyor, biraz bekleyin...")


  if(passwordLength <= 0):
   App(Error("\"0\" Sayısını ve \"-\" negatif sayılar giremezsiniz."))
  
  else:
   create = sample(chars, passwordLength)
   
   passw = "".join(create)
   
   data = [i];
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