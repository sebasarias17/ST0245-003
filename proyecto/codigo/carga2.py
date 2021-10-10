import urllib.request
from tkinter import filedialog
import os, sys
import requests
import json
import csv
import cv2

#llamar en caso de no tener los archivos .csv

def Enfermos():
    a = 0
    url =  requests.get('https://api.github.com/repos/mauriciotoro/ST0245-Eafit/contents/proyecto/datasets/imagenes/color/enfermo')
    convert = url.json()
    for i in convert:
        ruta_destino = os.path.join("./enfermos", i["name"])
        urllib.request.urlretrieve(i["download_url"], ruta_destino)
        a += 1

#llamar en caso de no tener los archivos .csv

def Sanos():
    b=0
    url =  requests.get('https://api.github.com/repos/mauriciotoro/ST0245-Eafit/contents/proyecto/datasets/imagenes/color/sano')
    convert = url.json()
    for i in convert:
        ruta_destino = os.path.join("./sanos", i["name"])
        urllib.request.urlretrieve(i["download_url"], ruta_destino)
        b += 1

def comprimir(archivos):
    contador = 0
    for line in archivos:
        if line.endswith('.webp'):
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
            

#Ingresar la direccion en donde se encunetran los archivos sanos en las comillas Ej."C:\Users\user\Documentos\Sano"
#path = "./sanas"
#archivos = os.listdir(path)
#
##Ingresar la direccion en donde se encuentran los archivos enfermos en las comilla Ej."C:\Users\user\Documentos\Enfermo"
#path = "./enfermos"
#archivos = os.listdir(path)
#
#list_Enfermos = []
#for files in archivos:
#    list_Enfermos.append(files)
#    
#list_Sano = []
#for files in archivos:
#    list_Sano.append(files)
#
#vaca1 = []
#dir = ".\enfermas"
#cont = os.listdir(dir)
#
#with open ("1.csv", "r") as csv_file:
#    csv_reader = csv.reader(csv_file)
#    for line in csv_file:
#        vaca = [item.strip() for item in line.split(',')]
#        vaca1.append(vaca)

path = "./"
archivos = os.listdir(path)



def __main__():
    comprimir(archivos)
__main__()