"""
#variable  operador= valor

numero = 10
print(numero, "\n")

numero += 5
print(numero, "\n")

numero -= 10
print(numero, "\n")

numero *= 5
print(numero, "\n")

numero /= 2
print(numero, "\n")

numeroAux = numero
numeroAux /= 2
numero //= 2

#print("Div normal: ", numeroAux)
#print("Div entera: ", numero)

numero = 10
print("div normal", 7504 / 12)
print("div %modulo", 7504 % 12)

print(10%3)

#Multiplo de un numero
numero = 151

if numero % 2 == 0:
  print(f"El numero {numero}  es par")
else:
  print(f"El numero {numero}  es impar")

if numero % 3 == 0:
  print(f"El numero {numero}  multiplo de 3")
else:
  print(f"El numero {numero}  no es multiplo de 3")
"""




#Digite un numero
#Genere una salida donde sea el numero invertido
#ejemplo
  #entrada:         1234
  #salida esperada: 4321

numero = 8943
print(numero)

u = numero % 10
numero //= 10
print(numero)
print(u)

d = numero % 10
numero //= 10
print(numero)
print(d)

c = numero % 10
numero //= 10
print(numero)
print(c)

m = numero % 10
numero //= 10
print(numero)
print(m)

numero = u*1000 + d*100 + c*10 + m*1
print("Salida: ", numero)

print("---------------------------")

print(numero)
numero = str(numero)
numero = numero[3] + numero[2] + numero[1] + numero[0]
numero = int(numero)
print(numero)

print(str(numero)[::-1] )