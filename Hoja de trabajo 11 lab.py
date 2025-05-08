#Simulación de Experimentos de Caída Libre
class ExperimentoFisico:
    def realizar_experimento(self):
        raise NotImplementedError("Este método debe ser implementado por las subclases.")

class CaidaLibre(ExperimentoFisico):
    def __init__(self, altura, gravedad):
        if altura < 0:
            raise ValueError("La altura no puede ser negativa.")
        if gravedad == 0:
            raise ZeroDivisionError("La gravedad no puede ser cero.")
        self.altura = altura
        self.gravedad = gravedad

    def calcular_tiempo_caida(self):
        # Cálculo de la raíz cuadrada sin usar math.sqrt()
        tiempo_aproximado = (2 * self.altura / self.gravedad)**0.5
        return tiempo_aproximado

    def realizar_experimento(self):
        return self.calcular_tiempo_caida()
try:
    experimento1 = CaidaLibre(10, 9.8)
    tiempo = experimento1.realizar_experimento()
    print("Tiempo de caída: {:.2f} segundos".format(tiempo))

    experimento2 = CaidaLibre(-5, 9.8) # Esto lanzará una excepción
    tiempo = experimento2.realizar_experimento()
    print("Tiempo de caída: {:.2f} segundos".format(tiempo))

except ValueError as e:
    print("Error de valor:", e)
except ZeroDivisionError as e:
    print("Error de división por cero:", e)

