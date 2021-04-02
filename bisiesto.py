#EJEMPLOA AÑO BISISESTO
'''
anio= input("ingrese el aÃ±o: ")
anio=int(anio)
if(anio%4==0):
    if(anio%100==0):
        if(anio%400==0):
            print("el aÃ±o es bisiesto")
        else: 
            print("el aÃ±o no es bisiesto")
    else:
        print("el aÃ±o es bisiesto")
else:
    print("el aÃ±o no es bisiesto: ")
'''
'''
def multiplicacion():
    mul1=8
    mul2=10
    print(mul1*mul2)
multiplicacion()
'''
'''
def multiplicacion(num1,num2=10):
    print(num1*num2)
multiplicacion(7)
'''
'''
def numeros(*parametros):
    print(parametros)
numeros(5,5,5)
'''
'''
def numeros(*parametros):
    print(parametros)
    print(type(parametros))
    print(parametros[0])
numeros(5,10,1)
'''
'''
def numeros(*parametros):
    return parametros[0]
print(numeros(5,6,7)*10)
'''
from math import pi
radio=float(input("digite el radio: "))

def diametro():
        return radio*2

def circunferencia():
    return pi*diametro()

def area():
    return pi*radio**2
print("==========================CIRCULO===============================")
print("diametro : {}".format(diametro()))
print("circunferencia :{}".format(circunferencia()))
print("area :{} ".format(area()))


