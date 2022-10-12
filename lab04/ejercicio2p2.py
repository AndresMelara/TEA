#Programa que calcula numeros maximos y minimos
numeromaximo = 0
numerominimo = 0
primer_numero = True
while True:
    try:
        input_str = input("Ingrese un numero: ")
        if (input_str == "Fin"):
            break
        else:
            if (primer_numero):
                numeromaximo = int(input_str)
                nnumerominimo = int(input_str)
                primer_numero = False
            else:
                if (int(input_str) > numeromaximo): numeromaximo = int(input_str)
                if (int(input_str) < numerominimo): numerominimo = int(input_str)
    except:
        print("Valor no es valido")
        continue
    print("Maximo:", numeromaximo)
    print("Minimo:", numerominimo)