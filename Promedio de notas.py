# pedir un nombre
# pedir la cantidad de notas tomadas 
# pedir el valor de cada nota
# obtener el promedio de las notas
# imprimir el nombre y el promedio de esa persona
nombre = input("Ingrese Un Nombre: ").capitalize()
numeroNotas= int(input("ingrese el numero de notas: "))
c = 0
sumaNotas = 0
while c < numeroNotas:
  sumaNotas += float(input(f"Ingrese el Valor de nota # {c}:\t"))
  c += 1
  promedio = sumaNotas
  print(f"{nombre} tiene un promedio de { round(promedio, 3) }")