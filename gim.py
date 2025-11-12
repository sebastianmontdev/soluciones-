dias_entreno = int(input("ingrese dias que va a entrenar"))

if dias_entreno <= 1:
    
    print("no aflojes tu puedes mejorar")

elif dias_entreno <= 3 :
    
    print("Bien, pero puedes dar más")
    
elif dias_entreno >= 4 :
    
    print("¡Excelente disciplina! + gana 1 punto de energía")
    
else:
    print("error")