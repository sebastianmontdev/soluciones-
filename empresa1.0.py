nota_t = float(input("ingrese nota 1"))
nota_l = float(input("ingrese nota 2"))
nota_final = (nota_t * 0.7) + (nota_l * 0.3)

if nota_final >= 3:
    
    print("aprobado")
    
elif 2 <= nota_final < 3:
    
    print("revisión")
    
elif nota_final < 2 :
    
    print("reprobado") 