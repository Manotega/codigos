def busca(lista, elemento):
    primeiro = 0
    ultimo = len(lista) - 1
    lista.sort()
    while primeiro <= ultimo:
        
        m = (ultimo + primeiro) // 2
        if elemento == lista[m]:
            print(m)
            return m
        elif elemento < lista[m]:
            ultimo = m - 1
            print(m)
        elif elemento > lista[m]:
            primeiro = m + 1
            print(m)
    return False

