# Proyecto del Primer Cuatrimestre Fundamentos de Programación (Curso  \<XX\>/\<YY\>)
Autor/a: \<Marcos Núñez Morales\>   uvus:\<XJR2031\>

El dataset son casos confirmados de covid recolectados por el govierno de Mexico, provienen de la siguient fuente: SINAVE/DGE/InDRE.

Este programa se encarga de leer datasets de este tipo y devolver por pantalla toda la información


## Estructura de las carpetas del proyecto

* **/src**: Contiene los diferentes módulos de Python que conforman el proyecto.
  * **\<Casos.py\>**: El modulo principal "Casos" contiene la funcion encargada de leer el dataset, a su vez que crea la tupla nombrada y convierte las variables en str.
  * **\<Casos_test.py\>**: EL modulo "Casos_test" es el modulo de prueba para mostrar por terminal como se vería la tupla creada en el modulo "Casos", este modulo se encarga de hacer uso de la funcion de lectura definida en el modulo principal y buscar los datos en el dataset para luego imprimirlos por pantalla.
  * **\<parser.py\>**: Este modulo "parser" se encarga de asignar el valor true y false dependiendo del dato que entre(Si o No) y definir las variables de tipo fecha . 
* **/data**: Contiene el dataset del proyecto
    * **\<confirmados-2020-03-21.csv\>**: Son los datos de casos covid en Mexico el dia 21-03-2020, contiene todos los datos especificos de cada caso.
    
## Estructura del *dataset*

Los datos que contiene el dataset son especificos de cada caso:

El dataset está compuesto por \<10\> columnas, con la siguiente descripción:

* **\<Numero de caso>**: de tipo \<int\>, representa el número del caso covid 
* **\<Estado>**: de tipo \<str\>, representa el estado de Mexico donde se encontraba el individuo
* **\<Sexo>** : de tipo \<str\>, representa el sexo del individuo
* **\<Edad>** : de tipo \<int\>, representa la edad del idividuo en el dia del registro
* **\<Fecha del inicio de los sintomas>** : de tipo \<datetime\>, representa la fecha en la que el individuuo comenzo a presentar sintomas
* **\<Identificación covid>** : de tipo \<str\>, representa si el individuo ha sido confirmado con covid mediante RT-PCR
* **\<Procedencia>** : de tipo \<str\>, representa la procedencia del indivuo
* **\<Fecha de llegada a Mexico>** : de tipo \<datetime\>, representa la fecha en la que el individuo llegó a Mexico, puede ser una en concreto o que el individuo ya estuviera en Mexico y se devuelve el valor "NA" en ese caso
* **\<Horas ingresado>** : de tipo \<float\>, representa las horas que ha estado el individuo ingresado en el hospital
* **\<Recuperado tras 14 días>** : de tipo \<bool\>, representa si el individuo se ha recuperado de los sintomas despues de 14 dias de tenerlos

## Tipos implementados

La namedtuple implementada esta definida en el modulo "Casos" definida por el nombre "Confirmado",contiene todos los nombres de cada columa y les asigna sus valores, en pantalla muestra "Caso_covid=" y los datos correspondientes

## Funciones implementadas
La funcion pricipal encargada de leer el dataset se encuentra en el modulo "Casos", las funciones del modulo "parser" solo se encargan de definir variables del formato bool y datetime, las funciones del modulo "Casos_test" se encargan de hacer uso de la funcion principal y mostrarlo por pantalla.

### \<Casos\>

* **<lee_confirmados>**: Esta funcion define una lista vacia con el nombre "Confirmados", posteriormente con el fichero de datos abierto considera todas las columnas del ficher, define los datos de cada columna y crea una tupla con el nombre "Confirmado" y la añade a la lista vacia del inicio, devuelve la lista 

### \<Casos_test\>

* **<mostrar_iterable>**: Muestra por consola los elemtos de cada iterable en distintas filas
* **<test_lee_confirmados>**: Hace una llamada de la funcion principal e imripime por pantalla la cantidad de casos que ha leido y las tuplas correspondientes a cada caso

### \<parser\>

* **<parse_bool>**: En el dataset solo se puede encontar el valor "Si" o "No", esta funcion le asigna el valor "True" al "Si" y el "False" al "No" 
* **<parse_date>**: Define la cadena de formato fecha sin hora, devuelve la fecha en el caso de que haya una en el dataset, si no hay fecha devuelve "NA".