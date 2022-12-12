# Proyecto del Primer Cuatrimestre Fundamentos de Programación (Curso  \22\/\26\)
Autor/a: \Marcos Núñez Morales\   uvus:\XJR2031\

El dataset son casos confirmados de covid recolectados por el govierno de Mexico, provienen de la siguient fuente: SINAVE/DGE/InDRE.

Este programa se encarga de leer datasets de este tipo y devolver por pantalla toda la información


## Estructura de las carpetas del proyecto

* **/src**: Contiene los diferentes módulos de Python que conforman el proyecto.
  * **\Casos.py**: El modulo principal "Casos" contiene la funcion encargada de leer el dataset, a su vez que crea la tupla nombrada y convierte las variables en str.
  * **\Casos_test.py**: EL modulo "Casos_test" es el modulo de prueba para mostrar por terminal como se vería la tupla creada en el modulo "Casos", este modulo se encarga de hacer uso de la funcion de lectura definida en el modulo principal y buscar los datos en el dataset para luego imprimirlos por pantalla.
  * **\parsers.py**: Este modulo "parser" se encarga de asignar el valor true y false dependiendo del dato que entre(Si o No) y definir las variables de tipo fecha . 
* **/data**: Contiene el dataset del proyecto
    * **\confirmados-2020-03-21.csv**: Son los datos de casos covid en Mexico el dia 21-03-2020, contiene todos los datos especificos de cada caso.
    
## Estructura del *dataset*

El dataset fue obtenido desde la siguiente url: https://www.kaggle.com/datasets/adangalvan/covidmexico

Este dataset es la publicación diaria de casos confirmados de Covid-19 en Mexico.

En un principio el dataset estaba compuesto por **8** columnas, a las cuales se les ha añadido dos generadas de manera aleatoria.
Las nuevas columnas añadidas son la columna **Horas_ingresado** y la columna **Recuperado_tras_14_dias**

El dataset está compuesto por **10** columnas, con la siguiente descripción:

* **\Numero de caso**: de tipo \int\, representa el número del caso covid 
* **\Estado**: de tipo \str\, representa el estado de Mexico donde se encontraba el individuo
* **\Sexo** : de tipo \str\, representa el sexo del individuo
* **\Edad** : de tipo \int\, representa la edad del idividuo en el dia del registro
* **\Fecha del inicio de los sintomas** : de tipo \datetime\, representa la fecha en la que el individuuo comenzo a presentar sintomas
* **\Identificación covid** : de tipo \str\, representa si el individuo ha sido confirmado con covid mediante RT-PCR
* **\Procedencia** : de tipo \str\, representa la procedencia del indivuo
* **\Fecha de llegada a Mexico** : de tipo \datetime\, representa la fecha en la que el individuo llegó a Mexico, puede ser una en concreto o que el individuo ya estuviera en Mexico y se devuelve el valor "NA" en ese caso
* **\Horas ingresado** : de tipo \float\, representa las horas que ha estado el individuo ingresado en el hospital
* **\Recuperado tras 14 días** : de tipo \bool\, representa si el individuo se ha recuperado de los sintomas despues de 14 dias de tenerlos

## Tipos implementados

La namedtuple implementada esta definida en el modulo "Casos" definida por el nombre "Infor",contiene todos los nombres de cada columa y les asigna sus valores, en pantalla muestra "Info=" y los datos correspondientes

## Funciones implementadas
La funcion pricipal encargada de leer el dataset se encuentra en el modulo "Casos", las funciones del modulo "parser" solo se encargan de definir variables del formato bool y datetime, las funciones del modulo "Casos_test" se encargan de hacer uso de las funciones del modulo principal y mostrarlas por pantalla.

### \Casos\

* **lee_confirmados**: Esta funcion define una lista vacia con el nombre "Confirmados", posteriormente con el fichero de datos abierto considera todas las columnas del ficher, define los datos de cada columna y crea una tupla con el nombre "Confirmado" y la añade a la lista vacia del inicio, devuelve la lista 

* **filtra_por_estado**: Esta función define una lista vacia y va añadiendo a la misma las tuplas que corresponden con un estado en concreto que se elige antes de ejecutarla

* **calcular_casos_total_hospital**: Esta función cuenta la cantidad de tuplas que hay para un determinado estado, cuenta la cantidad de casos covid que han habido en el estado que se elige antes de ejecutar

* **obten_maximo_horas**: Esta función devuelve una lista de tuplas con todos los casos covid de un determinado estado que se elige antes de ejecutar, las tuplas que devuelve son las que tienen la cantidad maxima de horas en el hospital, devolverá una sola tupla por estado ya que no hay tantos datos como para que se hayan repetido la cantidad maxima de horas varias veces en un estado, si se diera el caso de que un estado tuviera varios casos en el que se compartan la misma cantidad maxima de horas se mostrarian ambos.

* **ordena_por_horas**: Esta función crea una lista de tuplas con todos los casos covid de un determinado estado, devuelve la lista ordenada de menor a mayor en función del numero de horas ingresado en e hospital.

