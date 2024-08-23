```python
#Ejercicio 1
#Eleva todos los elementos de la lista al cuadrado.
ejer_2 = [1, 2, 3, 4, 5]
cuadrado = [x**2 for x in ejer_2]
print(cuadrado)
###

ejer_2 = [1,2,3,4,5]
cuadrado = [x**2 for x in ejer_2]


####
ejer_2 = [1,2,3,4,5]
cuadrado = [x**2 for x in ejer_2]
###
ejer_2 = [1,2,3,4,5]
cuadrado = [x**2 for x in ejer_2]
```


```python
#Ejercicio 2
#Haz un programa que detecte todos los duplicados de un elemento en una lista:
#•	Utiliza una variable duplicado para asignarle el valor del elemento del que queremos encontrar todos sus duplicados.
#•	El programa debe devolver todos los índices de los elementos duplicados.
#•	Aplícalo para encontrar los duplicados de "un", "es", y "binario" en la lista:
#ejer_3 = ["Un", "árbol", "binario", "es", "una", "estructura", "de", "un", "tipo", "particular", "a", "veces", "no", "es", "ni", "binario"]


ejer_3 = ["Un", "árbol", "binario", "es", "una", "estructura", "de", "un", "tipo", "particular", "a", "veces", "no", "es", "ni", "binario"]

def encontrar_lista_duplicado(lista, duplicado):
indices = []
    for i, elemento in enumerate(lista):
        if elemento.lower() == duplicado.lower():  # Comparación sin distinguir entre mayúsculas y minúsculas
            indices.append(i)
    return indices

# Encontrar los duplicados de "un", "es", y "binario"
duplicados_un = encontrar_duplicados(ejer_3, "un")
duplicados_es = encontrar_duplicados(ejer_3, "es")
duplicados_binario = encontrar_duplicados(ejer_3, "binario")

# Mostrar los resultados
print("Índices de 'un':", duplicados_un)
print("Índices de 'es':", duplicados_es)
print("Índices de 'binario':", duplicados_binario)
```


```python
ejer_3 = ["Un", "árbol", "binario", "es", "una", "estructura", "de", "un", "tipo", "particular", "a", "veces", "no", "es", "ni", "binario"]

def encontrar_lista_duplicados(lista, duplicados):
    indices = []
    for i, elementos in enumerate(lista):
        if elemento.lower == duplicate.lower
        print indices(i)

duplicados_un = encontrar_duplicados(ejer_3, "un")
duplicados_es = encontrar_duplicados(ejer_3, "es")
duplicados_binario = encontrar_duplicados(ejer_3, "binario")
```


```python
#¿Cuántas veces se repite el número 3 en la siguiente tupla?
#Crea una tupla nueva con los elementos desde la posición 5 a la 10.
#¿Cuántos elementos tiene la tupla ejer_3?
#ejer_9 = (3, 20, 3, 47, 19, 3, 29, 45, 67, 78, 90, 3, 3, 5, 2, 4, 7, 9, 4, 2, 4, 3, 3, 4, 6, 7)

ejer_9 = (3, 20, 3, 47, 19, 3, 29, 45, 67, 78, 90, 3, 3, 5, 2, 4, 7, 9, 4, 2, 4, 3, 3, 4, 6, 7)
repeated_3 = ejer_9.count(3)
nueva_tupla = ejer_9[5:10]
cantidad_de_elementos = len(ejer_9)
###
repeated_3 = ejer_9.count(3)
nueva_tupla = ejer_9[5:10]
cantidad_de_elementos = len(ejer_9)

###
repeated_3 = ejer_9.count(3)
nueva_tupla = ejer_9[5:11]
cantidad_de_elementos = len(ejer_9)
print("the number of repeated threes is", repeated 3)
print("the number of elementos from 5 to 11 is", nueva_tupla)
```


