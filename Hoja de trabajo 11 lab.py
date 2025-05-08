#Simulación de Experimentos de Caída Libre
# class ExperimentoFisico:
#     def realizar_experimento(self):
#         raise NotImplementedError("Este método debe ser implementado por las subclases.")
# class CaidaLibre(ExperimentoFisico):
#     def __init__(self, altura, gravedad):
#         if altura < 0:
#             raise ValueError("La altura no puede ser negativa.")
#         if gravedad == 0:
#             raise ZeroDivisionError("La gravedad no puede ser cero.")
#         self.altura = altura
#         self.gravedad = gravedad
#     def calcular_tiempo_caida(self):
#         tiempo_aproximado = (2 * self.altura / self.gravedad)**0.5
#         return tiempo_aproximado
#     def realizar_experimento(self):
#         return self.calcular_tiempo_caida()
# try:
#     experimento1 = CaidaLibre(10, 9.8)
#     tiempo = experimento1.realizar_experimento()
#     print("Tiempo de caída: {:.2f} segundos".format(tiempo))

#     experimento2 = CaidaLibre(-5, 9.8)
#     tiempo = experimento2.realizar_experimento()
#     print("Tiempo de caída: {:.2f} segundos".format(tiempo))
# except ValueError as e:
#     print("Error de valor:", e)
# except ZeroDivisionError as e:
#     print("Error de división por cero:", e)

#Calculadora Científica Personalizada
class OperacionCientifica:
    def calcular(self): raise NotImplementedError()
class RaizCuadrada(OperacionCientifica):
    def __init__(self, n):
        self.n = n
    def calcular(self):
        if self.n < 0:
            return None
        return self.n**0.5
class Potencia(OperacionCientifica):
    def __init__(self, b, e): self.b, self.e = b, e
    def calcular(self): return self.b**self.e
class Logaritmo(OperacionCientifica):
    def __init__(self, n, b=10):
        self.n, self.b = n, b
    def calcular(self):
        def log_nat(x, p=100):
            if x <= 0: return None
            if x == 1: return 0.0
            s, t = 0.0, (x - 1) / (x + 1)
            tp = t
            for i in range(1, p + 1):
                s += tp / (2 * i - 1)
                tp *= t * t
            return 2 * s
        if self.n <= 0 or self.b <= 0 or self.b == 1:
            return None
        ln_n = log_nat(self.n)
        ln_b = log_nat(self.b)
        return ln_n / ln_b if ln_n is not None and ln_b is not None else None
class Factorial(OperacionCientifica):
    def __init__(self, n):
        self.n = n
    def calcular(self):
        if not isinstance(self.n, int) or self.n < 0:
            return None
        r = 1
        for i in range(1, self.n + 1): r *= i
        return r if self.n >= 0 else None
ops = [
    RaizCuadrada(25),
    Potencia(2, 3),
    Logaritmo(100, 10),
    Factorial(5),
    RaizCuadrada(-9),
    Logaritmo(0),
    Factorial(-3),
    Logaritmo(10, 0)
]
for op in ops:
    res = op.calcular()
    print("{}: {}".format(op.__class__.__name__, res))


