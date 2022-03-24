def ClearCache(fileOne, fileTwo):
  with open(fileOne, "w") and open(fileTwo, "w") as i:
   print("'%(fileOne)s' and '%(fileTwo)s' cleared password cache!" % { "fileOne": fileOne, "fileTwo": fileTwo})