from collections import namedtuple , Counter
import csv
from datetime import datetime
from parsers import *

from matplotlib import pyplot as plt


#Definición de tupla con nombre
Info = namedtuple('Info', 'Numero_caso, Estado, Sexo, Edad, Fecha_de_Inicio_de_los_sintomas, Identificacion_de_COVID_19_por_RT_PCR, \
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
   @rtype: [Info(int, str, str, date, str, str, datetime.date, float, boolean)]
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
            tupla = Info(numero_caso, estado, sexo, edad, fecha_inicio_sintomas,identificacion_covid, procedencia, llegada_a_mexico,horas_ingresado,recuperado_tras_14_dias)
            confirmados.append(tupla)
   return confirmados  

#--------------------------------------------------------------------------------------------------------------------------------------
#Entrega 2
#--------------------------------------------------------------------------------------------------------------------------------------

#--------------Bloque 1-------------------------------------------------

def filtra_por_estado(registros,estado="CIUDAD DE MEXICO"):
    """
    Función que deuleve una lista de tuplas de tipo Info
    con los datos de los casos de un determinado estado, 
    de normal devuelve los casos de la Ciudad de Mexico
    @param registros: tupla con nombre de tipo Info
    @type registros:[Info(int, str, str, date, str, str, datetime.date, float, boolean)]
    @param estado:estado por el que se va a filtrar, si no se asigna valor toma el valor Ciudad de Mexico
    @type estado: str
    @return: devuelve una lista de tuplas del estado determinado 
    @rtype: [Info(int, str, str, date, str, str, datetime.date, float, boolean)]
    """

    res = []
    for a in registros:
        if a.Estado == estado :
            res.append(a)
    return res

def filtra_por_genero(registros,genero="M",n=5):
    """
    Función que devuelve una lista de tuplas de tipo Info
    con los datos de los casos de un determinado genero y una cantidad determinada
    de casos, los devuelve ordenados de menor a mayor en función de las horas ingresado, 
    de normal devuelve los primeros 5 casos del genero Masculino
    @param registros: tupla con nombre de tipo Info
    @type registros:[Info(int, str, str, date, str, str, datetime.date, float, boolean)]
    @param genero: genero por el cual se va a filtrar las tuplas
    @type estado: str
    @return: devuelve una lista de tuplas del estado determinado 
    @rtype: [Info(int, str, str, date, str, str, datetime.date, float, boolean)]
    """
    res = [p for p in registros if p.Sexo==genero]
    resp = sorted(res, key = lambda x:x.Horas_ingresado)
    return resp[:n]

def calcular_casos_total_hospital(registros,estado="CIUDAD DE MEXICO",Tiempo = 24):
    """
    Función que devuelve la cantidad de casos que ha habido 
    en un estado determinado que han estado ingresados en el hospital mas del 
    numero de horas determinadas por la variable Tiempo, si no se especifica,
    la función filtra por los casos que hayan estado mas de un día ingresados.
    De normal devuelve la cantidad de casos del estado Ciudad de Mexico
    @param registros: tupla con nombre de tipo Info
    @type registros:[Info(int, str, str, date, str, str, datetime.date, float, boolean)]
    @param estado:estado por el que se va a filtrar, si no se asigna valor toma el valor Ciudad de Mexico
    @type estado: str
    @return: devuelve una lista de tuplas del estado determinado
    @rtype: [Info(int, str, str, date, str, str, datetime.date, float, boolean)]
    """

    res=[]
    for a in registros:
        if a.Estado==estado:
            if a.Horas_ingresado > Tiempo:
                res.append(a)
    return len(res)

#--------------Bloque 2-------------------------------------------------

def obten_maximo_horas(registros,estado="CIUDAD DE MEXICO"):
   """
   Función que devuelve una lista de tuplas con los casos covid con el maximo
   numero de horas ingresado en el hospital de un determinado estado
   @param registros: tupla con nombre de tipo Info
   @type registros:[Info(int, str, str, date, str, str, datetime.date, float, boolean)]
   @param estado:estado por el que se va a filtrar, si no se asigna valor toma el valor Ciudad de Mexico
   @type estado: str
   @return: devuelve una lista de tuplas del estado determinado
   @rtype: [Info(int, str, str, date, str, str, datetime.date, float, boolean)]
   """
   lista=[]
   for a in registros:
        if a.Estado == estado:
            lista.append(a)
   res=[max(lista, key = lambda x:x.Horas_ingresado)]
   return res




def filtra_n_registros_por_genero_y_estado_ordena_por_horas(registros,estado="CIUDAD DE MEXICO",genero = "M",n=4):
    """
    Función que devuleve una lista de las tuplas de los casos de un determinado estado,
    ordenada de menor a mayor dependiendo de la cantidad de horas ingresado
    @param registros: tupla con nombre de tipo Info
    @type registros:[Info(int, str, str, date, str, str, datetime.date, float, boolean)]
    @param estado:estado por el que se va a filtrar, si no se asigna valor toma el valor Ciudad de Mexico
    @type estado: str
    @return: devuelve una lista de tuplas del estado determinado
    @rtype: [Info(int, str, str, date, str, str, datetime.date, float, boolean)]
    """
    res=[p for p in registros if p.Estado==estado and p.Sexo==genero]
    return sorted(res[:n], key=lambda x:x.Horas_ingresado)


def agrupar_por_estado(registros,estados):
    """
    Función que devuelve un diccionario de cada estado con las horas del ingresado,
    del primer caso covid del estado correspondiente
    @param registros: tupla con nombre de tipo Info
    @type registros:[Info(int, str, str, date, str, str, datetime.date, float, boolean)]
    @param estados: lista con todos los eestados del dataset
    @type estados: [str,str,str,str,str,str,str,str,str,str,str,str,str,str,str,str,str,str,str,str,str,str,str,str,str,str,str,str]
    @retunr: diccionario con cada estad y las horas ingresadas en el hospital del primer caso covid del estado correspondiente
    @rtype: {str, float} 
    """
    res = dict()
    for a in registros:
        if a.Estado in estados:
            res[a.Estado] = (a.Estado,a.Horas_ingresado)
    return res   



#--------------------------------------------------------------------------------------------------------------------------------------
#Entrega 3
#--------------------------------------------------------------------------------------------------------------------------------------

#--------------Bloque 3-------------------------------------------------

def total_horas_en_el_hospital_de_los_estados_segun_genero(registros,genero="F"):
    """
    Funcion que devuelve un diccionario siendo las claves los estados, 
    y los valores la cantitad de horas que han estado ingresados los casos
    covid del genero indicado con anterioridad

    @param registros: tupla con nombre de tipo Info
    @type registros:[Info(int, str, str, date, str, str, datetime.date, float, boolean)]
    @param genero: genero por el cual se va a filtrar el diccionario
    @type genero: str
    @return:Devuelve un diccionario con las claves los estados y los valores la cantidad de horas ingresados de sus casos correspondientes
    @rtype: {str , float}
    """

    dicc={}
    for caso in registros:
        if caso.Sexo == genero:
            if caso.Estado in dicc:
                dicc[caso.Estado] += caso.Horas_ingresado
            else:
                dicc[caso.Estado] = caso.Horas_ingresado
    return dicc





def maximo_genero_repetido_en_un_estado(registros,estado="CIUDAD DE MEXICO"):
    """
    Funcion que devuelve un diccionario de un estado determinado, 
    el diccionario muestra el genero mas repetido en los casos del estado correspondiente
    y la cantidad de veces que se repite,
    si no se especifica devuelve los casos del estado de Ciudad de Mexico

    @param registros: tupla con nombre de tipo Info
    @type registros:[Info(int, str, str, date, str, str, datetime.date, float, boolean)]
    @param estado: estado por el cual se va a filtrar el diccionario
    @type estado: str
    @return: devuelve un diccionario con la condicion del estado y mostrando solo el genero y la cantida de repeticiones
    @rtype: {str , int}
    """
    lista = []
    for a in registros:
        if a.Estado == estado:
            lista.append(a.Sexo)
    contador = Counter(lista)
    return contador.most_common(1)

def maxima_edad_por_genero_estado(registro,estado = "CIUDAD DE MEXICO"):
    """
    Funcion que devuelve un diccionario de un estado determinado,
    siempre devuelve dos diccionarios, uno para cada genero, el diccionario
    muestra la maxima edad de cada sexo en el estado correspondiente,
    si no se especifica devuelve los casos del estado de Ciudad de Mexico

    @param registros: tupla con nombre de tipo Info
    @type registros:[Info(int, str, str, date, str, str, datetime.date, float, boolean)]
    @param estado: estado por el cual se filtra el diccionario
    @type estado: str
    @return: dos diccionarios con la edad maxima del genero correpondiente en el estado especificado
    @rtype: {str , int}
    """
    lista_genero_edad=[(t.Sexo,t.Edad) for t in registro if t.Estado == estado]
    lista_ordenada = sorted(lista_genero_edad, key = lambda x:x[1])
    return dict(lista_ordenada)


def top_n_estados_por_horas_ingresado(registro,n=3):
    """
    Función que devuelve un diccionario con los estados como claves, y una
    cantidad "n" de horas ingresado de los casos covid del estado correspondiente como valores,
    la cantidad de horas ingresado son los casos con la maxima cantidad de horas,
    si no se especifica devuelve los 3 casos con la maxima cantidad de horas

    @param registros: tupla con nombre de tipo Info
    @type registros:[Info(int, str, str, date, str, str, datetime.date, float, boolean)]
    @param n: cantidad de casos los cuales se quieren mostrar por consola
    @type n: int
    @return: diccionario con claves de cada estado, y valores de la cantida maxima de horas ingresado de los n casos
    @rtype: {str , float , float , float}
    """
    
    dicc = {}
    estados = {a.Estado  for a in registro}
    for e in estados:
        dicc[e]= sorted ([a.Horas_ingresado for a in registro if a.Estado == e] , reverse = True)[:n]
    return dicc

def aux_obten_estados_cantidad_casos_por_genero(registro,genero="F"):
    """
    Función que devuelve un diccionario de un genero determinado,
    esta funcion es una auxiliar para poder obtener las graficas,
    devuelve un diccionario de los estados y la cantidad de casos covid 
    que hay en dicho estado segun el genero determinado


    @param registros: tupla con nombre de tipo Info
    @type registros:[Info(int, str, str, date, str, str, datetime.date, float, boolean)]
    @param genero: genero por el cual se filtra el diccionario
    @type genero: str
    @return: diccionario con los estados como claves y la cantidad de casos del genero determinado como valores
    @rtype: {str , int}
    """
    dicc = {}
    lista = [a for a in registro if a.Sexo == genero]

    for t in lista:
        if t.Estado not in dicc:
            dicc[t.Estado] = 1
        else:
            dicc[t.Estado] +=1
    return dicc

def grafica_estados_mas_frecuentes_por_genero(registro,genero="F"):
    """
    Función que dibuja una grafica de barras basandose en la funcion auxiliar,
    la grafica muestra los estados y muestra la cantidad de casos 
    del genero especificado como los valores de las barras

    @param registros: tupla con nombre de tipo Info
    @type registros:[Info(int, str, str, date, str, str, datetime.date, float, boolean)]
    @param genero: genero por el cual se va a filtrar para mostrar la grafica
    @type genero: str
    @return: grafica con los estados y su cantidad de casos del genero determinado
    @rtype: grafica   
    """
    lista_estados = []
    lista_contador = []
    titulo = 'Estados con mas casos segun el genero determinado'
    for key, value in aux_obten_estados_cantidad_casos_por_genero(registro,genero).items():
        lista_estados.append(key)
        lista_contador.append(value)
    fig = plt.figure(titulo)
    ax = fig.add_subplot(111)
    n_x = range(len(lista_estados))
    ax.bar(n_x,lista_contador,width =0.6,align='center')
    ax.set_xticks(n_x)
    ax.set_xticklabels(lista_estados,rotation = 'vertical',fontsize = 7)
    plt.show()