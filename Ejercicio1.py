import os
# Clasificacion de estudiantes de acuerdo a puntaje
list_categoria1 = []# Puntaje (30 - 50) y edad (15 -  20)
list_categoria2 = []# Puntaje (51 80) y edad  (21 - 30)
list_categoria3 = []# Puntaje (81 - 100 ) y edad (31 - 50)
sw = True

def fnt_limpiar():
    os.system('cls')
    print('\nBienvenido al sistema de calificacion de estudiantes')
    print('Autor: Michell Alejandra Mosquera Pacheco')
    print('Instalacion: Universidad Catolica Luis Amigó')
    print('Categoria I: ',list_categoria1)
    print('Categoria II: ',list_categoria2)
    print('Categoria III: ',list_categoria3)


def fnt_registrar (Id, Nombre, Puntaje, Edad):
    if Id == '' or Puntaje == '' or Edad == '' or Nombre == '':
        enter = input('\nDebe ingresar todos los datos <ENTER>')
    else:
        if Id in list_categoria1 or list_categoria2 or list_categoria3:#Si ese Id se encuentra ya registrado
                enter = input('\nEsta persona ya se encuentra categorizada <ENTER>')
        else:
            axuP = int(Puntaje) #Convierte el dato en entero
            AuxE = int(Edad) #Convierte el dato en entero
            if (axuP >= 30 and axuP <= 50) and (AuxE >= 15 and AuxE <= 20):
                list_categoria1.append([Id,Nombre,AuxE,Puntaje])
            elif (axuP >= 51 and axuP <= 80) and (AuxE >= 15 and AuxE <= 30):
                list_categoria1.append([Id,Nombre,Edad,Puntaje])
            elif (axuP >= 81 and axuP <= 100) and (AuxE >= 31 and AuxE <= 50):
                    list_categoria1.append([Id,Nombre,Edad,Puntaje])
            enter = input(f'\nEstudiante {Nombre} ha sido registrado con éxito')          
def fnt_selector(op):
    fnt_limpiar()
    if op == '1':
        IdStr = input('Id: ')
        NombreStr = input('Nombres completos: ')
        EdadStr = input('Edad: ')
        PuntajeStr = input('Puntaje: ')
        fnt_registrar(IdStr,NombreStr,EdadStr,PuntajeStr)
            
while sw == True:
    fnt_limpiar()
    opcionesStr = input('\n\n --- MENU PRINCIPAL ---\n\n1. REGISTRAR\n2. CONSULTAR\n3. SALIR\n. -> ')
    fnt_selector(opcionesStr)



