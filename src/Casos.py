from collections import namedtuple

import csv
from parsers import *

#Definición de tupla con nombre
Caso_covid = namedtuple('Caso_covid', 'Numero_caso, Estado, Sexo, Edad, Fecha_de_Inicio_de_los_sintomas, Identificacion_de_COVID_19_por_RT_PCR, \
    Procedencia, Fecha_de_llegada_a_Mexico, Horas_ingresado,Recuperado_tras_14_días')


def lee_confirmados(nombre_fichero):
   
   """
   Función que crea una lista vacia con el nombre Confirmados, 
   especifica el tipo de cada dato de la tupla con nombre,
   lee el archivo csv y añade los datos correspondientes a la lista vacía.

   @param nombre_fichero: nombre y ruta del fichero a leer
   @type nombre_fichero: str
   @return: Devuelve una lista con los datos leidos
   @rtype: [int, str, str, date, str, str, date, float, boolean]
   """
   confirmados = []
   with open(nombre_fichero, encoding='utf-8') as f:
        lector = csv.reader(f)
        next(lector)
        for numero_caso, estado,sexo, edad, fecha_inicio_sintomas, identificacion_covid,procedencia, llegada_a_mexico,horas_ingresado,recuperado_tras_14_dias in lector:
            numero_caso = int(numero_caso)
            edad = int(edad)
            fecha_inicio_sintomas = parse_date(fecha_inicio_sintomas)
            horas_ingresado = float (horas_ingresado)
            recuperado_tras_14_dias = parse_bool(recuperado_tras_14_dias)
            llegada_a_mexico = parse_date(llegada_a_mexico)       
            tupla = Caso_covid(numero_caso, estado, sexo, edad, fecha_inicio_sintomas,identificacion_covid, procedencia, llegada_a_mexico,horas_ingresado,recuperado_tras_14_dias)
            confirmados.append(tupla)
   return confirmados  