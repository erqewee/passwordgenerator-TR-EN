def ClearLogs(fileOne, fileTwo):
  with open(fileOne, "w") and open(fileTwo, "w") as i:
   print("'%(fileOne)s' ve '%(fileTwo)s' Temizlendi!" % { "fileOne": fileOne, "fileTwo": fileTwo})