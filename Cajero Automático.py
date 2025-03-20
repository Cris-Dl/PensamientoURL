#Cajero Automático
Cantidad=3000
intentos=3
while Cantidad>0 and intentos>0:
    Retiro=int(input("Ingrese el monto a retirar o seleccione 0 si desea cancelar: "))
    if(Retiro==0):
        break
    while(Retiro>Cantidad) or Retiro<0:
        print("El retiro no es valido")
        intentos=intentos-1
        if(intentos==0):break
        print("Le quedan ",intentos," intentos")
        Retiro=int(input("Ingrese el monto a retirar o seleccione 0 si desea cancelar: "))
    if(Retiro==0):
        break
    Cantidad=Cantidad-Retiro
    if(Cantidad>0):
        print("Su saldo actual es de: ",Cantidad)
print("Adios")