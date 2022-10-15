'''
Módulo que contiene funciones para conversión de tipos
'''
from datetime import datetime

def parse_bool(cadena):
    '''
    @param cadena: Cadena que puede contener los valores "SI", "NO" (tanto en mayúsculas como en minúsculas)
    o tener el valor None.
    @type cadena: str
    @return: True, si la cadena contiene "SI" (independientemente de las mayúsculas y minúsculas),
        False, si la cadena contiene "NO" y None en cualquier otro caso. 
    '''
    booleano = None
    if cadena.upper() == 'SI':
        booleano = True
    elif cadena.upper() == 'NO':
        booleano = False
    return booleano

def parse_date(cadena, formato = "%d/%m/%Y"):
    '''
    @param cadena: Cadena de texto que representa una fecha
    @type cadena: str
    @param formato: Cadena de texto que representa el formato de una fecha
    @type formato: str
    @return: Un objeto tipo date con la fecha si hay fecha, si no hay fecha registrada devuelve "NA"
    '''
    if cadena != "NA":
        return datetime.strptime(cadena, formato).date()
    else: return "NA"
