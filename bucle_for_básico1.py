print("Ejercicio 1: Básico")
for i in range(101):
    print(i)

print("Ejercicio 2: Múltiples de 2")
for i in range(2, 501, 2):
    print(i)
  
print("Ejercicio 3: Contando Vanilla Ice")
for i in range(1, 101):
    if i % 10 == 0:
        print("baby")
    elif i % 5 == 0:
        print("ice ice")
    else:
        print(i)

print("Ejercicio 4: Wow. Número gigante a la vista")
suma = 0
for i in range(0, 500001, 2):
    suma += i
print("Suma:", suma)

print("Ejercicio 5: Regrésame al 3")
for i in range(2024, 0, -3):
    print(i)

print("Ejercicio 6: Contador dinámico")
numInicial = 2
numFinal = 20
multiplo = 2
for i in range(numInicial, numFinal + 1):
    if i % multiplo == 0:
        print(i)

