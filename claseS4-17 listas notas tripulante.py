"""
# list( objeto iterable )

nombre = "Alejandro"
listaCaracteres = list( nombre )

print( nombre )
print( listaCaracteres )

print( listaCaracteres[5] )


secuenciaNumerica = range(10 )
listaNumeros = list( secuenciaNumerica )
print( secuenciaNumerica )
print( listaNumeros )

print( type( listaNumeros  ) )


print( list() )
listaDatosDiferentes = [ 2, 3.2, "Texto", True] 

print( type( listaDatosDiferentes) )

for dato in listaDatosDiferentes:
    print( dato, type( dato ) )


# list() --> Falso
# list([1,2,3,4]) --->
print( "Valores relacionados" )
print( bool( [] ) )
print( bool( ["dato", 2] ) )


# operador in

frutas = ["Manzana", "Pera", "Mango", "Piña"]

print( frutas )
print( "Mango" in frutas )
print( "Sandia" in frutas )

frutas[0] = "Sandia"

print( frutas )
print( "Sandia" in frutas )


for fruta in frutas:
    print("Me gusta la fruta", fruta)
"""

"""
tripulante = "Paco"
notas = [ 4, 2.3, 4.6, 5, 4.5]
sumaNotas = 0

for nota in notas:
    sumaNotas += nota

promedio = sumaNotas / len( notas ) 
print( tripulante )
print( f"Las notas de {tripulante} son las siguientes")
for nota in notas:
    print( nota)

print("\nPromedio:", promedio )

"""
tripulantes   = [ "Maria", "Rosa", "Pedro" ]
notas         = [  [ 4, 2.3, 4.6, 5, 4.5],  
                   [ 4, 2.3, 5, 4, 4.5], 
                   [ 4, 2, 4.6, 6, 4.5]]

if len(tripulantes) == len(notas):
    for i in range(len(notas)):
        print( tripulantes[i], "tiene las notas siguientes", notas[i] )
 
else:
    print("Se ha cometido un error al ingresar datos")