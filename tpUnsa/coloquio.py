"""Módulo nro 5 - Coloquio
Pongamos en practica lo visto hasta ahora, resolvamos un ejercicio sencillo. Condiciones:

Resolverlo en 35 minutos
Subir el archivo Nombre_apellido.ipynb al profesor con el ejerció resuelto
EJERCICIO
El fichero cotizacion.csv () contiene las cotizaciones de las empresas del IBEX35 con las siguientes columnas: 
Nombre (nombre de la empresa), 
Final (precio de la acción al cierre de bolsa), 
Máximo (precio máximo de la acción durante la jornada), 
Mínimo (precio mínimo de la acción durante la jornada), 
Volumen (Volumen al cierre de bolsa), 
Efectivo (capitalización al cierre en miles de euros).

Construir una función que reciba el fichero cotizaciones y cree un 
fichero nuevo en formato csv con el mínimo, el máximo y el promedio de dada columna.

Ejemplo
Archivo de entrada (ejemplo):

Nombre	       Final	     Máximo	    Mínimo	    Volumen	    Efectivo
ACCIONA	95,95	96,75	94,4	84962	8166,11
ACERINOX	8668	8672	8468	88599	7633,81
ACS	37,28	37,66	37,22	655982	24517,29
AENA	167,1	167,5	166,1	133738	22336,1
 

Devolver un archivo cotizacion2.csv con los siguientes datos:

 

 	Mínimo	Máximo	Media
Final	37,28	8668	2242,0825
Mínimo	37,22	8468	2191,43
Máximo	37,66	8672	2243,3775
Volumen	84962	655982	240820,25
Efectivo	7633,81	24517,29	15663,3275"""

import csv


maximos = []
minimos = []
final=[]
volumen = []
efectivo = []
efectivo_float = []

with open("cotizacion.csv", "r", newline="\n") as csv_cotizacion:
    leer = csv.reader(csv_cotizacion, delimiter=";")


    for linea in leer:
        # print(linea)
        try:
            efectivo.append(linea[5])
            maximos.append(linea[2])
            minimos.append(linea[3])
            final.append(linea[1])
            volumen.append(linea[4])
        except:
            pass

def cambiar_caracter(arreglo):
    nuevo_arreglo=[]
    for valor in arreglo:
        try:
            x = valor.replace(",", ".")
            nuevo_arreglo.append(float(x))
        except ValueError:
            pass
    return nuevo_arreglo

nuevo_efectivo = cambiar_caracter(efectivo)
    

def maximo(arreglo):
    max_valor = None
    for num in arreglo:
        if (max_valor is None or num > max_valor):
            max_valor = num
    return max_valor

def minimo(arreglo):
    min_valor = None
    for num in arreglo:
        if (min_valor is None or num < min_valor):
            min_valor = num
    return min_valor
    


def promedio(arreglo):
    suma=0
    for valor in arreglo:
        suma = suma + valor
    promedio_arr = suma / len(arreglo)
    return promedio_arr

pro_max = cambiar_caracter(maximos)
pro_min = cambiar_caracter(minimos)
pro_final = cambiar_caracter(final)
pro_vol = cambiar_caracter(volumen)
pro_efe = cambiar_caracter(efectivo)


datos = [
  ("", "Minimo", "Maximo", "media"),	 
  ("Final", minimo(pro_final), maximo(pro_final), promedio(pro_final)),
  ("Minimo", minimo(pro_min), maximo(pro_min), promedio(pro_min)),
  ("Maximo", minimo(pro_max), maximo(pro_max), promedio(pro_max)),
  ("Volumen", minimo(pro_vol), maximo(pro_vol), promedio(pro_vol)),
  ("Efectivo", minimo(pro_efe), maximo(pro_efe), promedio(pro_efe)),
  ]

with open("cotizacion2.csv", "w", newline="\n") as csv_cotizacion2:
  csv2 = csv.writer(csv_cotizacion2, delimiter=",")
  for dato in datos:
      csv2.writerow(dato)