```python
#Ejercicio 4
#Comprueba si el número 60 está en la tupla del ejercicio 3.
ejer_9 = (3, 20, 3, 47, 19, 3, 29, 45, 67, 78, 90, 3, 3, 5, 2, 4, 7, 9, 4, 2, 4, 3, 3, 4, 6, 7)

if 60 in ejer_9:
    print(60, "is in the list")
else:
    print(60, "is not in the list")

```


```python
#Ejercicio 5
#1.	Convierte la tupla del ejercicio 3 en una lista.
#2.	Convierte la tupla del ejercicio 3 en un set.
#3.	Convierte la tupla del ejercicio 3 en un diccionario, usando también los índices.

ejer_9 = (3, 20, 3, 47, 19, 3, 29, 45, 67, 78, 90, 3, 3, 5, 2, 4, 7, 9, 4, 2, 4, 3, 3, 4, 6, 7)
lista_ejer_9 = list(ejer_9)
print(lista_ejer_9, "convertido a lista")
set_ejer_9 = set(ejer_9)
print(set_ejer_9, "convertido en set")


# Conversión de tupla a diccionario usando los índices como claves
diccionario = {i: ejer_9[i] for i in range(len(ejer_9))}

diccionario = {i: ejer_9[i] for i in range(len(ejer_9))}

diccionario = {i: ejer_9[i] for i in range(len(ejer_9))}

```


```python
#Ejercicio 6
ejer_6 = {1: 11, 2: 22, 3: 33, 4: 44, 5: 55}

resultado = 1
for valor in ejer_6.values():
    resultado *= valor

print("El resultado de multiplicar todos los valores es:", resultado)
```


```python
#Ejercicio 7
#1.	Crea un diccionario que describa un libro, con los siguientes campos o claves: "título", "autor", "idioma original", "año de publicación".
#2.	Crea una lista llamada librería.
#3.	Añade cuatro libros de tu elección a la librería.

libro1 = {
    "título": "Cien años de soledad",
    "autor": "Gabriel García Márquez",
    "idioma original": "Español",
    "año de publicación": 1967
}

libreria[]

libreria.append(libro1)

Libro2={
    "título": "Don Quijote de la Mancha",
    "autor": "Miguel de Cervantes",
    "idioma original": "Español",
    "año de publicación": 1605
}
libreria.append(libro2)

libro3 = {
    "título": "1984",
    "autor": "George Orwell",
    "idioma original": "Inglés",
    "año de publicación": 1949
}
librería.append(libro3)
```


```python
#Modifica los valores del idioma de todos los libros del ejercicio anterior para que sea "esperanto".

for libro in libreria("titulo", "idioma", "ano de publicacion"):
    libro("idioma") = "Esperanto"
    for libro in libreria:
        print(libro)

##
for libro in libreria("titulo", "idioma", "ano de publicacion"):
    libro("idioma") = "Esperanto"
    for libro in libreria:
        print(libro)
```


```python
#Ejercicio 9
#1.	Escribe un programa que, dada una variable titulo, busque los libros que hay en la librería con ese título. Si no se encuentra, debe devolver el mensaje Ese no lo tengo, ¿mola?.
#2.	Prueba el programa con uno de tus libros y con otro que no contenga tu librería.

librería = [
    {"título": "1984", "autor": "George Orwell", "idioma original": "inglés", "año de publicación": 1949},
    {"título": "Cien años de soledad", "autor": "Gabriel García Márquez", "idioma original": "español", "año de publicación": 1967},
    {"título": "El principito", "autor": "Antoine de Saint-Exupéry", "idioma original": "francés", "año de publicación": 1943},
    {"título": "Fahrenheit 451", "autor": "Ray Bradbury", "idioma original": "inglés", "año de publicación": 1953}
]

# Función para buscar un libro por título
def buscar_libro(titulo):
    for libro in librería:
        if libro["título"].lower() == titulo.lower():
            return libro
    return "Ese no lo tengo, ¿mola?"SS

# Prueba con un título que existe en la librería
titulo_a_buscar = "1984"
resultado = buscar_libro(titulo_a_buscar)
print(resultado)

# Prueba con un título que no existe en la librería
titulo_a_buscar = "Harry Potter"
resultado = buscar_libro(titulo_a_buscar)
print(resultado)
###

def buscar_libro(titulo):
    for libro in libreria:
        if libro["titulo"].lower == titulo.lower:
            return libro
        else:
             return "ese no lo tengo, mola?"

#Prueba con un titulo que no existe
titulo_a_buscar = "El Principito"
resultado = buscar_libro(titulo_a_buscar)
```


