'''
Módulo con la funcionalidad principal.
'''

from collections import namedtuple

import csv
from parser import *

#Definición de tupla con nombre
Confirmado = namedtuple('Caso_covid', 'Numero_caso, Estado, Sexo, Edad, Fecha_de_Inicio_de_los_sintomas, Identificacion_de_COVID_19_por_RT_PCR, \
    Procedencia, Fecha_de_llegada_a_Mexico, Horas_ingresado,Recuperado_tras_14_días')


def lee_confirmados(nombre_fichero):
    Confirmados = []
    with open(nombre_fichero, encoding='utf-8') as f:
        lector = csv.reader(f)
        next(lector)
        for NumeroCaso, Estado,Sexo, Edad, FechaInicioSintomas,  IdentificacionCovid,Procedencia, LlegadaAMexico,HorasIngresado,RecuperadoTras14Dias in lector:
            NumeroCaso = int(NumeroCaso)
            Edad = int(Edad)
            FechaInicioSintomas = parse_date(FechaInicioSintomas)
            HorasIngresado = float (HorasIngresado)
            RecuperadoTras14Dias = parse_bool(RecuperadoTras14Dias)
            LlegadaAMexico = parse_date(LlegadaAMexico)       
            tupla = Confirmado(NumeroCaso, Estado, Sexo, Edad, FechaInicioSintomas, IdentificacionCovid,Procedencia, LlegadaAMexico,HorasIngresado,RecuperadoTras14Dias)
            Confirmados.append(tupla)
    return Confirmados  