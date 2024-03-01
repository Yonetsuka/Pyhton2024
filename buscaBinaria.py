def busca_binaria(array, x, low, high):
    while low <= high:
        mid = low + (high - low) // 2
        if array[mid] == x:
            return mid
        elif array[mid] < x:
            low = mid + 1
        else:
            high = mid - 1
    return -1


lista = [2,4,5,6,7,8,9,10,11]

alvo = int(input("Digite o numero q vc qr buscar da lista: "))

resultado = busca_binaria(lista,alvo,0,len(lista)-1)

if resultado != -1:
    print("Elemento encontrado no index " + str(resultado))
else:
    print("Elemento n foi encontrado")
