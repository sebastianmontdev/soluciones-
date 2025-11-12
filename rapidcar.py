hora = 2000

tarifa = int(input("ingrese el numero de horas"))
multa = 5000
if tarifa <= 0:
    
    print("debe ingresar un numero mayor de 0")
    
elif tarifa > 5 :
    
    print("el valor del parqueadero es con penalizacion por pasarse del tiempo es", tarifa * hora + multa)
    
elif tarifa <= 5 :
    
    print("el valor del parqueadero es:", tarifa * 2000)
    
else:
    print("debe ingresar numeros")