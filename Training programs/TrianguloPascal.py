import time # Importa la libreria para medir el tiempo de ejecución

def trianguloPascal(arg):
    filas = [1] # Almacena la secuencia de cada fila
    valor = arg # n filas
    
    tabs = "\t".expandtabs(valor + 1)
    print("{}{}".format(tabs, filas)) # tabs en las filas para que se vea en forma de triangulo
    
    tInicial = time.time()  # Guardamos el tiempo de inicio
    
    for i in range(1, arg):
        long = len(filas) # long de la lista de filas
        fila = [1] # new list con valor inicial de 1
        for x in range(0, long-1):
            calc = filas[x] + filas[x+1] # hacemos el calculo para la siguiente fila
            fila.append(calc) # agregamos el resultado a la nueva fila
        fila.append(1) # cerramos lista con valor de 1
        tabs = "\t".expandtabs(valor)  # agregamos los tabs en la tabla para que se imprima en forma de triangulo
        valor -= 1 # decremento por 1 por cada fila del triangulo
        print("{}{}".format(tabs, fila))
        filas = fila
    
    tFinal = time.time()  # Guardamos el tiempo de finalización
    tTranscurrido = tFinal - tInicial  # Calculamos el tiempo transcurrido
    print(f"\n", "Tiempo de ejecución: ", tTranscurrido, " segundos", "\n") # Imprime el tiempo

print("Ingresa un numero de filas para el triangulo de pascal: ", end=" ") # Imprime el triangulo de Pascal
n = int(input())
trianguloPascal(n) # El valor que vamos a ingresar desde el menú para el triangulo de pascal
