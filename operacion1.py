import math
#C a F
#C=input("Digitegrados Centigrados para Farenheit: ")
#F=(float(C)*1.8)+32
#farenheit=(float(C)*(9/5))+32
#print(F,farenheit,"F")


#C a K
#C=input("Digitegrados Centigrados para Kelvibn: ")
#K=(float(C)+273.15)
#print(K,"K")


#pitagoras 
A=input("ingrese coordenada X: ")
B=input("ingrese coordenada Y: ")

raiz=(math.sqrt(float(A)**2+float(B)**2))

print("La distancia desde punto 0 a las coordenadas indicadas es: ",(round(raiz,2)))

