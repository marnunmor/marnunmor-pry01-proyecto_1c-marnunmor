from  Casos import *

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
    


def test_calcular_casos_total_hospital(registros,estado="CIUDAD DE MEXICO"):
    """
    Función que prueba el calculo de los casos totales de los hospitales,
    muetra por pantalla la cantidad de casos covid que ha tenido un determinado estado

    @param registros: tupla con nombre de tipo Caso_covid
    @type registros:[Caso_covid(int, str, str, date, str, str, datetime.date, float, boolean)]
    @param estado:estado por el que se va a filtrar, si no se asigna valor toma el valor Ciudad de Mexico
    @type estado: str    
    """
    res=calcular_casos_total_hospital(registros,estado)
    print("="*150)
    print(f"Hay {res} casos del estado {estado} en el que el paciente ha estado ingresado mas de un día dado como parametro")
    
    

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

def test_ordena_por_horas(registros,estado="CIUDAD DE MEXICO"):
    """
    Función que prueba el ordenar una lista de tuplas de un determinado estado,
    las ordena de menor a mayor segun las horas ingresadas en el hospital del caso,
    muestra por pantalla una lista de tuplas

    @param registros: tupla con nombre de tipo Caso_covid
    @type registros:[Caso_covid(int, str, str, date, str, str, datetime.date, float, boolean)]
    @param estado:estado por el que se va a filtrar, si no se asigna valor toma el valor Ciudad de Mexico
    @type estado: str
    """
    res = ordena_por_horas(registros,estado)
    print("="*150)
    print(f"Hay {len(res)} casos de {estado} ordenados de menor a mayor segun las horas ingresadas de los casos:")
    print("="*150)
    mostrar_iterable(res)


def test_agrupa_por_estado(registros):
    """
    Función que muestra por pantalla un diccionario con cada uno de los 28 estados,
    devuleve un diccionario con el estado y las horas ingresado en el hospital
    del primer caso covid del estado correspondiente
    
    @param registros: tupla con nombre de tipo Caso_covid
    @type registros:[Caso_covid(int, str, str, date, str, str, datetime.date, float, boolean)]
    """
    Estados = ("CIUDAD DE MEXICO","SINALOA","COAHUILA","CHIAPAS","MEXICO","QUERETARO","NUEVO LEON","DURANGO","PUEBLA","YUCATÓN","QUINTANA ROO","SAN LUIS POTOSI","JALISCO","OAXACA","GUERRERO","AGUASCALIENTES","GUANAJUATO","CHIHUAHUA","TAMAULIPAS","SONORA","VERACRUZ","COLIMA","BAJA CALIFORNIA","HIDALGO","TABASCO","MORELOS","NAYARIT","ZACATECAS","BAJA CALIFORNIA SUR")
    res=agrupar_por_estado(registros,Estados)
    print("="*150)
    print(f"Mostrando Diccionario de los estados con su numero de Horas del primer caso correspondiente:")
    print("="*150)
    print("\n".join(str(item) for item in res.items()))

   


if __name__=="__main__":
    test_lee_confirmados("./data/confirmados-2020-03-21.csv")
    
    Registro = lee_confirmados("./data/confirmados-2020-03-21.csv")

    test_filtra_por_estado(Registro)
    test_filtra_por_estado(Registro,"NUEVO LEON")

    test_calcular_casos_total_hospital(Registro,"YUCATÓN")
    test_calcular_casos_total_hospital(Registro)

    test_obten_maximo_horas(Registro,"COAHUILA")
    test_obten_maximo_horas(Registro)

    test_ordena_por_horas(Registro,"MEXICO")
    test_ordena_por_horas(Registro)

    test_agrupa_por_estado(Registro)