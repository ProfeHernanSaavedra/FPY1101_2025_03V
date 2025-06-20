conciertos=[
    {
        'ciudad' : 'Cairo',
        'publico': 30000,
        'canciones':['if your name is main',
                     'Break my heart and return',
                     'String float around you'
                     ]
    },
    {
        'ciudad' : 'Moscu',
        'publico': 25000,
        'canciones':['Break my heart and return',
                     'Open your mind, close your file',
                     'value Error'
                     ]
    },
    {
        'ciudad' : 'Berlin',
        'publico': 40000,
        'canciones':['if your name is main',
                     'value Error',
                     'Syntax of love'
                     ]
    }
]
# cancion 'Value Error'
#print(conciertos[2]['canciones'][2])

#ciudad = cairo
#print(conciertos[0]['ciudad'])

#cuántas personas escucharon una canción
def cuantos_escucharon(c):
    total = 0
    for dato in conciertos:
        if c in dato['canciones']:
            total = total + dato['publico']
    return total

#si dos canciones fueron tocadas en el mismo concierto(lista)
def mismo_concierto(c1,c2):
    for dato in conciertos:
        canciones = dato['canciones']
        if c1 in canciones and c2 in canciones:
            return True
    return False

print("CANCIONES DEL GRUPO")
print("*******************")
print("if your name is main\nBreak my heart and return\nString float around you\nOpen your mind, close your file\nvalue Error\nSyntax of love")
cancion = input("Ingrese una cancion: ").strip()
total = cuantos_escucharon(cancion)
print("El total de publico que escucho la cancion ",cancion," es: ",total)
print()
print("Ahora ingrese dos canciones, para saber si tocaron en el mismo concierto:")
cancion1 = input("Ingrese canción 1: ").strip()
cancion2 = input("Ingrese canción 2: ").strip()
esta = mismo_concierto(cancion1,cancion2)
if esta == True:
    print("Si fueron tocadas en el mismo concierto")
else:
    print("NO fueron tocadas en el mismo concierto")
