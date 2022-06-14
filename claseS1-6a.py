print("Cine TIC\n\n")

edad = int(input("Digite su edad: "))
edadMinima = 18
condicion = edad >= edadMinima #Salida booleana

# True             False
# 1                  0
# bool("existe")   bool("")

print( f"La edad minima para ingresar es {edadMinima} \n\n" )



if edad >= edadMinima:
  print("Cumple la edad minima. Puede ingresar.")
else:
  
  #estaAcompañado = input("Usted esta acompañado? ")
  #estaAcompañado = estaAcompañado.lower()
  if edad > 0:
    estaAcompañado = input("Usted esta acompañado? ").lower()
    if estaAcompañado == 'si':
      print("No cumple la edad minima, pero se encuentra acompañado. Puede ingresar")

    elif estaAcompañado == 'no':
      print("No cumple la edad minima y no se encuentra acompañado. No puede ingresar")   
    else:
      print("Ha ingresado un valor no valido. Vuelva a correr el programa")
  else:
    print("Ha ingresado una edad no valida")


print("\n\nGracias por venir al cine TIC")
