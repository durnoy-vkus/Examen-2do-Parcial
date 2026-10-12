#Numeros en python
#Tipos numéricos
#int : números enteros
#float : números con decimales
#complex : usa j
#Todos pueden ser positivos o negativos

#Como identificarlos
#type muestra el tipo
x=1
y=2.5
z=5 + 1j
type(x)
type(y)
type(z)

#Ejemplo número complejo
#Parte real + parte imaginaria
x = 5 + 1j
y = -5 - 1j

#Casteo básico
#De int a float
float(1)  = 1.0
#Agrega .0

#De float a int
int(2.5) = 2
#Trunca decimales

#Conversion a complex
#Permitidos:
complex(5) = 5+0j
complex(5.5) = 5.5+0j

#No permitidos
#Conversion de complex a int o float

#Numeros aleatorios con random
import random
random.randrange(1,10)
#Genera números aleatorios del 1 al 9
#Ignora el valor final
#Util en juegos

#STRINGS EN PYTHON
#¿Que es un string?
#Texto guardado dentro de una variable

#Clave comillas
Simples = 'hola'
Dobles = "I/'m Sergi"
Triples = """varias líneas"""
#Las comillas triples permiten ingresar múltiples palabras

#Contar carácteres
palabra = 'murcielago'
print(len(palabra))
#Imprime 10
#len cuenta los carácteres, incluye espacios

#Buscar texto
"Python" in texto = True
"python" in texto = False
"JavaScript" in texto = True
#Python es case sensitive

#Cambiar formato
texto = 'Fundamentos de Python'
texto.upper() #Devuelve todo en mayúsculas
texto.lower() #Devuelve todo en minúsculas

#Limpiar espacios
espacios = ' este es el texto '
espacios.strip()
#Devuelve 'este es el texto'
#Solo quita los espacios extremos, no los internos
#Ideal para sanitizar inputs

#DOMINA STRINGS EN PYTHON
#Indices en Strings
texto2 = "Este es un texto"
#Tiene 15 posiciones contando desde 0
#Espacios y signos también ocupan espacios
print(texto[0]) #Imprime 'E'
print(texto[4]) #Imprimer un espacio

#Slicing: Fin no incluído
texto2 = "Este un texto"
print(texto[0:4]) #Imprime 'Este'
print(texto[:7]) #Omite final, imprime 'Este es'
print(texto[5:]) #Omite el inicio, imprime 'es un texto'
print(texto[5:-2]) #Indices negativos, imprime 'este es un tex'

#Remplazar
curso = "Este es un curso de JavaScript"
print(curso.replace("JavaScript", "Python"))
#Imrprime 'Este curso es de Python'
#Si la palabra aparece varias veces se reemplazan todas

#Dividir
texto3="Esto es un texto"
texto_dividido = texto.split(" ")
print(texto_dividido)
#Imprime: ['Este', 'es', 'un', 'texto']

#Comparar sin errores
texto4 = "Este texto tiene MAYÚSCULAS y minúsculas"
buscado = "mayúsculas"
print(buscado in texto4) #Devuelve False
print(buscado.lower() in texto4.lower()) #Devuelve True
#Normaliza el texto con lower o upper y usa in para buscar en el texto

#BOOLEANOS EN PYTHON
#Solo acepta dos valores
#True = verdadero
#False = falso
b=True
f=False
print(type(b)) #Imprime 'bool'

#Las comparaciones generan booleanos
#5>3 devuelve True
#3>5 devuelve false
#Se usan en if y while

#Casting con bool()
#Convierte otros datos a booleanos
#Python evalúa el contenido
bool("Hola") #Devuelve True
bool(123) #Devuelve True
bool([1, 2]) #Devuelve True

#Valores que dan True
#Texto con contenido
#Numeros diferentes de 0
#Lista con elementos
#Datos presentes = Verdadero

#Datos que dan False
#Cadenas vacías
#Numero 0
#Lista vacía
#Nond
#Datos vacíos/inexistentes = Falso

#Validar con isinstance()
número = 5
isinstance(número, int) #True
número = 5.5
isinstance(número, int) #False
#Confirma tipos de datos

#NONE EN PYTHON
#Representa la ausencia total de valor
#Tiene su propia clase: NoneType
x = None
print(x) #None
print(type(x)) #<class 'NoneType'>

