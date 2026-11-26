def validar_numeros(a, b):
    if not isinstance(a, (int, float)) or not isinstance(b, (int, float)):
        raise TypeError("Los argumentos deben ser valores numéricos")

def sumar(a, b):
    validar_numeros(a, b)
    return a + b

def restar(a, b):
    validar_numeros(a, b)
    return a - b

def multiplicar(a, b):
    validar_numeros(a, b)
    return a * b

def dividir(a, b):
    validar_numeros(a, b)
    if b == 0:
        raise ValueError("No se puede dividir entre cero")
    return a / b