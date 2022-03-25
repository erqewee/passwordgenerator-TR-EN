def ReadAll(Application, nameOne, nameTwo):
  with open(nameOne) as data:
   print(data.read());
  
  with open(nameTwo) as data:
    print(data.read());