#No es lo mismo que vacío
#Cada valor sigue siendo su propio tipo
"" #String vacío 
0 #cero
False #booleano falso
[] #lista vacía
None #ausencia de valor
#Estar vacío no implica inexistencia, profundo

#None es igual a false o 0
#Aunque se evalúan como falsos, son de tipo diferente
print(type(False)) #<class 'bool'>
print(type(0)) #<class 'int'>
print(type(None)) #<class 'NoneType'>

#Porque importa antes de ver funciones?
#Porque una función no puede devolver "nada"
#En esos casos devuelve "None"
def saludar():
       print("Hola")
#No hay return
resultado = saludar()
print (resultado) #None
print(type(resultado)) #<class 'NoneType'>

#¿Cómo identificar un None?
#Con un type()
x=None
print(type(x))
#<class 'NoneType'>
#Comparacion directa
if x is None:
      print("x no tiene valor")

#OPERADORES ARITMÉTICOS EN PYTHON
#Realizan calculos con variables
#Base x=5 y=10

#Suma y resta
#+ suma valores
#- resta valores
#Python respeta el signo
print(x + y) #Imprime 15
print(x - y) #Imprime 5

#Multiplicacion y división
#* Multiplica
#/ Divide
#/ Siempre da float
print(x*y) #50
print(x/y) #2.0

#Modulo, potencia y //
#Modulo: Residuo de división %
#12%5 = 2
#Potencia: Eleva base **
#x ** y = 100000
#Division entera: Quita los decimales //
#12//5 = 2

#Detectar números pares
#Usa números % 2 == 0
#Si da True, es par
par = 8
print(par%2==0)  #True

#Orden de precedencia / Jerarquía de operaciones
#1.- ()
#2.- **
#3.- * / // %
#4.- + -
#5.- Comparaciones
#6.- Lógicos
#Tip: usa paréntesis para forzar orden

