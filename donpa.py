pan = 300
cantidad_panes = int(input("ingrese el numero de panes que va a comprar"))
precio_final = pan * cantidad_panes
descuento_10 = precio_final * 0.10
descuento_20 = precio_final * 0.20

if cantidad_panes == 20 :
    
     print("el total de saldo es " , precio_final - descuento_10 )
     
elif cantidad_panes == 50 :
    
    print("el total de saldo es " , precio_final - descuento_20 )
    
elif cantidad_panes < 0 :
    
    print("cantidad invalida")
    
else :
    
    print("el total del saldo es " , precio_final)
    