
import sys

def cargar_datos():
    # Leer la entrada estándar
    entrada = sys.stdin.read().strip().split("\n")
    
    # Primera línea: número de casos de prueba
    num_casos = int(entrada[0])
    print(f"Cantidad de casos de prueba: {num_casos}\n")
    
    casos = []
    idx = 1  # Índice para recorrer las líneas de entrada

    for _ in range(num_casos):
        # Leer n y d
        n, d = map(int, entrada[idx].split())
        idx += 1
        
        print(f"Caso con n={n}, d={d}")
        
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


if __name__ == "__main__":
    casos = cargar_datos()
    for numCelulas,distancia,caso in casos:
        print(numCelulas)
        print(distancia)
        print(caso)
