
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
    '''Función que prueba la lectura de ficheros.
    Muestra por consola el número de autobuses leidos y
    un listado de los autobuses, mostrando uno por linea

    @param nombre_fichero: Nombre y ruta del fichero a leer
    @type nombre_fichero: str
    '''
    confirmados = lee_confirmados(nombre_fichero)
    print(f"Se han leido {len(confirmados)} casos covid y son:")
    mostrar_iterable(confirmados)

if __name__=="__main__":
    test_lee_confirmados("./data/confirmados-2020-03-21.csv")