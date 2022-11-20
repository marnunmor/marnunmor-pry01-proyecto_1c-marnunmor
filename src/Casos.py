from collections import namedtuple

import csv
from parsers import *

#Definición de tupla con nombre
Caso_covid = namedtuple('Caso_covid', 'Numero_caso, Estado, Sexo, Edad, Fecha_de_Inicio_de_los_sintomas, Identificacion_de_COVID_19_por_RT_PCR, \
    Procedencia, Fecha_de_llegada_a_Mexico, Horas_ingresado,Recuperado_tras_14_días')


#--------------------------------------------------------------------------------------------------------------------------------------
#Entrega 1
#--------------------------------------------------------------------------------------------------------------------------------------
def lee_confirmados(nombre_fichero):
   
   """
   Función que crea una lista vacia con el nombre Confirmados, 
   especifica el tipo de cada dato de la tupla con nombre,
   lee el archivo csv y añade los datos correspondientes a la lista vacía.

   @param nombre_fichero: nombre y ruta del fichero a leer
   @type nombre_fichero: str
   @return: Devuelve una lista con los datos leidos
   @rtype: [Caso_covid(int, str, str, date, str, str, datetime.date, float, boolean)]
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

#--------------------------------------------------------------------------------------------------------------------------------------
#Entrega 2
#--------------------------------------------------------------------------------------------------------------------------------------

#--------------Bloque 1-------------------------------------------------

def filtra_por_estado(registros,estado="CIUDAD DE MEXICO"):
    """
    Función que deuleve una lista de tuplas de tipo Caso_covid 
    con los datos de los casos de un determinado estado, 
    de normal devuelve los casos de la Ciudad de Mexico
    @param registros: tupla con nombre de tipo Caso_covid
    @type registros:[Caso_covid(int, str, str, date, str, str, datetime.date, float, boolean)]
    @param estado:estado por el que se va a filtrar, si no se asigna valor toma el valor Ciudad de Mexico
    @type estado: str
    @return: devuelve una lista de tuplas del estado determinado 
    @rtype: [Caso_covid(int, str, str, date, str, str, datetime.date, float, boolean)]
    """

    res = []
    for a in registros:
        if a.Estado == estado :
            res.append(a)
    return res

def calcular_casos_total_hospital(registros,estado="CIUDAD DE MEXICO"):
    """
    Función que devuelve el numero de casos que ha habido 
    en un estado determinado que han estado ingresados en el hospital mas de 24 horas.
    De normal devuleve el numero de casos del estado Ciudad de Mexico
    @param registros: tupla con nombre de tipo Caso_covid
    @type registros:[Caso_covid(int, str, str, date, str, str, datetime.date, float, boolean)]
    @param estado:estado por el que se va a filtrar, si no se asigna valor toma el valor Ciudad de Mexico
    @type estado: str
    @return: devuelve una lista de tuplas del estado determinado
    @rtype: [Caso_covid(int, str, str, date, str, str, datetime.date, float, boolean)]
    """

    res=0
    for a in registros:
        if a.Estado==estado and a.Horas_ingresado > 24 :
            res=res+1
    return res

#--------------Bloque 2-------------------------------------------------

def obten_maximo_horas(registros,estado="CIUDAD DE MEXICO"):
   """
   Función que devuelve una lista de tuplas con los casos covid con el maximo
   numero de horas ingresado en el hospital de un determinado estado
   @param registros: tupla con nombre de tipo Caso_covid
   @type registros:[Caso_covid(int, str, str, date, str, str, datetime.date, float, boolean)]
   @param estado:estado por el que se va a filtrar, si no se asigna valor toma el valor Ciudad de Mexico
   @type estado: str
   @return: devuelve una lista de tuplas del estado determinado
   @rtype: [Caso_covid(int, str, str, date, str, str, datetime.date, float, boolean)]
   """
   lista=[]
   for a in registros:
        if a.Estado == estado:
            lista.append(a)
   res=[max(lista, key = lambda x:x.Horas_ingresado)]

   return res




def ordena_por_horas(registros,estado="CIUDAD DE MEXICO"):
    """
    Función que devuleve una lista de las tuplas de los casos de un determinado estado,
    ordenada de menor a mayor dependiendo de la cantidad de horas ingresado
    @param registros: tupla con nombre de tipo Caso_covid
    @type registros:[Caso_covid(int, str, str, date, str, str, datetime.date, float, boolean)]
    @param estado:estado por el que se va a filtrar, si no se asigna valor toma el valor Ciudad de Mexico
    @type estado: str
    @return: devuelve una lista de tuplas del estado determinado
    @rtype: [Caso_covid(int, str, str, date, str, str, datetime.date, float, boolean)]
    """
    res=[]
    for a in registros:
        if a.Estado==estado:
            res.append(a)
    return sorted(res, key=lambda x:x.Horas_ingresado)


def agrupar_por_estado(registros,Estados):
    """
    Función que devuelve un diccionario de cada estado con las horas del ingresado,
    del primer caso covid del estado correspondiente
    @param registros: tupla con nombre de tipo Caso_covid
    @type registros:[Caso_covid(int, str, str, date, str, str, datetime.date, float, boolean)]
    @param estados: lista con todos los eestados del dataset
    @type estados: [str,str,str,str,str,str,str,str,str,str,str,str,str,str,str,str,str,str,str,str,str,str,str,str,str,str,str,str]
    @retunr: diccionario con cada estad y las horas ingresadas en el hospital del primer caso covid del estado correspondiente
    @rtype: {str, float} 
    """
    res = dict()
    for a in registros:
        if a.Estado in Estados:
            res[a.Estado] = (a.Estado,a.Horas_ingresado)
    return res   