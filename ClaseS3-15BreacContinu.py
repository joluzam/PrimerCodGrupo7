"""
#Secuencia Fibonacci
Cada nuevo término en la sucesión de Fibonacci se genera sumando los dos términos anteriores. Al comenzar con 1 y 2, los primeros 10 términos serán:

1, 2, 3, 5, 8, 13, 21, 34, 55, 89, ...

Al considerar los términos en la sucesión de Fibonacci cuyos valores no superan los cuatro millones, encuentre la suma de los términos de valor par.

x = 0
y = 1
z = x + y
acumulador = 0
for i in range(100):
  #print(x)
  if x % 2 == 0:
      acumulador += x
  if y > 4000000:
      break
  x = y
  y = z
  z = x + y
print(acumulador)

x = 0
y = 1
aux = x + y
acumulador  = 0
for i in range(100):
    #print(x)
    if x % 2 == 0:
        acumulador += x
    
    if y > 4000000:
        break
    
    x = y
    y = aux
    aux = x + y
print(acumulador) """

c = 0
while True:
    if c > 99:
        break

    c += 1

    if c % 2 != 0:
        continue

    print( c )


for i in range(100):
    if i % 2 == 0:
        continue
    print( i )