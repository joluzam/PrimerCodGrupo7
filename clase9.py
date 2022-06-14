
# Entradas
# Ingrese un valor del prestamo 
# numero de cuotas mes

# Salida
# ValorTotal
# ValorPorCuota
# interesesPermanentes

# caso 1
# valor del prestamo < 500'000
# valortotal +10%
# cadaCuota +3%

# caso 2
# valor del prestamo >= 500'000 y < 1'000'000
# valortotal +7%
# cadaCuota +5%

# caso 3
# valor del prestamo >= 1'000'000
# valortotal +5%
# cadaCuota +9%

print("\tPrestamos rapidos\n\n")

valorInicial = float(input("Digite el valor del prestamo: "))
numeroCuotas = int( input("Digite el numero de cuotas: "))  

if valorInicial > 0 and numeroCuotas > 0:
  
  if valorInicial < 500000:
    x = valorInicial*0.10 + valorInicial
    y = numeroCuotas*0.03
  
  elif valorInicial >= 500000 and valorInicial < 1000000:
    x = valorInicial*0.07 + valorInicial
    y = numeroCuotas*0.05
  
  elif valorInicial > 1000000:
    x = valorInicial*0.05 + valorInicial
    y = numeroCuotas*0.09
    
  valorPorCuota = (x + y)/numeroCuotas
  valorTotal = x + y
  print("Valor Total: ", valorTotal)
  print("Valor por cuota: ", valorPorCuota) 


else:
  print("El numero no es valido")