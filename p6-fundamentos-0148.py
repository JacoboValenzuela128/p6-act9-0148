# Valenzuela Arath 
# NC:0148

# ==========================================
# 1. VARIABLES EN PYTHON 0148
# ==========================================

# Ejemplo 1: Declaración de variables básicas
nombre = "Ana"
edad = 25
print("1. Variables - Ejemplo 1:")
print(nombre)
print(edad)

# Ejemplo 2: Cambio de tipo dinámico (Casting)
x = 4       # x es de tipo int
x = "Sally" # x ahora pasa a ser de tipo str (cadena)
print("\n1. Variables - Ejemplo 2:")
print(x)

# Ejemplo 3: Obtener el tipo de dato con type()
x = 5
y = "John"
print("\n1. Variables - Ejemplo 3:")
print(type(x))  # <class 'int'>
print(type(y))  # <class 'str'>


# ==========================================
# 2. MÚLTIPLES VARIABLES 0148
# ==========================================

# Ejemplo 1: Asignar muchos valores a múltiples variables
x, y, z = "Naranja", "Banana", "Cereza"
print("\n2. Múltiples Variables - Ejemplo 1:")
print(x, y, z)

# Ejemplo 2: Un mismo valor para múltiples variables
x = y = z = "Manzana"
print("\n2. Múltiples Variables - Ejemplo 2:")
print(x, y, z)

# Ejemplo 3: Desempaquetar una lista (Unpack)
frutas = ["Manzana", "Banana", "Cereza"]
x, y, z = frutas
print("\n2. Múltiples Variables - Ejemplo 3:")
print(x, y, z)


# ==========================================
# 3. TIPOS DE DATOS (DATA TYPES) 0148
# ==========================================

# Ejemplo 1: Tipos numéricos (int, float, complex)
entero = 10
decimal = 10.5
complejo = 1j

print("\n3. Tipos de Datos - Ejemplo 1:")
print(type(entero))    # <class 'int'>
print(type(decimal))   # <class 'float'>
print(type(complejo))  # <class 'complex'>

# Ejemplo 2: Colecciones ordenadas (list, tuple)
mi_lista = ["manzana", "banana", "cereza"] # Modificable (mutable)
mi_tupla = ("manzana", "banana", "cereza") # Inmutable

print("\n3. Tipos de Datos - Ejemplo 2:")
print(type(mi_lista))  # <class 'list'>
print(type(mi_tupla))  # <class 'tuple'>

# Ejemplo 3: Diccionarios (dict) y Mapeo
persona = {"nombre": "Carlos", "edad": 30}
print("\n3. Tipos de Datos - Ejemplo 3:")
print(persona["nombre"]) # Imprime 'Carlos'
print(type(persona))     # <class 'dict'>


# ==========================================
# 4. OPERADORES ARITMÉTICOS 0148
# ==========================================

# Ejemplo 1: Suma (+), Resta (-) y Multiplicación (*)
a = 10
b = 3
print("\n4. Aritméticos - Ejemplo 1:")
print("Suma:", a + b)           # 13
print("Resta:", a - b)          # 7
print("Multiplicación:", a * b) # 30

# Ejemplo 2: División (/), División entera (//) y Módulo (%)
x = 10
y = 3
print("\n4. Aritméticos - Ejemplo 2:")
print("División flotante:", x / y)   # 3.3333...
print("División entera:", x // y)    # 3
print("Módulo (residuo):", x % y)    # 1

# Ejemplo 3: Exponenciación (**)
base = 2
exponente = 5
resultado = base ** exponente  # 2 elevado a la 5
print("\n4. Aritméticos - Ejemplo 3:")
print("Exponenciación:", resultado)  # 32


# ==========================================
# 5. OPERADORES DE COMPARACIÓN 0148
# ==========================================

# Ejemplo 1: Igualdad (==) y Desigualdad (!=)
x = 5
y = 8
print("\n5. Comparación - Ejemplo 1:")
print("¿x es igual a y?:", x == y)     # False
print("¿x es diferente de y?:", x != y) # True

# Ejemplo 2: Mayor que (>) y Menor que (<)
a = 15
b = 20
print("\n5. Comparación - Ejemplo 2:")
print("¿a > b?:", a > b)   # False
print("¿a < b?:", a < b)   # True

# Ejemplo 3: Mayor o igual (>=) y Menor o igual (<=)
edad = 18
print("\n5. Comparación - Ejemplo 3:")
print("¿Es mayor o igual a 18?:", edad >= 18) # True
print("¿Es menor o igual a 17?:", edad <= 17) # False


# ==========================================
# 6. OPERADORES LÓGICOS 0148
# ==========================================

# Ejemplo 1: Operador 'and' (Ambas condiciones deben ser True)
x = 5
print("\n6. Lógicos - Ejemplo 1 (and):")
print(x > 2 and x < 10)  # True

# Ejemplo 2: Operador 'or' (Al menos una condición debe ser True)
x = 5
print("\n6. Lógicos - Ejemplo 2 (or):")
print(x > 10 or x < 6)   # True (porque x < 6 es True)

# Ejemplo 3: Operador 'not' (Invierte el resultado booleano)
x = 5
print("\n6. Lógicos - Ejemplo 3 (not):")
print(not(x > 2 and x < 10))  # False

print("Arath Valenzuela con ML")
print("NC:0148")