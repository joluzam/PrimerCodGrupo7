# funcines
# saludar
# interface
# sum() 
# sqrt() # raiz cuadrada # valor**(1/2)
"""
def saludo( nombre ):
    print(f"Hola {nombre}")
    print("Como se encuentra?")

saludo("Erick")
saludo("Pedro")
saludo("Martin")
"""
"""
nombre1 = "Erick"
nombre2 = "matias"
nombre3 = "jose"
nombre4 = "camila"

print(f"Hola {nombre1}")
print(f"Hola {nombre2}")
print(f"Hola {nombre3}")
print(f"Hola {nombre4}")
"""
"""
print("Hola Matias")
print("Hola Jose")
print("Hola Camila")
"""
'''
menu = """
-----------------------------
\t\t\tCalculadora

opciones:
[a]dicion
[r]esta
[m]ultiplicacion
[d]ivision

[s]alida
-----------------------------
"""

def mostrarCalculadora( interface ):
    print( interface )

def editarCalculadora( interface ):
    pass

mostrarCalculadora( menu )
'''

numeros = [1,2,3,4,5]
#print( sum( numeros ) )

def sumarLaLista( lista ):
    sumador = 0
    for valor in lista:
        sumador += valor
    return sumador

resultado = sumarLaLista( numeros )

print( resultado+56 )