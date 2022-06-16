
nombresGeneral    = ["Maria", "Pedro", "Marta", "Juan", "Raul"]
notasGeneral      = [[ 2.3, 5.0, 1.2], 
                  [ 3.5, 2.4, 4.2], 
                  [ 5.0, 3.0, 2.2],
                  [ 2.2, 4.0, 1.2],
                  [ 1.3, 5.0, 4.1]]  
"""
# Tripulantes
nombres = []

# lista de las lista de cada uno de los tripulantes
listasDeNotas = []

numeroDeTripulantes = int( input("Ingrese el numero de tripulantes: ") )

#Ingreso de tripulantes
for i in range( numeroDeTripulantes ):
    nombre = input("Ingrese el nombre del tripulante: ")
    nombres.append( nombre )

#Ingreso de lista de notas
for i in range( numeroDeTripulantes ):
    #Lista vacia por tripulante
    listaDeNotas = []
    numeroDeNotas = int( input(f"Cuantas notas tiene {nombres[i]} "))

    #ingreso de nota a la lista
    for x in range( numeroDeNotas ):
        nota = float( input( f"nota {x+1}: "))
        listaDeNotas.append( nota )

    #ingreso de la lista de notas del tripulante
    #a la lista general
    listasDeNotas.append( listaDeNotas )
"""


frutas = ["Durasno", "Mandarina", "Kiwi"]
print( len(frutas), "frutas", frutas )

# append
frutas.append("Mora")
print( len(frutas), "frutas",  "append" , frutas )

# insert
frutas.insert( 0 ,"Manzana")
print( len(frutas), "frutas",  "insert" , frutas )

# insert fuera del rango
frutas.insert( -1, "Granadilla")
print( len(frutas), "frutas",  "insert" , frutas )

#nueva lista de comdias
granos = ["lentejas", "Frijoles", "garbanzos"]
print( len(granos), "granos",  "     " , granos )

#operador +
comidas = frutas + granos
print( len(comidas), "comidas",  "  +  " , comidas )

#extend
frutas.extend( granos )
print( len(frutas), "frutas",  "extend" , frutas )
