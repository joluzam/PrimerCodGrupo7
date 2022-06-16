# identificar si un año es bisiesto

# multiplo 4
# no multiplo 100
# multiplo 400

año = int(input("Ingrese un año: "))

#and *
# or +

if  año % 4 == 0  and año % 100 != 0 or año % 400 == 0: 
  print("el año es bisiesto")
else:
  print("No es un año bisiesto")