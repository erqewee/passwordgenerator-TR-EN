def ReadAll(nameOne, nameTwo):
  with open(nameOne) as data1:
   print(data1.read());
  
  with open(nameTwo) as data2:
    print(data2.read());