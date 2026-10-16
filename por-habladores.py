# Parte 1
# Escribir un programa que pida dos números y muestre su suma, resta,
# multiplicación y división.
# - Pedir los dos números con input() y convertirlos con float().
# - Mostrar las cuatro operaciones con f-strings (ejemplo: 5.0 + 3.0 = 8.0).
# - Si el segundo número es 0, en lugar de dividir mostrar
#   "No se puede dividir entre cero".
# - Pregunta: ¿qué imprime input("a: ") + input("b: ") si escribes 5 y 3?
#   ¿Por qué?
a = float(input("Primer número: "))
b = float(input("Segundo número: "))
print(f"{a} + {b} = {a + b}")
print(f"{a} - {b} = {a - b}")
print(f"{a} * {b} = {a * b}")
if b == 0:
    print("No se puede dividir entre cero")
else:
    print(f"{a} / {b} = {a / b}")


# Parte 2
# Resolver cada ejercicio dos veces: con for + if (imperativo) y en una sola
# línea con sum() (funcional). Ambas versiones deben dar el mismo resultado.
# Usar la lista numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# 1. Predicción (sin ejecutar): qué imprime
#    print(sum(n ** 2 for n in nums if n % 2 == 0)) con nums = [1, 2, 3, 4, 5]
# 2. Sumar solo los números impares de numeros.
# 3. Sumar el cubo (n ** 3) de los múltiplos de 3.
# 4. Contar cuántos números son mayores que 5 (funcional: sum(1 for ...)).
# 5. Modificar el ejercicio 2 para que la lista la escriba el usuario,
#    separada por comas (ejemplo: 4,7,10,13).
# Completar la tabla de resultados (imperativo, funcional, ¿coinciden?).
numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

nums = [1, 2, 3, 4, 5]
print(sum(n ** 2 for n in nums if n % 2 == 0))

total = 0
for n in numeros:
    if n % 2 != 0:
        total += n
print(total)
print(sum(n for n in numeros if n % 2 != 0))

total = 0
for n in numeros:
    if n % 3 == 0:
        total += n ** 3
print(total)
print(sum(n ** 3 for n in numeros if n % 3 == 0))

contador = 0
for n in numeros:
    if n > 5:
        contador += 1
print(contador)
print(sum(1 for n in numeros if n > 5))

lista_usuario = [int(x) for x in input("Escribe números separados por comas: ").split(",")]
total = 0
for n in lista_usuario:
    if n % 2 != 0:
        total += n
print(total)
print(sum(n for n in lista_usuario if n % 2 != 0))


# Parte 3
# En Python una función es un dato: se guarda en variables, se pasa como
# argumento y se retorna desde otra función. Partir del código base
# (aplicar y crear_multiplicador).
# 1. Crear despedir(nombre) que retorne "Adiós <nombre>", guardarla en una
#    variable g y llamarla con g("Ana"). Explicar por qué se escribe
#    g = despedir y no g = despedir().
# 2. Usar aplicar con tres funciones: str.upper con "python", abs con -7 y
#    cuadrado con 4 (cuadrado la escribe el estudiante).
# 3. Escribir crear_sumador(n) que retorne una función que le suma n a su
#    argumento. Crear sumar10 = crear_sumador(10) y probar sumar10(5).
# 4. Crear doble y triple con crear_multiplicador, guardarlas junto con
#    cuadrado en una lista y aplicarlas todas al número 4 con un for.
#    Salida esperada: 8, 12, 16.
def aplicar(funcion, valor):
    return funcion(valor)


def crear_multiplicador(factor):
    def multiplicar(x):
        return x * factor
    return multiplicar


def despedir(nombre):
    return f"Adiós {nombre}"


g = despedir
print(g("Ana"))


def cuadrado(x):
    return x ** 2


print(aplicar(str.upper, "python"))
print(aplicar(abs, -7))
print(aplicar(cuadrado, 4))


def crear_sumador(n):
    def sumar(x):
        return x + n
    return sumar


sumar10 = crear_sumador(10)
print(sumar10(5))

doble = crear_multiplicador(2)
triple = crear_multiplicador(3)
funciones = [doble, triple, cuadrado]
for f in funciones:
    print(f(4))


# Parte 4
# Construir una mini calculadora que guarde sus operaciones en un
# diccionario de funciones, sin usar if para elegir la operación.
# 1. Definir sumar(a, b), restar(a, b), multiplicar(a, b) y dividir(a, b).
# 2. Guardarlas en operaciones = {"+": sumar, "-": restar,
#    "*": multiplicar, "/": dividir}.
# 3. Pedir al usuario dos números y un operador. Si escribe algo que no es
#    número, volver a pedirlo (try / except ValueError).
# 4. Buscar la función en el diccionario y ejecutarla:
#    operaciones[operador](a, b).
# 5. Si el operador no existe en el diccionario, mostrar "Operador no válido".
def sumar(a, b):
    return a + b


def restar(a, b):
    return a - b


def multiplicar(a, b):
    return a * b


def dividir(a, b):
    return a / b


operaciones = {"+": sumar, "-": restar, "*": multiplicar, "/": dividir}


def pedir_numero(mensaje):
    while True:
        try:
            return float(input(mensaje))
        except ValueError:
            print("Eso no es un número válido, intenta de nuevo.")


a = pedir_numero("Primer número: ")
b = pedir_numero("Segundo número: ")
operador = input("Operador (+ - * /): ")

if operador in operaciones:
    try:
        print(f"{a} {operador} {b} = {operaciones[operador](a, b)}")
    except ZeroDivisionError:
        print("No se puede dividir entre cero")
else:
    print("Operador no válido")
