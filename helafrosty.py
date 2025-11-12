helado_C = 4000
helado_V = 3.500
sabor = input("ingrese sabor de helado")
topping = 1000

if sabor == "chocolate":
    
    respuesta = input("quiere topping?")
    
    if respuesta == "si":
        print("total:", helado_C + topping)