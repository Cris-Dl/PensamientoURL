#Cristhian de León - 1540225
#1.- Consumo de agua
#water=int(input("Ingrese el consumo de agua: "))
#people=int(input("Ingrese la cantida de personas: "))
#if water>=0 and water<15:
    #print("La tarifa es de: Q", water*5 )
#elif water>=15 and water<=30 and people>=0:
    #if people>3:
        #print("La tarifa es de: Q", water*4)
    #elif people==3:
        #print("La tarifa es de: Q", water*4.5)
    #else:
        #print("La tarifa es de: Q", water*5)
#elif water>30 and people>=0:
    #if people>5:
        #print("La tarifa es de: Q", water*3.5)
    #elif people%2==0:
        #print("La tarifa es de: Q", water*4)
    #else:
        #print("La tarifa es de: Q", water*4.2)
#else:
    #print("Error al ingresar los datos, vuelva a intentar")
    

#2.- Regular tráfico
#year=int(input("Ingrese el año del vehiculo: "))
#placa=int(input("Ingrese el número de placa: "))
#un=placa%10
#if year>=2001 and year<=2025:
    #if un==0 or un==2 or un==4 or un==6 or un==8:
        #print("El vehiculo no circula los lunes")
    #elif un==1 or un==3 or un==5 or un==7 or un==9:
        #print("El vehiculo no circula los viernes")
    #elif year%2==0:
        #print("El vehiculo no circula despues del medio dia")
#elif year<2001 and year>=1903:
    #print("Advertencia, el vehiculo necesita mantenimiento obligatorio")
#else:
    #print("Error al ingresar los datos, vuelva a intentar")
