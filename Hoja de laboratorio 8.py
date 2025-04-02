#Ejercicio 1
# n=int(input("Ingrese el tamaño del array: "))
# m=int(input("Ingrese el tamaño del multiplo: "))
# salida=[]
# for i in range(1,n+1):
#     salida.append(i*m)
# print(salida)

#Ejercicio 2
# nom=int(input("Ingrese la cantidad de nombres a escribir: "))
# nombres=[]
# cantidad=[]
# cont=nom
# while cont!=0:
#     nomb=str(input("Ingrese un nombre: "))
#     nombres.append(nomb)
#     cont=cont-1
#     cant=len(nomb)
#     cantidad.append(cant)
# print("Lista de nombres", nombres)
# print("cantidad de letras en cada nombre", cantidad)

#Escenario 1
cant=int(input("Ingrese la cantidad de clientes: "))
lista =[]
promedio=0
div=cant
uno, dos, tres, cuatro, cinco=0,0,0,0,0
suma=0
while cant!=0:
    nota=int(input("Ingrese la calificación: "))
    lista.append(nota)
    promedio=promedio+nota
    cant=cant-1
    if nota==1:
        uno=uno+1
    elif nota==2:
        dos=dos+1
    elif nota==3:
        tres=tres+1
    elif nota==4:
        cuatro=cuatro+1
    elif nota==5:
        cinco=cinco+1
print("calificaciones", lista)
print("Malo", uno)
print("Regular", dos)
print("Buena", tres)
print("Muy buena", cuatro)
print("Excelente", cinco)
p=promedio/div
print("Total promedio es igua  a: ", p)
print("El porcentaje menor al promedio es:", )
for numero in lista:
    if numero < p:
        suma+=numero
print((suma*100)/promedio, "%")
if uno>dos and uno>tres and uno>cuatro and uno>cinco:
    print("El más frecuente es:", uno)
elif dos>uno and dos>tres and dos>cuatro and dos>cinco:
    print("El más frecuene es:", dos)
elif tres>uno and tres>dos and tres>cuatro and tres>cinco:
    print("El más frecuene es:", tres)
elif cuatro>uno and cuatro>dos and cuatro>tres and cuatro>cinco:
    print("El más frecuene es:", cuatro)
elif cinco>uno and cinco>dos and cinco>tres and cinco>cuatro:
    print("El más frecuene es:", cinco)