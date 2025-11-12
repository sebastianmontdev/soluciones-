producto = 2000
cantidad = int(input("ingrese la cantidad de productos"))
resultado = cantidad * producto
if cantidad < 10:
    
    print("el total de los productos es:", resultado )
elif  cantidad == 10 & cantidad < 30:
        print("el total de los productos es:", resultado * 0.15 - resultado)
elif cantidad >= 30:
    print("el total de los productos es:", (resultado * 0.15 - resultado) + 5000)
else:
    print("error")