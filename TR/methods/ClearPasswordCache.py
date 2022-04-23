from methods.Application import *;

def ClearPasswordCache(fileOne, fileTwo):
  with open(fileOne, "w") and open(fileTwo, "w") as i:
   App("'%(fileOne)s' ve '%(fileTwo)s' dosyaları temizlendi!" % { "fileOne": fileOne, "fileTwo": fileTwo})