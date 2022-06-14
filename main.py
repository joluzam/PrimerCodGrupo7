#Decenas, centenas, ¡unidades!
#Jorge Luis Zabala Medrano

numero = input("numero:")
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
