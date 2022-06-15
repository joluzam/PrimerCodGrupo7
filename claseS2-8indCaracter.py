# Identificar el caracter ingresado
# vocales: a,e,i,o,u
# alfabeto: b,c,d,f,g,h,......
# caracter diferente: +,/,',=,$, ....

caracter = input("Digite un caracter: ").lower()

vocales = 'aeiou'
alfabeto ='abcdefghijklmnopqrstuvwxyz'

#"".find()
# len ( string ) => longitud del string

if len(caracter) == 1:
  
  if caracter in vocales:
    print("Es una vocal")
    
  elif caracter in alfabeto:
    print("Es una consonante")
  else:
    print("No es una letra")
else:
  print("Entrada no valida. Ingrese SOLO UN CARACTER.")

# demostrativo. no es necesario aprenderlo --->
#ord() # caracter utf32
#chr() # utf32 caracter

if ord(caracter) >= 97 and ord(caracter) <= 122:
  print("Hace parte del afabeto")