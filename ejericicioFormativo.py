import os

turistas = {    
    "001": ["John Doe", "Estados Unidos", "12-01-2024"],
    "002": ["Emily Smith", "Estados Unidos", "23-03-2024"],
    "012": ["Julian Martinez", "Argentina", "19-09-2023"],
    "014": ["Agustin Morales", "Argentina", "28-03-2024"],
    "005": ["Carlos Garcia", "Mexico", "10-05-2024"],
    "006": ["Maria Lopez", "Mexico", "08-12-2023"],
    "007": ["Joao Silva", "Brasil", "20-06-2024"],
	"003": ["Michael Brown", "Estados Unidos", "05-07-2023"],
	"004": ["Jessica Davis", "Estados Unidos", "15-11-2024"],
    "008": ["Ana Santos", "Brasil", "03-10-2023"],
    "010": ["Martin Fernandez", "Argentina", "13-02-2023"],
    "011": ["Sofia Gomez", "Argentina", "07-04-2024"],
     }

#print(turistas["001"][2])
#for codigo,datos in turistas.items():
#    print(datos[0])

def turista_por_pais(pais):
    #mostrar por pantalla una lista con los nombres de los turistas que pertenecen a ese pais
    nomTuristas = []
    for datos in turistas.values():
        if datos[1].lower() == pais.lower():
            nomTuristas.append(datos[0])
    
    if nomTuristas:
        print(f"Turistas del país {pais}: ")
        for nombre in nomTuristas:
            print(nombre)
    else:
        print("NO se encontraron turistas de ese país")

def turistas_por_mes(mes):

    total = len(turistas)
    contar = 0

    for datos in turistas.values():
        fecha = datos[2]
        fecha_mes = int(fecha.split("-")[1])
        if fecha_mes == mes:
            contar = contar + 1
    
    porcen = (contar / total )* 100
    return round(porcen,1)


def eliminar_turista():
    for codigo,datos in turistas.items():
        print(codigo,datos[0]) 

    nombreTurista = input("Ingrese el nombre del turista a eliminar: ").lower().strip()
    codigoEliminar = None

    for codigo,datos in turistas.items():
        if datos[0].lower() == nombreTurista:
            codigoEliminar = codigo
            break
    if codigoEliminar:
        del turistas[codigo]
        print("Turista eliminado")
        for codigo,datos in turistas.items():
            print(codigo,datos[0]) 
    else:
        print("No se encontró el turista")

  
while True:
     
    print("MENU PRINCIPAL")
    print("1. Turista por pais")
    print("2. Turista por mes")
    print("3. Eliminar Turista")
    print("4. Salir")

    opcion = int(input("Ingrese opción: "))
    os.system("cls")
    if opcion == 1:
        pais = input("Ingrese el país: ")
        turista_por_pais(pais)
    elif opcion == 2:
        while True:
            try:
                mes = int(input("Ingrese el mes (1-12): "))
                if mes >= 1 and mes <= 12:
                    porcentaje = turistas_por_mes(mes)
                    print(f"Porcentaje de turistas en el Chile el mes {mes} fue de {porcentaje}%")
                    break
                else:
                    print("Debe ingresar un número entre 1 y 12")
            except ValueError:
                print("Debe ingresar un número")
    elif opcion == 3:
        eliminar_turista()
    elif opcion == 4:
        print("Saliendo....")
        break
    else:
        print("Opción no válida")