RojosDerribados = int(input("Digita la cantidad de aliens rojos derribados: "))
VerdesDerribados = int(input("Digita la cantidad de aliens verdes derribados: "))
AzulesDerribados = int(input("Digite la catidad de  aliens azules derribados: "))

AliensDerribados = RojosDerribados + AzulesDerribados + VerdesDerribados

sumaPuntos = (RojosDerribados*10) + (VerdesDerribados*5) + (AzulesDerribados*2)

BonoRojos = 0
if RojosDerribados > 10:
  BonoRojos = 0.1*sumaPuntos
BonoVerdes = 0
if VerdesDerribados > 5:
  BonoVerdes = 0.05*sumaPuntos
BonoAzules = 0
if AzulesDerribados > 2:
  BonoAzules = 0.02*sumaPuntos

totalBono = BonoAzules + BonoVerdes + BonoRojos

totalPuntos = sumaPuntos + totalBono

totalPuntos = int(totalPuntos)

print("El total de puntos es: ", totalPuntos )
print("La cantidad de aliens derribados es: ", AliensDerribados)