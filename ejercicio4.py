import random

#Funcion para crear la lista con número aleatorios del 1 al 10
def generar_lista(n, minimo, maximo):
    return [random.randint(minimo, maximo) for _ in range(n)]

#Funcion para sacar el cuadrado y el cubo de la lista random
def Cuadrado_Cubo(lista):
    listCuadrado = []
    listCubo = []
    for num in lista:
        listCuadrado.append(num**2)
        listCubo.append(num**3)
    print("Lista de Cuadrado: ",listCuadrado)
    print("Lista de Cuadrado: ",listCubo)

# Inicializar lista con 10 valores aleatorios entre 1 y 10
lista_numeros = generar_lista(10, 1, 10)
print("Lista de Números: ",lista_numeros)

# Mostrar los valores con sus cuadrados y cubos
Cuadrado_Cubo(lista_numeros)