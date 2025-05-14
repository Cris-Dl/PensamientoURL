dias = ["Lunes", "Martes", "Miercoles", "Jueves", "Viernes"]

azucar = [130, 160, 95, 175, 160]
sal = [2000, 2400, 1800, 2400, 2700]
presion_sistolica = [115, 130, 110, 125, 175]
promedioazu = sum(azucar)/len(dias)
promediosal = sum(sal)/len(dias)
promediosisto = sum(presion_sistolica)/len(dias)
for i in range(5):
    if azucar[i]>=70 and azucar[i]<=140:
        print("En el dia", dias[i], "tiene un azucar normal")
    else:
        print("En el día", dias[i], "no es normal")
print("El promedio del azucar semanala es de:", promedioazu)
print()
for i in range(5):
    if sal[i] < 2300:
        print("En el día", dias[i], "la sal es normal")
    else:
        print("En el día", dias[i], "no es normal")
print("El promedio de la sal semanal es de:", promediosal)
print()
for i in range(5):
    if presion_sistolica[i] < 120:
        print("En el dia", dias[i], "tiene la presión normal")
    elif presion_sistolica[i] >= 120 and presion_sistolica[i] <= 129:
        print("En el día", dias[i], "tiene la presión elevada")
    elif presion_sistolica[i] >=130 and presion_sistolica[i] <= 139:
        print("En el dias", dias[i], "tuvo hipertensión etapa 1")
    elif presion_sistolica[i] >= 140:
        print("En el día", dias[i], "tuvo hipertensión etapa 2")
print("El promedio de la presión en la semanda es de:", promediosisto)