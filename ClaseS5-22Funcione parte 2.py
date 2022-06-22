# funcines
# saludar
# interface
# sum() 
# sqrt() # raiz cuadrada # valor**(1/2)

def saludo( nombre ):
    print(f"Hola {nombre}")
    print("Como se encuentra?")

def mostrarCalculadora( interface ):
    print( interface )

def editarCalculadora( interface ):
    pass

def sumarLaLista( lista ):
    sumador = 0
    for valor in lista:
        sumador += valor
    return sumador

if __name__ == "__main__":
    #print("El codigo deberia comenzar aca")
    numeros = [1,2,3,4,5]
    print( sumarLaLista(numeros) )