#Ejemplo operadores aritmeticos
print("Suma: ", 5+3)
print("Resta:", 10-4)
print("Multiplicación:", 3*4)
print("División:", f"{10/3}")
#Limitar a dos decimales
print("División:", f"{10/3:.2f}")
print("División entera:", 10//3)
print("Módulo:", 10%3)
print("Potencia:", 2**3)

#Operadores de asignación en Python
#Actualizan el valor de una variable usando su valor previo y una operación
#Forma larga
x=5
x = x+3 #8
x = x-3 #2
#Operador de asignación
x = 5
x += 3 #8
x -= 3 #2

#Operaciones básicas y tipos
#*=     x*=3    #15    #int
#/=      x/=3    #5.0  #float
#%/     x%/1   #1.0   #float
#//=     x//=2   #2     #int
#**=    x**=3  #125 #int

#Modulo y división entera
#Modulo, devuelve el resto de la división y lo reasigna
x=5.0  #float
x%=2  #1.0
#Division entera (//), divide y descarta la parte decimal
y=20 
y//=2 #10
y=21
y//=2 #10

#Exponente (**=), eleva a potencias repetidas y reasigna
y=10
y**=3 #1000 (10*10*10)

#Operador Walrus (:=)
#Asigna y devuelve el valor en la misma expresión
print(z := 3) #Imprime 3 y a la vez asigna z=3
print(z)

#Resumen
#= Asigna valor inicial
#+= suma y reasigna
#-= resta y reasigna
#*= multiplica y reasigna
#/= divide y reasigna > resultado flotante
#%= módulo (residuo) y reasigna
#//= división entera (ignora decimales)
#**= exponente y reasigna
#:= Walrus: asigna y usa en la misma expresión

#OPERADORES LÓGICOS EN PYTHON
#Estos operadores permiten combinar dos o más condiciones booleanas para tomar una decisión
#x=5 y=3 x=5
#Operador AND - Todas las condiciones deben de ser True
#A           B          A and B
#True      True     True
#True      False    False
#False    True      False
#False    False    False
#Ejemplo
#x>y and y>z 
x>y #True
y>z #False
#Resultado final = False

#Operador OR - Una condición debe de ser verdadera
#A           B          A and B
#True      True     True
#True      False    True
#False    True      True
#False    False     False
#Ejemplo
#x>y or y>z 
x>y #True
y>z #False
#Resultado final = True

#Operador NOT - Invierte el valor de un booleano
#A            Not A
#True       False
#False      True
#Ejemplos
not True     #False
not False   #True
not (x>y)    #False
not (x==z)  #False

#Ejemplo Operadores Lógicos
edad = 18
tiene_identificacion = True
es_estudiante = False
if edad >= 18 and tiene_identificacion:
    print("Cumple ambas condiciones")
if edad >= 18 or es_estudiante:
    print("Cumple al menos una condición")
if not es_estudiante:
    print("No es estudiante")

#Ejemplo Entrada de datos
nombre = input("¿Tu nombre? ")
edad = int(input("¿Tu edad? "))
print("Hola,", nombre)
print(f"En 5 años tendrás {edad + 5}")
#input() siempre devuelve str
#Usar int() o float() para convertir

#ENTRADA DE DATOS EN PYTHON
#input()pausa el programa y espera datos desde el teclado
#Devuelve el valor como texto

#Sintaxis
nombre = input("Escribe tu nombre: ")
#El mensaje orienta al usuario, el dato se guarda en el nombre

#Clave
#input() siempre devuelve texto
#Convierte antes de calcular
#int() para numeros enteros
#float() para numeros decimales

#Ejemplo
juego = input("Videojuego favorito: ")
horas = int(input("Horas jugadas: "))
print(juego, horas)

#Pasos
#1.- Mostrar una pregunta
#2.- Capturar la respuesta
#3.- Convertir si es necesario
#4.- Usar el dato

#Convesion de tipos(Casting)
#String a numero
num_str = "42"
num_int = int(num_str) #42
num_flt = float(num_str) #42.0

#Numero a string
edad = 25
texto = str(edad) #"25"

#Redondear
pi = 3.14159
print(round(pi, 2)) #3.14

#COLECCIONES EN PYTHON
#LISTAS EN PYTHON
#¿Que es una lista?
#Es una coleccion de elementos
#Ordenados
#Mutable
#Permite duplicadosh
#Indices desde 0

#Ejemplo - Acceder y modificar
frutas[1] = "naranja"
frutas[1] = "banana"

#Clave - Agregar y eliminar
#append("barco") = agrega al final
#insert(1, bicicleta) = inserta en la posicion
#remove("auto") = borra un valor
#pop(1) = borra por indice

#Pasos - Medir y cortar
len(frutas) #Cuenta elementos
frutas[0:2] #Rango
frutas[:2] #Desde inicio
frutas[1:] #Hasta el final

#Clave - Ordenar y verificar
sort() #Ordena
reverse() #Invierte
"manzana" in frutas #Verifica si existe

#Ejemplo - Unir listas
coleccion1 + coleccion2 #NuevaLista
coleccion1.extend(coleccion2) #Modifica lista original

#Listas - Colecciones ordenadas
alumnos = ["Ana", "Luis", "Paty"]
calif = [9.0, 7.5, 8.2]

#Acceder por indice (desde 0)
print(alumnos[0]) #"Ana"
print(alumnos[-1]) #"Paty"

#Agregar y eliminar
alumnos.append("Carlos")
alumnos.remove("Luis")

#Longitud
print(len(alumnos))

#Recorrer
for a in alumnos:
     print(a)

#Operaciones con listas
#Funciones
print(max(calif)) 
print(min(calif))
print(sum(calif))
prom = sum(calif)/len(calif)

#Ordenar
#Ascendente
calif.sort()
#Descendente
calif.sort(reverse=True)

#Slicing los primeros que quieras
top3 = calif[:3]

#List comprehension (filtrado datos)
aprobados = [c for c in calif if c >= 6]

#Tuplas en Python
#Concepto clave
#Ordenadas
#Inmutables, no cambian
#Permiten duplicados
#Acepta distintos tipos de datos
#Ejemplo
tecnologia = ("Python", "JavaScript", "Go")
print(tecnologia) #("Python", "JavaScript", "Go")
print(type(tecnologia)) #<class 'tuple'>

#Tupla de un solo elemento
#Sin coma
fruta = ("manzana")
print(type(fruta)) #<class 'str'>
#Con coma
fruta = ("manzana",)
print(type(fruta)) #<class 'tuple'>
#Duplicados permitidos
t = ("Python", "Go", "JavaScript", "Python")
print(len(t))

#Mix de tipos y desempaquetado
#Tipos mezclados
tupla = ("Python", 5, True)
print(type(tupla)) #<class 'tuple'>
#Desempaquetado
x, y = tupla
print(x) #Python
print(y) #5
print(z) #True

#Concatenar y duplicar
#Concatenar
tupla1 = (1, 2, 3)
tupla2 = (4, 5, 6)
tupla3 = tupla1 + tupla2
print(tupla3) #(1, 2, 3, 4, 5, 6)
#Duplicar
tupla = ("A", "B", "C")
print(tupla * 2) #('A', 'B', 'C', 'A', 'B', 'C'

#Recorrer con for
colores = ("rojo", "verde", "azul")
for color in colores:
    print(color)
#rojo   
#verde
#azul

#Modificar una tupla (Truco)
#1.- Convertir a lista
#2.- Modificar la lista
#3.- Convertir a tupla
tupla_a_modificar = ("Python", "JavaScript", "Go")
lista_comodin = list(tupla_a_modificar)
lista_comodin.append("ReactJS")
tupla_modificada = tuple(lista_comodin)
print(tupla_modificada) #('Python', 'JavaScript', 'Go', 'ReactJS')

#Tuplas
periodo = ("Agosto", "Diciembre", 2026)

inicio, fin, anio = periodo
print(inicio)
print(fin)
print(anio)

periodo[0] = "Enero"

#Conjuntos (sets) en Python
#¿Que es un conjunto?
#Ejemplo
frutas = {"manzana", "naranja", "mandarina", "naranja"}
print(frutas) #{'mandarina', 'naranja', 'manzana'}
print(type(frutas)) #<class 'set'>
print(len(frutas)) #3 (el duplicado se ignora)

#Verificar elementos
#Usa in y not para comprobar presencia
frutas = ("manzana", "naranja", "mandarina")
print("manzana" in frutas) #True
print("pera" not in frutas) #True

#Agregar elementos
#add() agrega uno
frutas = {"manzana", "naranja"}
frutas.add("pera")
print(frutas) #{'pera', 'naranja', 'manzana'}
#Update() agrega varios
frutas_tropicales = {"mango", "piña"}
frutas.update(frutas_tropicales)
print(frutas) #{'pera', 'naranja', 'mango', 'manzana', 'piña'}

#Eliminar elementos
#remove(x) elimina un elemento, si no existe da error
s = {1, 2, 3}
s.remove(2)
print(s) #{1, 3}
#Error si no existe

#discard(x) elimina un elemento, si no existe no hace nada
s = {1, 2, 3}
s.discard(5)
print(s) #{1, 2, 3}
#Seguro, sin error

#pop() elimina un elemento aleatorio
s = {1, 2, 3}
s.pop() #Aleatorio
print(s) #Cambia cada vez

#clear() vacia todo el conjunto
s = {1, 2, 3}
s.clear()
print(s) #set()

#Operaciones entre conjuntos
set1 = {"a", "b", "c"}
set2 = {"c", "d", "e"}

#Union
set1.union(set2) #{'a', 'b', 'c', 'd', 'e'} (todos)
#Intersección
set1.intersection(set2) #{'c'} (comunes)
#Diferencia
set1.difference(set2) #{'a', 'b'} (solo en set1)

#Eliminar duplicados de una lista
#lista con duplicados
lista = [1, 2, 2, 3, 3, 4]
#Convertir a set
set(lista)
#Volver a lista
lista_limpia = list(set(lista))
#Resultado
lista_limpia # [1, 2, 3, 4]

frutas = {"manzana", "naranja", "naranja", "pera"}
print(frutas)

#Conjuntos
#Diccionarios en python
#¿Que es un diccionario?
#Coleccion ordenada
#Pares clave-valor
#Claves unicas
#Valores pueden repetirse
#Acepta distintos tipos de datos
#Ejemplo
auto = {
     "marca": "Renault",
     "Modelo": "Clio",
     "Año": 2025
}
#Acceder a valores
#Obten el valor usando la clave
#Con corchetes
print(auto["marca"]) #Renault
#Con get
print(auto.get("marca")) #Renault

#Claves, valores y verificacion
#Claves
auto.keys #Marca, modelo, año
#Valores
auto.values #Renault, Clio, 2025
#¿Existe una clave?
if "marca" in auto:
     print("Si existe") #Case sensitive
#"marca" != "Marca"

#Modificar, agregar y eliminar
auto["Año"] = 2020 #Modifica
auto["color"] = "verde" #Agrega

#Con update() (varios cambios)
auto.update({"año": 2022, "puertas": 4})

#Eliminar elementos
auto.pop("puertas") #elimina la clave indicada
auto.popitem() #elimina el ultimo par insertado
auto.clear() #Vacia el diccionario {}

#Recorrer un diccionario
for k in auto:
     print(k)
#marca
#modelo
#año

for v in auto.values():
     print(v)
#Renault
#Clio
#2022
#...

#Diccionarios anidados
familia = {
     "hijo1": {"nombre": "Pedro", "edad": 8},
     "hijo2": {"nombre": "Ana", "edad": 7},
     "hijo1": {"nombre": "Marcelo", "edad": 6}
     }
#Acceder a datos internos
print(familia["hijo1"]["nombre"]) #Pedro

#Diccionarios: Pares clave - valor
alumno = {
     "nombre": "Ana Lopez",
     "grupo": "3A",
     "Calificaciones": [8.5, 9.0, 7.5]
}

#Acceder
print(alumno["nombre"]) #"Ana Lopez"

#Agregar / modificar
alumno["email"] = "ana@mail.com"
alumno["grupo"] = "3B"

#Recorrer
#Clave y valor
for clave, valor in alumno.items():
     print(f"{clave}; {valor}")

#Valores 
for valor in alumno.values():
     print(valor)

#Claves
for clave in alumno:
     print(clave)

#Bucle for en python
#¿que hace?
#Recorre una secuencia iterable
#Toma un elemento por vuelta
#Evita codigo repetido
#Sirve para texto, listas, tuplas
palabra = "Python"
for letra in palabra:
     print(letra)

#Ejemplo - Recorrer listas
frutas = ["manzana", "naranja", "kiwi"]
for fruta in frutas:
    print(fruta)

#Clave - break, continue y else
#break - Detiene todo el bucle
#if fruta == 
#    "naranja":
#     break

#Continue - salta solo esa vuelta
#if fruta == 
#    "naranja":
#    continue

#else - corre al terminar normal
else: 
     print("Ya termino el bucle")

#Pasos
#Como funciona range()
range(10) #de 0 a 9
range(3,5) #3 y 4
range(0,10,2) #0, 2, 4, 6 y 8

#Ejemplo for anidado
adjetivos = ["rica", "saludable"]
for adjetivo in adjetivos:
     for fruta in frutas:
          print(fruta, adjetivo)

#Clave
#pass
for i in range(10):
     pass
#Evita bloque vacio

#Break y continue
#break: salir del ciclo
for i in range(10):
    if i == 5:
          break;
    print(i) #0,1,2,3 y 4

#Continue: saltar iteracion
for i in range(6):
     if i ==3:
          continue
     print(i) #0,1,2,4,5

#Como agregar datos en python
#Lista
#Agregar con append()
compras = ["pan", "leche"]
compras.append("huevos")
print(compras)

#Tupla()
#No usa append()
ubicacion = ("Casa", "Trabajo")
ubicacion += ("Escuela")
print(ubicacion)

#Diccionario
#Agregar con una clave
precios = {"pan": 25}
precios["leche"] = 30
print(precios)

#Colecciones en python
#Tupla - Coleccion ordenada e inmutable
tupla = (1, "a", True)
#Ejemplo
t = (10, "hola", 3.5)
print(t[1]) #hola

#Lista - Coleccion ordenada y mutable
lista = [1, "a", True]
#Ejemplo
l = [1, 2, 3]
l.append(4)
print(l) #1, 2, 3, 4

#Diccionario - Coleccion ordenada de pares clave - valor
dicc = {"clave": valor}
#Ejemplo
d = {"nombre": "Ana", "edad": 25}
print(d["nombre"]) #Ana

#Conjunto (set) - Coleccion no ordenada de elementos unicos
conj = {1, "a", True}
#Ejemplo
s = {1, 2, 2, 3}
print(s) #1, 2, 3

#Coleccion (Generico) - Termino general para agrupar datos en Python
#Incluye: Tuplas, lista, diccionarios y conjuntos

#Practica - Calculadora simple

nombre = input("Ingresa tu nombre: ")
calificaciones = []
for i in range(3):
     calificacion = float(input(f"Ingresa la calificaion {i + 1}: "))
     calificaciones.append(calificacion)

promedio = sum(calificaciones)/len(calificaciones)
print("Nombre: ", nombre)
print("Calificaciones: ", calificaciones)
print(f"Promedio: {promedio:.2f}")

if promedio >= 6.0:
     print("Resultado: Aprobado")
else:
     print("Resultado: Reprobo")