```python
#Ejercicio 10
#Convierte el programa del ejercicio 2 en una función al que se le pase el valor a buscar como un argumento posicional.

ejer_3 = ["Un", "árbol", "binario", "es", "una", "estructura", "de", "un", "tipo", "particular", "a", "veces", "no", "es", "ni", "binario"]


def encontrar_duplicados(lista, valor):
    indices = []
    for i, valor in enumerate(lista):
        if valor.lower() == valor_a_buscar.lower():
            indices.append(i)
    return indices

# Ejemplos de uso de la función
resultado_un = encontrar_duplicados(ejer_3, "un")
resultado_es = encontrar_duplicados(ejer_3, "es")
resultado_binario = encontrar_duplicados(ejer_3, "binario")

print("Indices para 'un':", resultado_un)
print("Indices para 'es':", resultado_es)
print("Indices para 'binario':", resultado_binario)


##
def encontrar_duplicados(lista, valor):
    indices = []
    for i in enumerate(lista)
```


```python
#Ejercicio 11
#Convierte el programa del ejercicio 9 en una función a la que se le pasen como argumentos la librería (posicional) y el título (argumento keyword con valor "ninguno" por defecto).

def buscar_libro_en_libreria(libreria, titulo:"ninguno"):
    for libro in libreria:
        if libro["titulo"].lower == titulo.lower:
        return "el libro", libro, "esta en la libreria:
else:
return "el libro", libro, "no esta en la libreria"

```


```python
# Ejercicio 12 - Solicita al usuario que ingrese su dirección de email. 
#Imprime un mensaje indicando si la dirección es válida o no, valiéndose de una función para decidirlo.
#Una dirección se considerará válida si contiene el símbolo "@".

def validar_email(email):
    if "@" in email:
        return "La dirección de email es válida."
    else:
        return "La dirección de email no es válida."

# Solicita al usuario que ingrese su dirección de email
email_usuario = input("Por favor, ingresa tu dirección de email: ")

# Llama a la función y muestra el resultado
resultado = validar_email(email_usuario)
print(resultado)
```


```python
#Ejercicio 13
#Escribe una función que compruebe si un DNI es válido, devolviendo True en caso afirmativo.
#•	El DNI debe tener entre 7 y 8 dígitos numéricos.
#•	Para saber si la letra del DNI es correcta, usa el siguiente fragmento de código:
#python
#DNI = 55555555
#palabra = 'TRWAGMYFPDXBNJZSQVHLCKE

def validar_dni(dni):
    # Asegurarse de que el DNI tiene entre 7 y 8 dígitos
    if len(dni) < 7 or len(dni) > 8 or not dni.isdigit():
        return False

def validar_dni(dni):
    
 # Calcular la letra correcta del DNI
    dni_numero = int(dni)
    palabra = 'TRWAGMYFPDXBNJZSQVHLCKE'
    letra_correcta = palabra[dni_numero % 23]

    # Pedir al usuario que ingrese la letra de su DNI
    letra_dni = input("Introduce la letra de tu DNI: ").upper()

    # Comprobar si la letra es correcta
    return letra_correcta == letra_dni

# Solicitar al usuario que introduzca su DNI
dni_usuario = input("Introduce los dígitos de tu DNI (sin la letra): ")

# Validar el DNI
if validar_dni(dni_usuario):
    print("El DNI es válido.")
else:
    print("El DNI no es válido.")

```