* **agrupar_por_estado**: Esta función crea un diccionario vacio al cual va añadiendo todos los estados que hay en el dataset y devuelve el diccionario con los estados una vez y a cada uno le añade las horas ingresadas del primer caso del estado correspondiente.

* **total_horas_en_el_hospital_de_los_estados_segun_genero**: Esta función devuelve un diccionario siendo las claves los estados, y los valores la cantitad de horas que han estado ingresados los casos covid del genero indicado con anterioridad

* **maximo_genero_repetido_en_un_estado**: Esta función devuelve un diccionario de un estado determinado, el diccionario muestra el genero mas repetido en los casos del estado correspondiente y la cantidad de veces que se repite, si no se especifica devuelve los casos del estado de Ciudad de Mexico

* **maxima_edad_por_genero_estado**: Esta función devuelve un diccionario de un estado determinado,siempre devuelve dos diccionarios (uno para cada genero), el diccionario muestra la maxima edad de cada sexo en el estado correspondiente, si no se especifica devuelve los casos del estado de Ciudad de Mexico

* **top_n_estados_por_horas_ingresado**: Esta función devuelve un diccionario con los estados como claves, y una cantidad "n" de horas ingresado de los casos covid del estado correspondiente como valores, la cantidad de horas ingresado son los casos con la maxima cantidad de horas, si no se especifica devuelve los 3 casos con la maxima cantidad de horas

* **aux_obten_estados_cantidad_casos_por_genero**: Esta función que devuelve un diccionario de un genero determinado, esta función es una auxiliar para poder obtener las graficas devuelve un diccionario de los estados y la cantidad de casos covid  que hay en dicho estado segun el genero determinado

* **grafica_estados_mas_frecuentes_por_genero**: Esta función dibuja una grafica de barras basandose en la función auxiliar,la grafica muestra los estados y muestra la cantidad de casos del genero especificado como los valores de las barras


### \Casos_test\

* **mostrar_iterable**: Muestra por consola los elemtos de cada iterable en distintas filas
* **mostrar_diccionario**: Muestrapor consola los elementos de un diccionario, muestra las claves y sus valores 

* **test_lee_confirmados**: Hace una llamada de la funcion principal e imripime por pantalla la cantidad de casos que ha leido y las tuplas correspondientes a cada caso

* **test_filtra_por_estado**: Hace llamada a la funcion **filtra_por_estado** y muestra en pantalla la lista de tuplas del estado determinado

* **test_calcular_casos_total_hospital**: Hace llamada a la funcion **calcular_casos_total_hopital** y muestra por pantalla en numero de casos que han habido en el estado determinado con anterioridad

* **test_obten_maximo_horas**: Hace llamda a la función **obten_maximo_horas** y muestra por pantalla las tuplas(casi siempre es una) de un estado determinado que tiene el numero maximo de horas

* **test_ordena_por_horas**: Hace llamada a la función **ordena_por_horas** y muestra por pantalla una lista de tuplas de un determinado estado elegido con anterioridad, la lista esta ordenada de menor a mayor en función de las horas ingresadas en el hospital de los casos

* **test_agrupa_por_estado**: Hace llamada a la función **agrupa_por_estado** y muestra por pantalla un diccionario con cada uno de los estados y cada uno con las horas correspondientes de su primer caso covid del dataset

* **test_total_horas_en_el_hospital_de_los_estados_segun_genero**: Hacella llamada a la función **total_horas_en_el_hospital_de_los_estados_segun_genero** y muestra por pantalla el diccionario que tiene como claves los estados y valores el total de horas ingresados del genero determinado

* **test_maximo_genero_repetido_en_un_estado**: Hace llamada a la función **maximo_genero_repetido_en_un_estado** prueba la función y lo muestra por pantalla el diccionario el genero mas repetido el estado correspondiente y su cantidad de veces repetido

* **test_maxima_edad_por_genero_estado**: Hace llamada a la función **maxima_edad_por_genero_estado**  y muestra por pantalla el diccionario que enseña los generos y la edad maxima del caso covid de dicho genero en un estado determinado

* **test_top_n_estados_por_horas_ingresado**: Hace llamada a la función **top_n_estados_por_horas_ingresado** y muestra un diccionario con los estados como claves y la cantidad n de horas ingresados que son las horas maximas de los n casos covid del estado determinado

* **test_aux_obten_estados_cantidad_casos_por_genero**: Hace llamada a la función **aux_obten_estados_cantidad_casos_por_genero** y muestra por pantalla la cantidad de casos de un genero determinado que tiene cada estado, de normal esta comentada ya que es una función auxiliar pero podria probarse

* **test_grafica_estados_mas_frecuentes_por_genero**: Hace llamada a la función **grafica_estados_mas_frecuentes_por_genero** y muestra las graficas del genero determinado enseñando los estados y la cantidad de casos que han habido en cada estado del genero correspondiente
### \parsers\

* **parse_bool**: En el dataset solo se puede encontar el valor "Si" o "No", esta funcion le asigna el valor "True" al "Si" y el "False" al "No" 
* **parse_date**: Define la cadena de formato fecha sin hora, devuelve la fecha en el caso de que haya una en el dataset, si no hay fecha devuelve "NA".
