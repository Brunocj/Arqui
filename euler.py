# Euler
import numpy as np
import time
import statistics
import matplotlib.pyplot as plt
import ctypes

def euler (x):
    return pow((1+1/x),x)

if __name__ == '__main__':
    N = 10000
    lib = ctypes.CDLL('./lib_euler.so')
    lib.euler.argtypes = [ctypes.c_int] #Declaracion de los tipos de datos de las entradas de la funcion euler dentro de lib_euler
    lib.euler.restype = ctypes.c_double #Declaracion de los tipos de datos de la salida de euler
    iteraciones = 100
    
    time_python = []
    time_c = []
    for _ in range(iteraciones):
        tic2 = time.perf_counter()
        lib.euler(N)
        toc2 = time.perf_counter()
        time_c.append(1e6*(toc2-tic2))
        # print("Tiempo Pow en C",toc2-tic2)

        tic1 = time.perf_counter()
        euler(N)
        toc1 = time.perf_counter()
        time_python.append(1e6*(toc1-tic1))
        #print("Tiempo pow Python",toc1-tic1)
    print("Mediana en python:",statistics.median(time_python))
    print("Mediana en c:",statistics.median(time_c))
    
    plt.plot(time_python)
    plt.plot(time_c)
    plt.grid()
    plt.legend(["Time Python", "Time C"])
    plt.xlabel("Iteraciones")
    plt.ylabel("Tiempo [us]")
    plt.savefig("Euler_comparacion2.png")
    plt.close()
     #gcc fPIC -shared lib_euler.c -o lib_euler.so
     #linea para compilar lib_euler.c y que se genere el .so que se usa en python con la libreria ctypes