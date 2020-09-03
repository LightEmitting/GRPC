#Librerias
import os

# Escribo archivo PSconfig.txt
code = 'output ON\nset v 4.5'

# Elimino el archivo PSconfig.txt
os.remove() 

# Creo archivo
f = open('PSconfig.txt')

# Escribo archivo
f.write(' \n' + code + ' \n')

# Envio code a la fuente que corresponda
os.system("python3 DPS_Control.py PSconfig.txt --port /dev/ttyUSB0 --speed 9600")

# Actualizo Base de Datos