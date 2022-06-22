#import os
from os import system

INTERFACE = """
----------------------------
\tENCRIPTADOR PYTHONICO

Opciones:
[E]ncriptar
[D]esncriptar
[S]salir

----------------------------
"""


CRIPTO = {
'a': 'm',
'b': 'q',
'c': 'w',
'd': 'u',
'e': 'y',
'f': 'g',
'g': 'z',
'h': 'k',
'i': 'f',
'j': 'c',
'k': 'r',
'l': 's',
'm': 'p',
'n': 'x',
'o': 'o',
'p': 'l',
'q': 't',
'r': 'h',
's': 'a',
't': 'd',
'u': 'e',
'v': 'v',
'w': 'i',
'x': 'n',
'y': 'b',
'z': 'j',
' ': ' '
}


def genDiccionerioCripto( ):
    import random
    
    ALFABETO ='abcdefghijklmnopqrstuvwxyz'
    alfabetoRadom = []
    
    while len(alfabetoRadom) != len(ALFABETO):
        numRandom = random.randint( 97, 122 ) # a, 97 - z, 122
        if chr( numRandom ) not in alfabetoRadom:
            alfabetoRadom.append( chr(numRandom ))
    
    cripto = {}
    for i, letra in enumerate( ALFABETO ):
        cripto[letra] = alfabetoRadom[i]

    return cripto


def encriptar():
    system("clear")
    print("\tEncriptador")
    texto = input("Ingrese el mensaje que desea Encriptar:\n").lower()
    textoEncriptado = ""

    for letra in texto:
        #print(textoEncriptado, CRIPTO[letra])
        textoEncriptado += CRIPTO[letra]

    return textoEncriptado
        

def desencriptar():
    system("clear")
    print("\tDesencriptador")
    textoEncriptado = input("Ingrese el mensaje que desea desencriptar:\n")
    textoReal = ""

    for letra in textoEncriptado:
        #print(textoEncriptado, CRIPTO[letra])
        textoReal += CRIPTO[letra]

    return textoReal
    


def loop():
    
    while True:
        system("clear")
        print( INTERFACE )
        opcion = input("Ingrese opcion: ").lower()

        if opcion == 'e':
            mensaje = encriptar()
            print("Su mensaje a sido encriptado y es")
            print( mensaje )
            
        elif opcion == 'd':
            pass
            
        elif opcion == 's':
            print("Gracias por usar el encriptador Pythonico")
            break
        else:
            print("Ha ingresado una opcion no valida")

        input()
        
#kosm dhflesmxdya