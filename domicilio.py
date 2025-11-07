
print("se recibe la llamada")
print("verificar la disponibilidad de lo que quiere el cliente")
disponibilidad = input("hay disponibilidad del producto?")
pedido = ""


if disponibilidad == "no" :
    
    print("ofrecer otro producto")
    nuevo_producto = input("el cliente acepto otro producto?")
    
    
    if nuevo_producto == "si" :
        
        print("verificar comanda")
        print("preparar pedido")
        print("enviar delibery")
        pedido = input("el pedido fue entregado y se recibio el dinero?")
        
        if pedido == "si":
            
            print("buen trabajo obtuvimos la ganacia")
        
        else:
            
            print("dato incorrecto")
            
    elif nuevo_producto == "no":
            
            print("cancelar pedido")
            
        
            
            
    else:
            
            print("dato incorrecto")
            
            
            
            
    
elif disponibilidad == "si" :
    
    print("verificar comanda")
    print("preparar pedido")
    print("enviar delibery")
    pedido = input("el pedido fue entregado y se recibio el dinero?")
    
    if pedido == "si":
        
        print("buen trabajo obtuvimos la ganacia")
        
    elif pedido == "no":
        
        print("cancelar pedido")
    
    else:
        
        print("dato incorrecto")

else :
    
    print("dato incorrecto")

