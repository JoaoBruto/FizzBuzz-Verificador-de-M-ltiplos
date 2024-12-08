numero = float(input("Digite o número múltiplo de 3, 5 ou 3 e 5: \n"))

if numero % 3 == 0 and numero % 5 == 0:
    print("FizzBuzz")

elif numero % 3 == 0:
    print("Fizz")

elif numero % 5 == 0:
    print("Buzz")

else:
    print("Esse número não é multiplo nem de 3 e nem de 5")