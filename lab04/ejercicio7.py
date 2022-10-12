#Programa que calcula calificación
puntos = float (input("Ingrese sus puuntos obtenidos: "))
if puntos < 0.0 or puntos > 10.0:
    print ("Fuera de rango. Debe colocar puntuación entre 0.0 y 10.0")
else:
    if puntos > 9.0:
        print("Sobresaliente")
    elif puntos >= 8.0 and puntos < 9.0:
        print("Notable")
    elif puntos >= 7.0 and puntos < 8.0:
        print("Bien")
    elif puntos >= 6.0 and puntos < 7.0:
        print("Suficiente")
    else:
        print("insuficiente") 
