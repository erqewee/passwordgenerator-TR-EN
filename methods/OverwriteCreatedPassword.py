def OverwriteCreated(sample, passwordLength, desc, security, userName, file, file2, fileName, fileName2, time, chars, Error, Application):
  i = input("Enter the password you want added: ")
  print("Creating your password, please wait...")


  if(passwordLength == 0):
   Application(Error("Don't enter \"0\" number."))
  
  else:
   create = sample(chars, passwordLength)

   passw = "".join(create)
   data = [];
   data.clear()
   data.append(passw + i)

   file.write("""const i = {
 
"Password": ['%(gen)s'],

"Name": '%(nm)s',
"Description": '%(d)s',
"Status": '%(sts)s', 
"Date": %(trh)s

};

module.exports = i; """ % { "d": desc, "sts": security, "nm": userName, "trh": time, "gen": passw + i})

   file2.write(
 """
|-----------------------|
| > Password: '%(gen)s'
|-----------------------|
| Name: '%(nm)s'
| Description: '%(d)s'
| Status: '%(sts)s'
| Date: %(trh)s
|-----------------------|
 """ % { "d": desc, "sts": security, "nm": userName, "trh": time, "gen": passw + i})
   Application("""
   Your password: %(gen)s
   
   Your password has been saved in the '%(name)s' and '%(name2)s' file! """ % { "name2": fileName2, "name": fileName, "gen": data})
   
   file.close();
   file2.close();