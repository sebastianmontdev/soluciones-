
cantidad = 0.0

for i in range(cantidad):
    
    nota = float(input(f"dijite la nota {i+1}"))
    if 0 <= nota <= 5:
        nota.append(nota)
        break
    else:
        print("la nota debe estar entre 0 y 5")