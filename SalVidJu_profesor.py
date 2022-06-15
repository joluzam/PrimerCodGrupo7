# alienigenas 
  # rojo  -> 10 puntos
  # verde -> 5 puntos
  # azul  -> 2 puntos

# sumar todos los puntos 

# mas de 10 rojo 
  # bonus 10% sobre el puntaje final

# mas de 5 verdes 
  # bonus 5% sobre el puntaje final

# mas de 2 azules 
  # bonus 2% sobre el puntaje final

# // div entera
#salida
# cantidad y valor total

"""
Por ejemplo:
Ingrese la cantidad de rojos derribados:  2
20
Ingrese la cantidad de verdes derribados: 5
25
Ingrese la cantidad de azules derribados: 12
24
puntaje 69 
puntaje + bonus 1.3 = 70.3
entero
Puntaje total: 70
"""

numeroRojos = int(input("Ingrese la cantidad de rojos derribados: "))
numeroVerdes = int(input("Ingrese la cantidad de verdes derribados: "))
numeroAzules = int(input("Ingrese la cantidad de azules derribados: "))


aliensDerribados = numeroRojos + numeroAzules + numeroVerdes

puntosRojos = numeroRojos*10
puntosVerdes = numeroVerdes*5
puntosAzules = numeroAzules*2

sumaPuntos = puntosRojos + puntosVerdes + puntosAzules
#print("La suma de puntos es: ", sumaPuntos)

bonusRojos = 0
bonusVerdes = 0
bonusAzules = 0

if numeroRojos > 10:
  bonusRojos = 0.1*sumaPuntos

if numeroVerdes > 5:
  bonusVerdes = 0.05*sumaPuntos

if numeroAzules > 2:
  bonusAzules = 0.02*sumaPuntos

totalBonus = bonusAzules + bonusVerdes + bonusRojos

totalPuntos = sumaPuntos + totalBonus

totalPuntos = int(totalPuntos)

print("El total de puntos es: ", totalPuntos )
print("La cantidad de aliens derribados es: ", aliensDerribados)