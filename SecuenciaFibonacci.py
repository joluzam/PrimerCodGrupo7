#Secuencia Fibonacci
x = 0
y = 1
z = x + y
for i in range(15):
  print(x)
  x = y
  y = z
  z = x + y