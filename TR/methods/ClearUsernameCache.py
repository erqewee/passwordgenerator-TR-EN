from methods.Application import *;

def ClearUsernameCache(log):
  with open(log, "w") as i:
   App("'%(fileOne)s' dosyası temizlendi!" % { "fileOne": log })