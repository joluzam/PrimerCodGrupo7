#Decenas, centenas, ¡unidades!
"""
numero = input("Ingrese numero entero a evaluar: ")
denominacion = (len(numero))
if denominacion == 1:
    print("unidad")
elif denominacion == 2:
      print("decena")
elif denominacion == 3:
      print("centena")
elif denominacion == 4:
      print("milésima")
elif denominacion == 5:
      print("decena de mil")
elif denominacion == 6:
      print("centena de mil")
else:
    print("fuera de rango")  

"""
numero = int (input ('Ingresa el valor de numero: '))

unidades=numero%10
decenas=(numero%100-unidades)//10
centenas=(numero%1000-decenas)//100
milesima=(numero%10000-centenas)//1000
decenaDeMil=(numero%100000-decenas)//10000
centenaDeMil=(numero%1000000-decenas)//100000


dig= str(numero)

print( f"digitos:{len( dig )}")

print (f'unidades:{(unidades)}')
print (f'decenas:{(decenas)}')
print (f'centenas:{(centenas)}')
print (f'milesima:{(milesima)}')
print (f'decena de mil:{(decenaDeMil)}')
print (f'centena de mil:{(centenaDeMil)}')