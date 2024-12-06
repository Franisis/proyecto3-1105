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
    allpairs= [] 
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
    return allpairs


def createPairs(distancia, caso,allPairs):
    memo = set({})
    comparativeGroup=set({})
    groups=[]
    for pair in allPairs:
        cell = list(pair.keys())[0]
        nextCell=pair[cell]['siguiente']
        
        #crear primer par
        if cell not in memo and nextCell not in memo and len(memo)==0:
            memo.add(cell)
            memo.add(nextCell)
            groups.append([cell,nextCell])
        elif cell not in memo  and len(memo)>0:
            """
            primero necesitamos ver si hay camino entre los pares dentro de pairs
            de lo contrario creamos un nuevo par con nextCell [cell, nextCell], pero si nextCell ya está en memo se añade el cell solo como [cell]
            """
            
            for group in groups:
                if cell not in group:
                    spmm=sepuedenMandarmensajes(group, cell, caso, distancia)
                    if  spmm and cell not in memo:
                        #verifica que se puedan mandar mensajes en el grupo
                        group.append(cell)
                        memo.add(cell)
                    elif cell not in memo and nextCell not in memo:
                        groups.append([cell])
                        memo.add(cell)
                    
                    
    
    return groups, memo
    
    #funcion que me permite encontrar 1 celula dentro del caso dado su id
def buscarCelula(caso, id):
    return [celula for celula in caso if celula[0]==id ][0]

def buscarCelulaEnAllPairs(allpairs,id, idnext):
    return [pair for pair in allpairs if list(pair.keys())[0]==id and pair[list(pair.keys())[0]]['siguiente'] ==idnext ]

def coincidenciasMaximasGrupo(group, allpairs,caso):
    
    coincidencias=set({})
    for cell in group:
        cellInfo=buscarCelula(caso,cell)
        peptides= cellInfo[3]
        if len(coincidencias)==0:
            for peptide in peptides:
                coincidencias.add(peptide)
        else:
            coincidencias = coincidencias & set(peptides)
            
    return coincidencias
        

def sepuedenMandarmensajes(group, cell,caso,distancia):
    """
    se pasa un grupo consolidado por parametro y una celula a comprobar
    se retorna cuantas celulas del grupo coinciden con la celula a comprobar
    """
    #el determinante nos ayuda a mirar si se puede enviar mensajes entre celulas
    determinante=0
    completeCell = buscarCelula(caso,cell)

    if len(group)==1:
        celulaCompleta=buscarCelula(caso,group[0])

        celulaCompletaConjunto = set(celulaCompleta[3])
        completeCellConjunto = set(completeCell[3])
        d=calcularDistancia(completeCell, celulaCompleta)
        
        if len(celulaCompletaConjunto.intersection(completeCellConjunto))>0 and d<=distancia :
            #se suma +1 debido a que 
            
            determinante+=1

    else:
        """
        primero necesitamos encontrar las coincidencias que hay en el grupo, es decir
        si comparten una cierta cantidad de peptidos una vez compartan cierta cantidad 
        toca revisar si la celula que estamos comparando tiene la misma cantidad de celulas que la pareja original.
        """

        #coincidencias dentro del grupo es un set 
        coincidenciasGrupo = coincidenciasMaximasGrupo(group, allpairs,caso)
        
        for celula in group:
            celulaCompleta=buscarCelula(caso,celula)
            #Se hacen conjuntos con la celula completa y complete cell y comprobar
            celulaCompletaConjunto = set(celulaCompleta[3])
            completeCellConjunto = set(completeCell[3])
            d=calcularDistancia(completeCell, celulaCompleta)
            
            if len(celulaCompletaConjunto.intersection(completeCellConjunto))>=len(coincidenciasGrupo) and d<=distancia :
                #se suma +1 debido a que      
                determinante+=1
    if determinante==len(group):
        return True
    else:
        return False
     
def findGroupNumber(pairs, id):
    #se busca la celula por la id y se retorna al grupo al que pertenece
    for pair in pairs:
        if id in pair:
            return id, pairs.index(pair)
        
if __name__ == "__main__":
    casos = cargar_datos()
    for numCelulas,distancia,caso in casos:
        allpairs=pares(numCelulas,distancia,caso)  # Llamar a la función
        pairs,memo=createPairs(distancia,caso,allpairs)
        for id in memo:
            id,groupid=findGroupNumber(pairs,id)
            print(f'{id} {groupid+1}')
