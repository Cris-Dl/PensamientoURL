print("Bienvenido al programa")
print()
num=int(input("Ingrese un número del 1 al 9: "))
resul=''
if num<1:
    print("Valor invalido, vuelva a intentar")
elif num<=3:
    resul=num*'I'
    print("El número" ,num, "en números romanos es:",resul,)
elif num==4:
    print("El número" ,num, "en números romanos es: IV")
elif num>=5 and num<=8:
    resul='V'+(num-5)*'I'
    print("El número" ,num, "en números romanos es:",resul,)
elif num==9:
    print("El número" ,num, "en números romanos es: IX")
else:
    print("Valor invalido, vuelva a intentar")
    
