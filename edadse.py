age = 17
genre = "M"


if (17 < age < 100):
    
    print("eres mayor de edad")
elif (0 < age < 18):
    print("eres menor de edad")

    

elif (genre == "M" or genre == "m" ):
    
    print("usted es hombre")
    

elif(genre == "F" or genre == "f"):
    
    print("usted es mujer")
    
elif(genre == "O" or genre == ""):
    print("usted es una barbie")
    
else:
    print ("invalido")