# Programa para calcular pago por hora con horas extra
def calcularSalario(horas,tarifa):
    horas_extras = horas - MAX_HORAS_SEMANALES
    if (horas_extras > 0):
        pago = (MAX_HORAS_SEMANALES * tarifa) + (horas_extras * (tarifa*1.5))
    else:
        pago = horas * tarifa
    return pago

try:
    MAX_HORAS_SEMANALES = 40
    horas = int(input("Dijite la cantidad de horas por semana que trabajo: "))
    tarifa = float(input(" Dijiste su pago por hora: "))
    salario = calcularSalario(horas,tarifa)
    print("Salario: " , salario)
except:
    print ("Error, debe ingresar un valor numerico")


#horas_extras = int(horas) - MAX_HORAS_SEMANALES
#if (horas_extras > 0):
#    salario = (MAX_HORAS_SEMANALES * tarifa) + (horas_extras * (tarifa*1.5)) 
#else:
#    salario = horas * tarifa
