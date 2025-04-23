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
def suma_hasta(n):
    if n<0:
        print("El número debe sey mayor a 0")
    else:
        suma=n*(n+1)//2
        print("La suma es:", suma)
suma_hasta(8)