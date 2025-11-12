TARIFA_N = 500
TARIFA_P = 750
penalty = 2000
FINDE = True
def Consultar_tarifas (ride, time,base_amount,discount,total_cost,day,surcharge):
    text = f"""El tipo de bicicleta fue: {ride}
El tiempo que fue usado fue de: {time}min
Con un precio base de: ${base_amount} por minuto\n"""
    if discount == True: 
        text += "Tuvo un descuento de: 10%\n"   
    if day == True :
        text += f"Y un recargo por ser fin de semana de: 5%\n"
    if surcharge == True:
        text += f"Con una penalizacion de ${penalty} por devolverla tarde\n"
        
    text += f"VALOR TOTAL A APAGAR: {total_cost}"
    
    return text



print(Consultar_tarifas("normal", 20 , TARIFA_N, False, (20 * TARIFA_N),False, False))