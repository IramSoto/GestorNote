# Imports
import os
import json
import argparse
from datetime import datetime
import shutil
#import rich

#Argumentos 
parser = argparse.ArgumentParser(description='Gestor de Notas')
parser.add_argument('accion', type=str, help='la Accion a ejecutar')
parser.add_argument('--nota', type=str, help='Nota a guardar')

args = parser.parse_args()

# Guardar una nota
def saveNote():
    if not args.nota.strip():
        print('La nota esta vacia y no se puede aceptar')
        return
    nuevaNota = {
		"Nota": args.nota,
		"Fecha": str(datetime.now())
	}
    jsonNuevaPersona = json.dumps(nuevaNota)
    with open('Archivos/notas.json', 'r') as archivo:
        notas = json.load(archivo)
    notas.append(jsonNuevaPersona)
    
    with open('Archivos/notas.json','w') as archivo:
        json.dump(notas, archivo, indent=4)
    print('Nota Guardada con Exito')
    
    
# Listar las Notas
def listNote():
    with open('Archivos/notas.json', 'r') as archivo:
        items = json.load(archivo)
    for item in items:
        print(item)
    print('Final de la Lista------------')
    
# Funcionalidad del programa    
if args.accion == 'ADD' and args.nota is not None:
    saveNote()
elif args.accion == 'GET':
    listNote()
else:
    print('La acción que se quiere realizar no existe.')