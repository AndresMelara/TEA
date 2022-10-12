def CalcularSalario(horas, tarifa):
    horas_extras = horas - MAX_HORAS_SEMANALES
    if (horas_extras > 0):
        pago = (MAX_HORAS_SEMANALES * tarifa) + (horas_extras * (tarifa*1.5))
    else:
        pago = horas * tarifa
    return pago

MAX_HORAS_SEMANALES = 40
horas = int(input("ingrese el número de horas trabajadas: "))
tarifa = float (input ("Ingrese tarifa por hora: "))
salario = CalcularSalario(horas, tarifa) 
print(salario)    