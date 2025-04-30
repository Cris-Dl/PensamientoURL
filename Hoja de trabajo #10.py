#1.- Clinica veterinaria
class Animal:
    def __init__(self, nombre, edad, peso, dosis):
        self.nombre=nombre
        self.edad=edad
        self.peso=peso
        dosis=self.peso*0.05
        self.dosis=dosis 
class Perro(Animal):
    def __init__(self, nombre, edad, peso, dosis, raza):
        super().__init__(nombre, edad, peso, dosis)
        self.raza=raza

class Gato(Perro):
    def __init__(self, nombre, edad, peso, dosis, raza, color):
        super().__init__(nombre, edad, peso, dosis, raza)
        self.color=color

class Ave(Animal):
    def __init__(self, nombre, edad, peso, dosis, habitat, origen):
        super().__init__(nombre, edad, peso, dosis)
        self.habitat=habitat
        self.origen=origen

class Reptil(Animal):
    def __init__(self, nombre, edad, peso, dosis, tipo):
        super().__init__(nombre, edad, peso, dosis)
        self.tipo=tipo

#Perro
perro1=Perro("Max", 5, 15, 1,"Gran Dannes")
print("Nombre del perro:", perro1.nombre, ", Edad del perro:" ,perro1.edad, ", Peso del perro:", perro1.peso, ", Raza del perro:", perro1.raza, ", La dosis del perro es de: ", perro1.dosis)

#Gato
#gato1=Gato("Aisha", 13, 2, "Angora", "Negro")
#print("Nombre del gato:", gato1.nombre, ", Edad del gato:", gato1.edad, ", Peso del gato:")
