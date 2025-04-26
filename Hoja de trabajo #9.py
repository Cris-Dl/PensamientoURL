#Ejercicio 1
# def num(n):
#     if n%2==0:
#         print("El número es par")
#     else:
#         print("El número es impar")
# num(9)

#Ejercicio 2
#lista=[]
# def suma_lista(lista):
#     sumatotal=sum(lista)
#     print("Su suma es de: ", sumatotal)
# num=int(input("Ingrese el número o ingrese cero para salir: "))
# lista.append(num)
# while num!=0:
#     num=int(input("Ingrese otro número o ingrese cero para salir"))
#     lista.append(num)
# suma_lista(lista)

#Ejercicio 3
# def cuenta_regresiva(n):
#     if n<0:
#         print("¡Despegue!")
#     else:
#         print(n)
#         cuenta_regresiva(n-1)
# cuenta_regresiva(5)

#Ejercicio 4
# def cuenta_aumenta(n):
#     if n<1:
#         print("El número debe ser mayor a 0")
#     else:
#         if n==1:
#             print(1)
#         else:
#             cuenta_aumenta(n-1)
#             print(n)
# cuenta_aumenta(4) 

#Ejercicio 5
# def suma_hasta(n):
#     if n<0:
#         print("El número debe sey mayor a 0")
#     else:
#         suma=n*(n+1)//2
#         print("La suma es:", suma)
# suma_hasta(8)

#Ejercicio 6
# def factorial(n, acumulador=1):
#     if n > 1:
#         factorial(n - 1, acumulador * n)
#     else:
#         print(acumulador)
# factorial(5)

#Ejercicio 7
# def minimorec(lista, minimoact):
#     if not lista:
#         print(minimoact)
#         return
#     primer = lista[0]
#     resto = lista[1:]
#     if primer < minimoact:
#         nuevomin = primer
#     else:
#         nuevomin = minimoact
#     minimorec(resto, nuevomin)
# def minimo(lista):
#     if not lista:
#         return
#     minimorec(lista[1:], lista[0])
# lista2 = [5, 3, 8, -1, 2]
# minimo(lista2)
# listavacia = []
# minimo(listavacia)

#Juego
# import time
# def adivinar(secreto, restantes, inicio):
#     if restantes <= 0:
#         print(f"\n¡Se acabaron tus intentos! El número secreto era {secreto}.")
#         return
#     intento_str = input(f"Intento #{iniciales - restantes + 1}: Ingresa tu número: ")
#     try:
#         intento = int(intento_str)
#     except ValueError:
#         print("¡Entrada inválida! Por favor, ingresa un número entero.")
#         return adivinar(secreto, restantes, inicio)
#     if intento == secreto:
#         tiempo_total = time.time() - inicio
#         print(f"¡Felicidades! ¡Adivinaste el número {secreto} en {iniciales - restantes + 1} intentos!")
#         print(f"Te tomó {tiempo_total:.2f} segundos.")
#         return
#     elif intento < secreto:
#         print("Demasiado bajo. ¡Intenta de nuevo!")
#     else:
#         print("Demasiado alto. ¡Intenta de nuevo!")
#     adivinar(secreto, restantes - 1, inicio)
# def iniciar_juego():
#     secreto = 77
#     while True:
#         try:
#             intentos_str = input("Ingresa el número de intentos que tendrás: ")
#             intentos = int(intentos_str)
#             if intentos <= 0:
#                 print("Debes tener al menos un intento.")
#             else:
#                 break
#         except ValueError:
#             print("¡Entrada inválida! Por favor, ingresa un número entero para los intentos.")
#     print("\n¡Comienza el juego!")
#     iniciotiempo = time.time()
#     global iniciales
#     iniciales = intentos
#     adivinar(secreto, intentos, iniciotiempo)
# if __name__ == "__main__":
#     iniciar_juego()
