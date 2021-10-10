import urllib.request
from tkinter import filedialog
import os, sys
import requests
import json
import csv
import cv2

#llamar en caso de no tener las imagenes
#crear una carpeta llamada enfermos para almacenar las imagenes del ganado enfermo

def Enfermos():
    a = 0
    url =  requests.get('https://api.github.com/repos/mauriciotoro/ST0245-Eafit/contents/proyecto/datasets/imagenes/color/enfermo')
    convert = url.json()
    for i in convert:
        ruta_destino = os.path.join("./enfermos", i["name"])
        urllib.request.urlretrieve(i["download_url"], ruta_destino)
        a += 1

#llamar en caso de no tener las imagenes
#crear una carpeta llamada sanos para almacenar las imagenes del ganado sano

def Sanos():
    b=0
    url =  requests.get('https://api.github.com/repos/mauriciotoro/ST0245-Eafit/contents/proyecto/datasets/imagenes/color/sano')
    convert = url.json()
    for i in convert:
        ruta_destino = os.path.join("./sanos", i["name"])
        urllib.request.urlretrieve(i["download_url"], ruta_destino)
        b += 1


#Crear una capeta llamada comprimidos_enfermos para almacenar las imagenes comprimidas del ganado
path = "./enfermos"
archivos = os.listdir(path)

def comprimir(archivos):
    contador = 0
    for line in archivos:
        print (line)
        if line.startswith('©'):
            contador+=1
        elif line.endswith('.webp'):
            contador+=1
        elif line.endswith('.gif'):
            contador+=1
        elif line.endswith('.py'):
            contador+=1
        else:
            print(line)
            print("else")
            img = cv2.imread(line)
            scale_percent = 0.50
            width = int(img.shape[1]*scale_percent)
            heigth = int(img.shape[0]*scale_percent)
            dimension=(width,heigth)

            resized=cv2.resize(img,dimension,interpolation=cv2.INTER_CUBIC)

            print(resized.shape)
            ruta_destino = os.path.join("./../comprimidos_enfermos", 'resized_'+line)
            cv2.imwrite(ruta_destino, resized)

            cv2.waitKey(0)
            cv2.destroyAllWindows()
    print("No se pudieron comprimir",contador,"Imagenes")
            





def __main__():
    comprimir(archivos)
__main__()

