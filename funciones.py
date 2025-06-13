
def validar_lista_numeros():
    while True:
        lista = input("Ingrese una lista de números separados por espacio: ")
        datos = lista.split()
        try:
            numeros = []
            for elemento in datos:
                numeros.append(int(elemento))
            return numeros
        except ValueError:
            print("Error, debe ingresar solo números enteros")

def clasificar_pares_impares(numeros):
    pares = []
    impares = []
    for num in numeros:
        if num % 2 == 0:
            pares.append(num)
        else:
            impares.append(num)
    return pares,impares
