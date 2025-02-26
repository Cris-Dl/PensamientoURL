print("Bienvenido al programa")
print()
v1=int(input("Ingrese un número de 5 dígitos: "))#56435
n1=0
n2=0
n3=0
n4=0
n5=0
n6=0
n7=0
n8=0
if v1>=10000 and v1<=99999:
    n1=v1%10000 #6435
    n2=n1%1000 #
    n3=n2%100
    n4=n3%10 #Ultimo digito
    n5=v1//10000 #Primer digito
    n6=n1//1000 #Segundo digito
    n7=n2//100 #Tercer digito
    n8=n3//10 #Cuarto digito
    if n5>=n6 and n6>=n7 and n7>=n8 and n8>=n4:
        print(n5,n6,n7,n8,n4)
    elif n5>=n4 and n7>=n6 and n4>=n6 and n8>=n6:
        print(n5,n7,n4,n8,n6)
    elif n4>=n5 and n6>=n7 and n5>=n7 and n7>=n8:
        print(n4,n6,n5,n7,n8)
    elif n5>=n4 and n7>=n6 and n4>=n6 and n6>=n8:
        print(n5,n7,n4,n6,n8)
    elif n4>=n5 and n6>=n7 and n7>=n5 and n5>=n8:
        print(n4,n6,n7,n5,n8)
    elif n4>=n5 and n6>=n7 and n7>=n5 and n8>=n5:
        print(n4,n6,n7,n8,n5)    
    elif n4>=n5 and n5>=n6 and n6>=n7 and n7>=n8:
        print(n4,n5,n6,n7,n8)
    elif n5>=n6 and n6>=n7 and n7>=n8 and n8>=n4:
        print(n5,n6,n7,n8,n4)
    elif n5>n6 and n6>=n7 and n4>n7 and n4>n8 and n7>=n8:
        print(n5,n6,n4,n7,n8)
    print()
    if n5<=n6 and n6<=n7 and n7<=n8 and n8<=n4:
        print(n4,n8,n7,n6,n5)
    elif n5<=n4 and n7<=n6 and n4<=n6 and n8<=n6:
        print(n6,n8,n4,n7,n5)
    elif n4<=n5 and n6<=n7 and n5<=n7 and n7<=n8:
        print(n8,n7,n5,n6,n4)
    elif n5<=n4 and n7<=n6 and n4<=n6 and n6<=n8:
        print(n8,n6,n4,n7,n5)
    elif n4<=n5 and n6<n7 and n7<=n5 and n5<=n8:
        print(n8,n5,n7,n6,n4)
    elif n4<=n5 and n6<=n7 and n7<=n5 and n8<=n5:
        print(n5,n8,n7,n6,n4)    
    elif n4<=n5 and n5<=n6 and n6<=n7 and n7<=n8:
        print(n8,n7,n6,n5,n4)
    elif n5<=n6 and n6<=n7 and n7<=n8 and n8<=n4:
        print(n4,n8,n7,n6,n5)
    elif n5<n6 and n6<=n7 and n4<n7 and n4<n8 and n7<=n8:
        print(n8,n7,n4,n6,n5)
        print(n7,n8,n4,n6,n5)
