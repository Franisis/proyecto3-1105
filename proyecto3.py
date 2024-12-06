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

    
def pares(numCelulas, distancia, caso):
    memo = []
    allpairs= [] 
    pairs=[]
    #lista de tuplas que muestra los grupos a 
    #los que pertenencen las celulas segun el indice
    for celula in caso:
        for celula2 in caso:
            # d almacena la distancia entre las 2 celulas
            d = calcularDistancia(celula, celula2)
            # se comprueba que no se opera en la misma celula y la distancia calculada (d) es menor
            numerodeMensajes=(buscarCoincidencias(celula, celula2))
            if celula != celula2 and d <= distancia and numerodeMensajes>0:
                # se calcula la cantidad de coincidencias entre las 2 celulas
                
                # numero de mensajes me cuenta masomenos el peso del arco entre las 2 celulas
                allpairs.append(
                    {
                        celula[0]: 
                        {
                        "siguiente": celula2[0],
                        "distancia": round(d,3),
                        "mensajes": numerodeMensajes,
                        'shared' : list(
                            set(celula[3]) & set(celula2[3])
                            )}
                    }
                    
                )
    
        
        realPairs=[]
        for pair in allpairs:
            cell = list(pair.keys())[0]
            nextCell = pair[cell]['siguiente']
            if len(realPairs)==0:
                realPairs.append([cell,nextCell])
            else:
                for rPair in realPairs:
                    if cell not in rPair:
                        """
                        buscar dentro del caso celulas la celula completa
                        """
                        celulaCompleta = buscarCelulaCompleta(cell, caso)
                        peptidos=celulaCompleta[3]
                        areFriends=0
                        for r in rPair:
                            celulaCompletaPar = buscarCelulaCompleta(r, caso)
                            numCoincidencias=buscarCoincidencias(celulaCompleta, celulaCompletaPar)
                            if numCoincidencias>0:
                                print(celulaCompleta, "es amigo de: ", celulaCompletaPar)
                                areFriends+=1
                        if areFriends==len(rPair):
                            rPair.append(cell)
                        else:
                            realPairs.append([cell])
    print(realPairs)
def buscarCelulaCompleta(idCelula, caso):
    return [celula for celula in caso if celula[0]==idCelula][0]
                
        
    
    
        

def getCellfromAllPairs():
    pass
            

                
                


if __name__ == "__main__":
    casos = cargar_datos()
    for numCelulas,distancia,caso in casos:
        print('numero de celulas: ', numCelulas)
        print('distancia: ',distancia)
        pares(numCelulas,distancia,caso)  # Llamar a la función
