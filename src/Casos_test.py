from  Casos import *
from parsers import *

def mostrar_diccionario(dicc):
    """
    Función que permite mostrar por consola los elementos de un diccionario,
    @param dicc: el diccionario que se quiere mostrar
    @type dicc: {clave , valor}
    """
    for clave, valor in dicc.items():
        print(f"{clave}-->{valor}") 

def mostrar_iterable(iterable):
    '''Función que permite mostrar por consola todos los elementos de un iterable.
    Cada elemento se muestra en una lista distinta

    @param iterable: Cualquier variable que se puede recorrer con un for
    @type iterable: Iterable
    '''
    for elemento in iterable:
        print(elemento)

def test_lee_confirmados (nombre_fichero):
    '''
    Función que prueba la lectura de ficheros.
    Muestra por consola el número de autobuses leidos y
    un listado de los autobuses, mostrando uno por linea

    @param nombre_fichero: Nombre y ruta del fichero a leer
    @type nombre_fichero: str
    '''
    confirmados = lee_confirmados(nombre_fichero)
    print(f"Se han leido {len(confirmados)} casos covid y son:")
    print("="*150)
    mostrar_iterable(confirmados)

#--------------------------------------------------------------------------------------------------------------------------------------
#Entrega 2
#--------------------------------------------------------------------------------------------------------------------------------------

def test_filtra_por_estado(registros,estado="CIUDAD DE MEXICO"):
    """
    Función que prueba el filtrado por estado
    y muestra por pantalla una lista de tuplas de los casos covid
    solo de los que son del estado determinado
    @param registros: tupla con nombre de tipo Caso_covid
    @type registros:[Caso_covid(int, str, str, date, str, str, datetime.date, float, boolean)]
    @param estado:estado por el que se va a filtrar, si no se asigna valor toma el valor Ciudad de Mexico
    @type estado: str
    
    """
    print("="*150)
    print(f"Estado = {estado}")
    res = filtra_por_estado(registros,estado)
    print(f"Se han leido {len(res)} casos covid del estado dado como parametro y los casos son:")
    print("="*150)
    mostrar_iterable(res)

def test_filtra_por_genero(registros,genero="M",n=5):
    """
    Función que prueba el filtrado por genero
    y muestra por pantalla una lista de tuplas de los casos covid
    solo de los que son del genero determinado, la cantidad de casos determinados
    y ordenados de menor a mayor en funcion de las horas ingresado
    @param registros: tupla con nombre de tipo Caso_covid
    @type registros:[Caso_covid(int, str, str, date, str, str, datetime.date, float, boolean)]
    @param genero: sexo por el que se va a filtrar las tuplas
    @type genero: str
    @param n: numero de tuplas que se quieren mostrar
    @type n: int
    
    """
    if genero=="M":
        g="Masculino"
    else: g="Femenino"

    print("="*150)
    print(f"Genero = {g}")
    res = filtra_por_genero(registros,genero,n)
    print(f"Los {n} casos covid del genero dado como parametro con el minimo de horas son:")
    print("="*150)
    mostrar_iterable(res)    
    


def test_calcular_casos_total_hospital(registros,estado="CIUDAD DE MEXICO",Tiempo=24):
    """
    Función que prueba el calculo de los casos totales de los hospitales,
    muetra por pantalla la cantidad de casos covid que ha tenido un determinado estado

    @param registros: tupla con nombre de tipo Caso_covid
    @type registros:[Caso_covid(int, str, str, date, str, str, datetime.date, float, boolean)]
    @param estado:estado por el que se va a filtrar, si no se asigna valor toma el valor Ciudad de Mexico
    @type estado: str    
    """
    res=calcular_casos_total_hospital(registros,estado,Tiempo)
    print("="*150)
    print(f"Hay {res} casos de {estado} en el que el paciente ha estado ingresado mas de {Tiempo} horas dadas como parametro")
    print("="*150)
    

def test_obten_maximo_horas(registros,estado="CIUDAD DE MEXICO"):
    """
    Función que obtiene una lista de tuplas de un determinado estado,
    las tuplas que se muestran son las que tienen el maximo de horas ingresados 
    del caso covid del determinado estado, la funcion podria mostrar varias tuplas si 
    varios casos del mismo estado compartieran le numero maximo de horas, pero no es el caso

    @param registros: tupla con nombre de tipo Caso_covid
    @type registros:[Caso_covid(int, str, str, date, str, str, datetime.date, float, boolean)]
    @param estado:estado por el que se va a filtrar, si no se asigna valor toma el valor Ciudad de Mexico
    @type estado: str

    """
    res = obten_maximo_horas(registros,estado)
    print("="*150)
    print(f"Hay {len(res)} casos covid con el maximo numero de horas ingresado en {estado}")
    mostrar_iterable(res)
    print("="*150)

