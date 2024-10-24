def bubble_sort(lista):
    n = len(lista) - 1
    for i in range(n):
        trocou = False
        for j in range(n):
            if lista[j] > lista[j+1]:
                lista[j], lista[j+1] = lista[j+1], lista[j]
                print(lista)
                trocou = True
        if not trocou:
            return lista
    return lista

