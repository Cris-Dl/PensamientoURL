#programa que extraiga la primera y la última palabra de una oración. Split()
#print("Bienvenido al programa")
#print()
#v1=str(input("Escriba alguna oración: "))
#p1=v1.split()
#print("Su primera palabra es ", p1[0], "y su ultima palabra es ", p1[-1] )


#2.- Crea un programa que elimine los espacios repetidos en una cadena
#print("Bienvenido al programa")
#t1=str(input("Esriba alguna oración: "))
#t2=t1.split()
#print(t2)
#t3=" ".join(t1.split())
#print(t3)


#3.- Dado un correo electrónico, extrae solo el dominio.
#h1=str(input("Ingrese su gmail: "))
#dom=h1.split("@")[1]
#print("El dominio del correo es: ", dom)


#4.- Dado un nombre de archivo, verifica si tiene la extensión correcta (ej. .pdf).
#doc=str(input("Ingrese su documento: "))
#if doc.endswith((".pdf", ".png", "docx", "jpg")):
    #print("Su documento es valido")
#else:
    #print("Su documento es invalido")
    

#5.- Dado un texto, invierte el orden de las palabras
#k1=str(input("Ingrese alguna oración: "))
#k2=" ".join(k1.split()[::-1])
#print(k2)

#6.- Palabras claves
test=str(input("En que lo podemos ayudar: "))
text=test.lower()
poema1= "Poema de amor. Todos los que amo están en ti y túen todo lo que amo."
poema2= "Poema de tristeza. No duermes. No. No duermo. Nos estamos hablando en las estrellas.Somos aquí dos glorias reflejadas en la paz de la tierra."
cancion1= "Cancion de amor. En tus ojos veo mi sol,en tus manos siento mi paz, y en tu corazón quiero morar."
cancion2= "Cancion de risteza. El viento susurra mi dolor, las sombras se llevan mi luz, y el silencio grita lo que perdí."
if 'poema' in text and 'amor' in text:
    print(poema1)
elif 'poema' in text and 'tristeza' in text:
    print(poema2)
elif 'cancion' in text and 'tristeza' in text:
    print(cancion2)
elif 'cancion' in text and 'amor' in text:
    print(cancion1)