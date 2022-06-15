"""
Realice un programa que pida un número por pantalla y verifique si es par o impar.

Pista: Utilice el operador de modulo (%) el cual retorna el residuo de la división entre un número y otro, si el resultado del residuo entre los dos números es cero quiere decir que la división fue exacta y el primer número es divisible entre el segundo.

El output del programa debe mostrar un mensaje igual a alguno de estos, dependiendo sea el caso:

"es par" en el caso de que sea par

"es impar" en el caso de que sea impar

De esta forma se debería mostrar en pantalla con todo en minúsculas, para así garantizar la mejor nota!
"""
Numero = int(input("Ingrese el numero a evaluar: "))
if Numero % 2 == 0:
  
    print("es par")
else:
    print("es impar")