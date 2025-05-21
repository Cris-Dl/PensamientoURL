matriz= [[0,0,0,0,0,0,0,1,1,0], [0,1,1,0,0,0,0,0,0,0], [0,1,0,0,0,0,0,0,0,0], [0,0,0,0,0,0,0,0,0,0], [0,0,0,0,0,0,0,0,0,0], [0,0,0,0,0,1,1,0,0,0], [0,0,0,0,0,1,1,0,0,0], [0,0,1,1,0,0,0,0,0,0],     [0,0,1,1,0,0,0,0,0,0],     [0,0,0,0,0,0,0,0,1,0] ]
def tablero(matriz):
    for i in matriz:
        print(i)
    print()

def contador (fila, columna, matriz):
    vecinos = 0
    filas = len(matriz)
    columnas = len(matriz[0])

    if columna -1 >= 0:
        vecinos += matriz[fila][columna - 1]
    if columna + 1 < columnas:
        vecinos += matriz[fila][columna+1]
    if fila - 1 >= 