def test_filtra_n_registros_por_genero_y_estado_ordena_por_horas(registros,estado="CIUDAD DE MEXICO",genero="F",n=4):
    """
    Función que prueba el ordenar una lista de tuplas de un determinado estado y genero,
    las ordena de menor a mayor segun las horas ingresadas en el hospital del caso,
    muestra por pantalla una cantidad n de listas de tuplas

    @param registros: tupla con nombre de tipo Caso_covid
    @type registros:[Caso_covid(int, str, str, date, str, str, datetime.date, float, boolean)]
    @param genero: sexo por el que se va a filtrar las tuplas
    @type genero: str
    @param n: numero de tuplas que se desean mostrar
    @type n. int
    @param estado:estado por el que se va a filtrar, si no se asigna valor toma el valor Ciudad de Mexico
    @type estado: str
    """
    res = filtra_n_registros_por_genero_y_estado_ordena_por_horas(registros,estado,genero)

    if genero== "F":
        x= "Femenino"
    else: x= "Masculino"
    print("="*150)
    print(f"Los {n} casos de {estado} del genero {x} ordenados de menor a mayor segun las horas ingresadas de los casos son:")

    print("="*150)
    if genero== "F":
        x= "Mujeres"
    else: x= "Hombres"
    print(f"Los {n} casos de {estado} de {x} ordenados de menor a mayor segun las horas ingresadas de los casos son:")
    print("="*150)
    mostrar_iterable(res)


def test_agrupa_por_estados(registros):
    """
    Función que muestra por pantalla un diccionario con cada uno de los 28 estados,
    devuelve un diccionario con el estado y las horas ingresado en el hospital
    del primer caso covid del estado correspondiente
    
    @param registros: tupla con nombre de tipo Caso_covid
    @type registros:[Caso_covid(int, str, str, date, str, str, datetime.date, float, boolean)]
    """
    estados = ("CIUDAD DE MEXICO","SINALOA","COAHUILA","CHIAPAS","MEXICO","QUERETARO","NUEVO LEON","DURANGO","PUEBLA","YUCATÓN","QUINTANA ROO","SAN LUIS POTOSI","JALISCO","OAXACA","GUERRERO","AGUASCALIENTES","GUANAJUATO","CHIHUAHUA","TAMAULIPAS","SONORA","VERACRUZ","COLIMA","BAJA CALIFORNIA","HIDALGO","TABASCO","MORELOS","NAYARIT","ZACATECAS","BAJA CALIFORNIA SUR")
    res=agrupa_por_estado(registros,estados)
    print("="*150)
    print(f"Mostrando Diccionario de los estados con su numero de Horas del primer caso correspondiente:")
    print("="*150)
    print("\n".join(str(item) for item in res.items()))

#--------------------------------------------------------------------------------------------------------------------------------------
#Entrega 3
#--------------------------------------------------------------------------------------------------------------------------------------


def test_total_horas_en_el_hospital_de_los_estados_segun_genero(registros,genero="F"):
    """
    Función que prueba la funcion del total de horas en el hospital de los estados segun el genero
    y muestra por pantalla el diccionario que tiene como claves los estados
    y valores el total de horas ingresados del genero determinado

    @param registros: tupla con nombre de tipo Caso_covid
    @type registros:[Caso_covid(int, str, str, date, str, str, datetime.date, float, boolean)]
    @param genero: genero por el cual se va a filtrar el diccionario
    @type genero: str
    @return:Devuelve un diccionario con las claves los estados y los valores la cantidad de horas ingresados de sus casos correspondientes
    @rtype: {str , float}
    """
    res = total_horas_en_el_hospital_de_los_estados_segun_genero(registros,genero)
    if genero == "F":
        x="Femenino"
    else: x="Masculino"
    print("="*150)
    print(f"El total de horas ingresados en el hospital de los casos del genero {x} en cada estado son los siguientes:")
    print("="*150)
    mostrar_diccionario(res)
   
def test_maximo_genero_repetido_en_un_estado(registros,estado="CIUDAD DE MEXICO"):
    """
    Función que prueba la funcion de la cantidad maxima del genero
    que hay como casos en un estado determinado y lo muestra por

    @param registros: tupla con nombre de tipo Caso_covid
    @type registros:[Caso_covid(int, str, str, date, str, str, datetime.date, float, boolean)]
    @param estado: estado por el cual se va a filtrar el diccionario
    @type estado: str
     @return: devuelve un diccionario con la condicion del estado y mostrando solo el genero y la cantida de repeticiones
    @rtype: {str , int}
    """
    
    res = maximo_genero_repetido_en_un_estado(registros,estado)
    print("="*150)
    print(f"El genero mas común de los casos y la cantidad de casos del genero del estado de {estado} es:")
    print(res)
    print("="*150)

