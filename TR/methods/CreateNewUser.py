def NewUser(Application, randomName, Error, file, log):
 i = input("İsmin Cinsiyetini Seçiniz (Male [Erkek] | Female [Kız]): ")

 data = [];
 data.clear()


 if((i == "Male") or (i == "male") or (i == "erkek")):
  boy = randomName(gender = "Male");
  data.append(boy)

  Application(
  """
  Kullanıcı Adı: %(name)s

  Kullanıcı adı '%(filename)s' dosyasına kaydedildi!
  """ % { "name": data, "filename": file })

  log.write(
  """
|---------------------|
| > Ad: '%(name)s'
|---------------------|
| Cinsiyet: Erkek
|---------------------|
  """ % { "name": boy })
  log.close();


 elif((i == "Female") or (i == "female") or (i == "kız") or (i == "kadın")):
  girl = randomName(gender = "Female");
  data.append(girl)

  Application(
  """
  Kullanıcı Adı: %(name)s

  Kullanıcı adı '%(filename)s' dosyasına kaydedildi!
  """ % { "name": data, "filename": file })

  log.write(
  """
|---------------------|
| > Ad: '%(name)s'
|---------------------|
| Cinsiyet: 'Kız / Kadın'
|---------------------|
  """ % { "name": girl })
  log.close();


 else:
  Application(Error("Böyle cinsiyet bulunamadı!"))