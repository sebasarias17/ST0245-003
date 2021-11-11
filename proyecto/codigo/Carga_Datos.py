import urllib.request
import os, sys
import requests
import json

#llamar en caso de no tener los archivos .csv

def Enfermos():
    url =  requests.get('https://api.github.com/repos/mauriciotoro/ST0245-Eafit/contents/proyecto/datasets/csv/enfermo_csv')
    convert = url.json()
    for i in convert:
        urllib.request.urlretrieve(i["download_url"],  i["name"])

#llamar en caso de no tener los archivos .csv

def Sanos():
    url =  requests.get('https://api.github.com/repos/mauriciotoro/ST0245-Eafit/contents/proyecto/datasets/csv/sano_csv')
    convert = url.json()
    for i in convert:
        urllib.request.urlretrieve(i["download_url"],  i["name"])


#Ingresar la direccion en donde se encunetran los archivos sanos en las comillas Ej."C:\Users\user\Documentos\Sano"
path_Sano = ""
archivos = os.listdir(path_Sano)

#Ingresar la direccion en donde se encuentran los archivos enfermos en las comilla Ej."C:\Users\user\Documentos\Enfermo"
path_Enfermo = ""
archivos = os.listdir(path_Enfermo)

list_Enfermos = []
for files in archivos:
    list_Enfermos.append(files)
    
list_Sano = []
for files in archivos:
    list_Sano.append(files)

def __main__():
    print(list_Enfermos)
    print("----------------------------------------------------------------------------------------------------------------")
    print("----------------------------------------------------------------------------------------------------------------")
    print("----------------------------------------------------------------------------------------------------------------")
    print(list_Sano)
__main__()