def test_maxima_edad_por_genero_estado(registro,estado="CIUDAD DE MEXICO"):
    """
    Función que prueba la funcion para mostrar la edad 
    maxima de cada genero de un estado determinado y muestra por pantalla el diccionario obtenido

    @param registros: tupla con nombre de tipo Info
    @type registros:[Info(int, str, str, date, str, str, datetime.date, float, boolean)]
    @param estado: estado por el cual se filtra el diccionario
    @type estado: str
    @return: dos diccionarios con la edad maxima del genero correpondiente en el estado especificado
    @rtype: {str , int}
    """
    res = maxima_edad_por_genero_estado(registro,estado)
    print("="*150)
    print(f"La edad maxima para cada genero de los casos covid del estado de {estado} son:")
    print("="*150)
    mostrar_diccionario(res)


def test_top_n_estados_por_horas_ingresado(registro,n=3):
    """
    Función que prueba la función que muestra la cantidad n de casos covid 
    y muestra un diccionario con los estados como claves y la cantidad n de horas ingresados
    que son las horas maximas de los n casos covid del estado determinado

    @param registros: tupla con nombre de tipo Info
    @type registros:[Info(int, str, str, date, str, str, datetime.date, float, boolean)]
    @param n: cantidad de casos los cuales se quieren mostrar por consola
    @type n: int
    @return: diccionario con claves de cada estado, y valores de la cantida maxima de horas ingresado de los n casos
    @rtype: {str , float , float , float}
    """
    res= top_n_estados_por_horas_ingresado(registro,n)
    print("="*150)
    print(f"Se muestran las horas maximas de los {n} casos covid de los estados correspondientes:")
    print("="*150)
    mostrar_diccionario(res)


def test_aux_obten_estados_cantidad_casos_por_genero(registro,genero="F"):
    """
    Función que prueba la función auxiliar y muestra por pantalla
    la cantidad de casos de un genero determinado que tiene cada estado,
    de normal esta comentada ya que es una función auxiliar pero podria probarse

    @param registros: tupla con nombre de tipo Info
    @type registros:[Info(int, str, str, date, str, str, datetime.date, float, boolean)]
    @param genero: genero por el cual se filtra el diccionario
    @type genero: str
    @return: diccionario con los estados como claves y la cantidad de casos del genero determinado como valores
    @rtype: {str , int}
    """
    res = aux_obten_estados_cantidad_casos_por_genero(registro,genero)
    if genero == "F":
        x="Femenino"
    else: x="Masculino"
    print("="*150)
    print(f"Estos son la cantidad de casos covid del genero {x} de los estados correspondientes:")
    print("="*150)
    mostrar_diccionario(res)


def test_grafica_estados_mas_frecuentes_por_genero(registro,genero="F"):
    """
    Función que prueba la función de dibujar graficas y muestra las graficas del genero determinado

    @param registros: tupla con nombre de tipo Info
    @type registros:[Info(int, str, str, date, str, str, datetime.date, float, boolean)]
    @param genero: genero por el cual se va a filtrar para mostrar la grafica
    @type genero: str
    @return: grafica con los estados y su cantidad de casos del genero determinado
    @rtype: grafica   
    """
    grafica_estados_mas_frecuentes_por_genero(registro,genero)

if __name__=="__main__":
    #test_lee_confirmados("./data/confirmados-2020-03-21.csv")
    
    Registro = lee_confirmados("./data/confirmados-2020-03-21.csv")

    test_filtra_por_estado(Registro)
    test_filtra_por_estado(Registro,"NUEVO LEON")

    test_filtra_por_genero(Registro)
    test_filtra_por_genero(Registro,"F",7)

    test_calcular_casos_total_hospital(Registro,"YUCATÓN",100)
    test_calcular_casos_total_hospital(Registro)

    test_obten_maximo_horas(Registro,"COAHUILA")
    test_obten_maximo_horas(Registro)

    test_filtra_n_registros_por_genero_y_estado_ordena_por_horas(Registro,"MEXICO","M",6)
    test_filtra_n_registros_por_genero_y_estado_ordena_por_horas(Registro)

    test_agrupa_por_estados(Registro)

    test_total_horas_en_el_hospital_de_los_estados_segun_genero(Registro)
    test_total_horas_en_el_hospital_de_los_estados_segun_genero(Registro,"M")
   
    test_maximo_genero_repetido_en_un_estado(Registro)
    test_maximo_genero_repetido_en_un_estado(Registro,"YUCATÓN")
    
    test_maxima_edad_por_genero_estado(Registro)
    test_maxima_edad_por_genero_estado(Registro,"YUCATÓN")

    test_top_n_estados_por_horas_ingresado(Registro)
    test_top_n_estados_por_horas_ingresado(Registro,5)

    #test_aux_obten_estados_cantidad_casos_por_genero(Registro,"M")
    #test_aux_obten_estados_cantidad_casos_por_genero(Registro,)

    test_grafica_estados_mas_frecuentes_por_genero(Registro)
    test_grafica_estados_mas_frecuentes_por_genero(Registro,"M")

    

    test_agrupa_por_estados(Registro)
