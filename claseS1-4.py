"""
nombre = "Juan"
apellido = "Guerrero"
nombreCompleto = nombre + apellido

print( nombreCompleto )
print( nombre, apellido )

print( "Su nombre es: {}  {}".format( nombre, apellido ) )
print( f"Su nombre completo es: {nombreCompleto}" )


numero = int(input("Digite un numero: "))
print( f"El numero es { type(numero) } es el dia de su cumple años")

# \n, \t
print("Cuando yo tenía seis años \n  vi en el libro sobre la selva \nvirgen: Historias \nvividas, una grandiosa \nestampa.Representaba \nuna serpiente")

print("Cuando yo tenía seis años \t  vi en el libro sobre la selva \tvirgen: Historias \tvividas, una grandiosa \testampa.Representaba \tuna serpiente")

print( comentario )

imagen = '''
       \\||||//
      =       =    self portrait of
      | "" "" |        Donovan
      -<0>^<0>-
 ,-.  |   j   |
: | :  \ ___ / "PEACE
`/|\'   \ - /    BRO"
 _______|\_/|_______
(       \   /       )
|        \%/        |
|   |     V     |   |
|   |       dwb |   |
|   |           |   |

'''

cita = 'El doctor dijo "El vivira" '
posee = "David's gat "

cuentoMayusculas = cuento.upper() 
cuentoMinusculas = cuentoMayusculas.lower()


#print( cuentoMinusculas )
#print( cuentoMinusculas.capitalize() )

nombre = "Juan"
apellido = "Guerrero"
otroNombre = "Diana"
nombreCompleto = nombre + apellido + otroNombre

#12 elementos
#11 posiciones
#|J|u|a|n|G|u|e|r|r|e|r |o |D
#|0|1|2|3|4|5|6|7|8|9|10|11|12...16

print( nombreCompleto )
print( nombreCompleto[4] )
print( nombreCompleto[11] )
print( nombreCompleto[-1] )

# inicio: final
print( nombreCompleto[4:13] )

# funcion len - longitud
print( len( nombreCompleto ) )
print( nombreCompleto[ len(nombreCompleto) - 1] )


"""

cuento = '''En el libro se afirmaba: 
“La serpiente boa se traga su presa
entera, sin masticarla. 
Luego, como no puede moverse,
duerme durante los seis 
meses que dura su digestión”.
Reflexioné mucho en ese
momento sobre las aventuras de
la jungla y logré trazar con 
lápices de colores mi primer
dibujo. Mi dibujo número 
1 era de esta manera:
'''

print(len(cuento))

dosPuntos = cuento.find(":")

print(cuento[0: dosPuntos + 1])

print("Hola a todos")