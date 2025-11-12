menu = 12000
bebida = 3000
iva = 0.08
resp = input("quiere bebida con su comida?")

if resp == "si":
    combo = menu + bebida
    print("el total con iva es:", combo * iva + combo)
elif resp == "no":
    print("el total con iva es:", menu * iva + menu)
    
else:
    print("dato invalido")