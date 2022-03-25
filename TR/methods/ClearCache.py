def ClearCache(Application, fileOne, fileTwo):
  with open(fileOne, "w") and open(fileTwo, "w") as i:
   Application("'%(fileOne)s' ve '%(fileTwo)s' dosyaları temizlendi!" % { "fileOne": fileOne, "fileTwo": fileTwo})