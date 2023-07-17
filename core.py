import json
import os

def clear():
    os.system('clear')

def cicloTry(var):
    try:
        numero = int(var)
        return numero
    except Exception:
        print('Error... El valor ingresado no es numerico...')
        input('Press enter to continue...')

def leerArchivo(nombreArchivo):
    ciclo = True
    while ciclo:
        localizacionArchivo = f'data/{nombreArchivo}.json'
        try:
            with open(localizacionArchivo, 'r') as archivo:
                contenido = archivo.read()
            contenidoDiccionario = json.loads(contenido)
            ciclo = False
            return contenidoDiccionario
        except Exception:
            with open(localizacionArchivo, 'w') as archivo:
                archivo.write('{}')

def escribirArchivo(nombreArchivo, escritura):
    localizacionArchivo = f'data/{nombreArchivo}.json'
    try:
        with open(localizacionArchivo, 'w') as archivo:
            archivo.write(escritura)
    except Exception:
        print('Error... No se pudo escribir el archivo...')
        input('Press enter to continue...')


def convertirArchivo(diccionario):
    archivoJson =  json.dumps(diccionario, indent=4)
    return archivoJson
            
def menuPrincipal():
    clear()
    print('-'*10, '{:^43}'.format('CENTRO MEDICO 🏣 CAMPUS MD'), '-'*10)
    print('-'*10, '{:^44}'.format('MENU PRINCIPAL📜'), '-'*10)
    print('-'*66)
    print('\n1. Agregar Cita📋\n2. Buscar Cita🔎\n3. Modificar Cita📑\n4. Eliminar Cita❌\n\n5. Salir👋')
