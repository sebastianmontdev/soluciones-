libro = 25000
estudiante = 0.15
total = 0

Cliente = input("ingrese si es cliente o estudiante")


if Cliente == "estudiante":
    descuento_estudiante = libro * estudiante - libro 
    print("tiene un 15 % de descuento el total es", descuento_estudiante)
    
    cupon = input("si tiene cupon ingreselo")
    
    if cupon == "LIBRO10":
        
        print("tiene un 10% de descuento el total es", descuento_estudiante * 0.10 - descuento_estudiante)
        
    else:
        print("el precio es:", descuento_estudiante)
        
        
    
elif Cliente == "cliente":
    
    print("el total a pagar es:", libro)
    
    cupon = input("si tiene cupon ingreselo")
    
    if cupon == "LIBRO10":
        
        print("tiene un 10% de descuento el total es", libro * 0.10 - libro)
        
    else:
        print("el precio es:", libro)
    
else:
    print("el precio es:", libro)   