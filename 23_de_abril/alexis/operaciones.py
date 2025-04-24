'''crear las funciones suma resta multiplicacion,division, division piso
crear una función que genere un numero aleatorio(impor random)
crear una función módulo
'''
import random

def sumar(a,b):
    return a+b

def restar(a,b):
    return a-b

def multiplicar(a,b):
    return a*b

def dividir(a,b):
    if b == 0:
        return "Error: División por cero"
    return a/b

def División_piso(a,b):
    return(a // b)

def Módulo (a,b):
    return(a%b)

def numero_aleatorio():
    return round(random.random(),2)


