#1.- Clinica veterinaria
# class Animal:
#     def __init__(self, nombre, edad, peso, dosis):
#         self.nombre=nombre
#         self.edad=edad
#         self.peso=peso
#         dosis=self.peso*0.05
#         self.dosis=dosis 
# class Perro(Animal):
#     def __init__(self, nombre, edad, peso, dosis, raza):
#         super().__init__(nombre, edad, peso, dosis)
#         self.raza=raza

# class Gato(Perro):
#     def __init__(self, nombre, edad, peso, dosis, raza, color):
#         super().__init__(nombre, edad, peso, dosis, raza)
#         self.color=color

# class Ave(Animal):
#     def __init__(self, nombre, edad, peso, dosis, habitat, origen):
#         super().__init__(nombre, edad, peso, dosis)
#         self.habitat=habitat
#         self.origen=origen

# class Reptil(Animal):
#     def __init__(self, nombre, edad, peso, dosis, tipo):
#         super().__init__(nombre, edad, peso, dosis)
#         self.tipo=tipo

# #Perro
# perro1=Perro("Max", 5, 60, 1, "Gran Dannes")
# perro2=Perro("Gordo", 9, 27, 1, "Chowchow")
# perro3=Perro("Scott", 12, 32, 1, "Labrador")
# print("Nombre del perro:", perro1.nombre, ", Edad del perro:" ,perro1.edad, ", Peso del perro en kg:", perro1.peso, ", Raza del perro:", perro1.raza, ", La dosis de ivermectina del perro es de: ", perro1.dosis)
# print("Nombre del perro:", perro2.nombre, ", Edad del perro:" ,perro2.edad, ", Peso del perro en kg:", perro2.peso, ", Raza del perro:", perro2.raza, ", La dosis de ivermectina del perro es de: ", perro2.dosis)
# print("Nombre del perro:", perro3.nombre, ", Edad del perro:" ,perro3.edad, ", Peso del perro en kg:", perro3.peso, ", Raza del perro:", perro3.raza, ", La dosis de ivermectina del perro es de: ", perro3.dosis)
# print()
# #Gato
# gato1=Gato("Aisha", 13, 5, 1, "Maine Coon", "Negro")
# gato2=Gato("Tom", 10, 4, 1, "Abisinio", "Gris")
# gato3=Gato("Kennyy", 2, 2.5, 1, "Gato Persa", "Amarillo")
# print("Nombre del gato:", gato1.nombre, ", Edad del gato:" , gato1.edad, ", Peso del gato en kg:", gato1.peso, ", Raza del gato:", gato1.raza, "Color del gato:", gato1.color ,",La dosis de ivermectina del gato es de: ", gato1.dosis)
# print("Nombre del gato:", gato2.nombre, ", Edad del gato:" , gato2.edad, ", Peso del gato en kg:", gato2.peso, ", Raza del gato:", gato2.raza, "Color del gato:", gato2.color ,",La dosis de ivermectina del gato es de: ", gato2.dosis)
# print("Nombre del gato:", gato3.nombre, ", Edad del gato:" , gato3.edad, ", Peso del gato en kg:", gato3.peso, ", Raza del gato:", gato3.raza, "Color del gato:", gato3.color ,",La dosis de ivermectina del gato es de: ", gato3.dosis)
# print()
# #Ave
# ave1=Ave("Flipo", 3, 0.04, 1, "Calido", "Brasil")
# ave2=Ave("Lunita", 2, 1.5, 1, "Calido", "Colombia")
# ave3=Ave("Flavio", 1, 0.4, 1, "Teemplado", "Mexico")
# print("Nombre de la ave:", ave1.nombre, ", Edad de la ave:" , ave1.edad, ", Peso de la ave en kg:", ave1.peso, "Habitat de la ave:", ave1.habitat, "Origen de la ave:", ave1.origen, ", La dosis de ivermectina del perro es de: ", ave1.dosis)
# print("Nombre de la ave:", ave2.nombre, ", Edad de la ave:" , ave2.edad, ", Peso de la ave en kg:", ave2.peso, "Habitat de la ave:", ave2.habitat, "Origen de la ave:", ave2.origen, ", La dosis de ivermectina del perro es de: ", ave2.dosis)
# print("Nombre de la ave:", ave3.nombre, ", Edad de la ave:" , ave3.edad, ", Peso de la ave en kg:", ave3.peso, "Habitat de la ave:", ave3.habitat, "Origen de la ave:", ave3.origen, ", La dosis de ivermectina del perro es de: ", ave3.dosis)
# print()
# #Reptil
# rep1=Reptil("Jaime", 7, 50, 1, "Lagarto")
# rep2=Reptil("Carlos", 25, 9, 1, "Serpiente")
# rep3=Reptil("Jasmmin", 19, 30, 1, "Tortuga")
# print("Nombre del reptil:", rep1.nombre, ", Edad del reptil:" , rep1.edad, ", Peso del reptil en kg:", rep1.peso, ", Tipo de reptil:", rep1.tipo, ", La dosis de ivermectina del perro es de: ", rep1.dosis)
# print("Nombre del reptil:", rep2.nombre, ", Edad del reptil:" , rep2.edad, ", Peso del reptil en kg:", rep2.peso, ", Tipo de reptil:", rep2.tipo, ", La dosis de ivermectina del perro es de: ", rep2.dosis)
# print("Nombre del reptil:", rep3.nombre, ", Edad del reptil:" , rep3.edad, ", Peso del reptil en kg:", rep3.peso, ", Tipo de reptil:", rep3.tipo, ", La dosis de ivermectina del perro es de: ", rep3.dosis)

#2.- Sistema de personas en una institución
class Persona:
    def __init__(self, nombre, edad, dni):
        self.nombre=nombre
        self.edad=edad
        self.dni=dni

class Estudiante(Persona):
    def __init__(self, nombre, edad, dni, carnet, carrera):
        super().__init__(nombre, edad, dni)
        self.carnet=carnet
        self.carrera=carrera

class Profesor(Persona):
    def __init__(self, nombre, edad, dni, codigo, curso):
        super().__init__(nombre, edad, dni)
        self.codigo=codigo
        self.curso=curso

class Administrativo(Persona):
    def __init__(self, nombre, edad, dni, id):
        super().__init__(nombre, edad, dni)
        self.id=id

#Estudiante
est1=Estudiante("Fernando", 19, 12345678, 20233015, "Ingeniería en sistemas")
print("Nombre del estudiante:", est1.nombre, ", Edad:", est1.edad, ", DNI:", est1.dni, ", Carnet:", est1.carnet, ", Carrera:", est1.carrera)

#Profesor
prof1=Profesor("Carlos", 25, 23456789, 1, "Precalculo")
print("Nombre del profesor", prof1.nombre, ", Edad:", prof1.edad, ", DNI:", prof1.dni, ", Codigo:", prof1.codigo, ", Curso:", prof1.curso)

#Admin
admin1=Administrativo("Miriam", 34, 34567890, 123)
print("Nombre del administrador:", admin1.nombre, ", Edad:", admin1.edad, ", DNI:", admin1.dni, ", ID:", admin1.id)
