def laczenie(lista1: list, lista2: list) -> list:
    for number in lista2:
        if number not in lista1:
            lista1.append(number)
    nowaLista = []
    for number in lista1:
        nowaLista.append(number**3)
    return nowaLista


print(laczenie([1, 2, 3, 4, 5], [1, 2, 9, 4, 6]))
