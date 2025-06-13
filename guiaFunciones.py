import funciones as fn
#lista = input("Ingrese una lista de numeros separados por espacio: ").split()
#print(lista)


num = fn.validar_lista_numeros()
print(num)
pares, impares = fn.clasificar_pares_impares(num)
print("Números pares: ",pares)
print("Números impares: ",impares)