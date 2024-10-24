def insertion_sort(lista):
    n = len(lista)
    for i in range(1, n):
        for j in range(1, n):
            if lista[j] < lista[j-1]:
                lista[j], lista[j-1] = lista[j-1], lista[j]
            
    return lista

            
   
        
        
n
