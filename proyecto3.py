from math import sqrt
import sys

def cargar_datos():
    # Leer la entrada estándar
    entrada = sys.stdin.read().strip().split("\n")
    
    # Primera línea: número de casos de prueba
    num_casos = int(entrada[0])
    
    
    casos = []
    idx = 1  # Índice para recorrer las líneas de entrada

    for _ in range(num_casos):
        # Leer n y d
        n, d = map(int, entrada[idx].split())
        idx += 1
        
        
        
        celulas = []
        for _ in range(n):
            # Leer los datos de una célula
            linea = entrada[idx].split()
            idx += 1
            id_celula = int(linea[0])
            x = int(linea[1])
            y = int(linea[2])
            peptidos = linea[3:]
            
            # Añadir a la lista de células
            celulas.append((id_celula, x, y, peptidos))
        
        casos.append((n, d, celulas))
        
        # Imprimir la información cargada
        
    
    return casos

def calcularDistancia(celula1, celula2):
    # Calcula la distancia entre celulas basadas en las coordenadas
    return sqrt((celula1[1] - celula2[1]) ** 2 + (celula1[2] - celula2[2]) ** 2)

def buscarCoincidencias(celula1, celula2):
    peptidos1 = celula1[3]
    peptidos2 = celula2[3]
    

    coincidencias = [elemento for elemento in peptidos1 if elemento in peptidos2]
    return len(coincidencias)


    
def pares(numcCelulas, distancia, caso):
    memo = []
    for celula in caso:
        for celula2 in caso:
            # d almacena la distancia entre las 2 celulas
            d = calcularDistancia(celula, celula2)
            # se comprueba que no se opera en la misma celula y la distancia calculada (d) es menor
            if celula != celula2 and d <= distancia:
                # se calcula la cantidad de coincidencias entre las 2 celulas
                print(buscarCoincidencias(celula, celula2))
                print(celula[0], celula2[0])
                


if __name__ == "__main__":
    casos = cargar_datos()
    for numCelulas,distancia,caso in casos:
        print('numero de celulas: ', numCelulas)
        print('distancia: ',distancia)
        pares(numCelulas,distancia,caso)  # Llamar a la función
