import random
import time
import statistics
from threading import Thread
from concurrent.futures import ThreadPoolExecutor
from multiprocessing import Pool
from memory_profiler import profile
@profile
def suma_norm(arr_a, arr_b):
    a =  0
    for i in range(len(arr_a)):
        a += (arr_b[i] - arr_a[i])**2
    return a
@profile #->Se usa para ver cuanta memoria ocupa cada linea de codigo al ser ejecutada (de la funcion definida inmediatamente debajo de @profile)
def norm_vec(arr_a, arr_b,):
    a = suma_norm(arr_a, arr_b)
    return a**(0.5)

def crear_vector(size):
    lst = []
    for i in range(size):
        lst.append(random.uniform(0, 10))
    return lst

if __name__ == "__main__":
    
    time_thread = []
    time_sinc = []
    time_process = []
    for i in range(50):
        a = crear_vector(4096)
        b = crear_vector(4096)
        ########################################################################################################################
        tic = time.perf_counter()
        #print(f"Normal serial: {norm_vec(a, b,)}")
        toc = time.perf_counter()
        ########################################################################################################################
        vectores = [(i, i+1024) for i in range(0, 4098, 1024)] #Generar un arreglo de pares de valores limites de los arreglos que van a entrar a las funciones
        with ThreadPoolExecutor(max_workers=4) as executor:
            resp_p_p = [executor.submit(suma_norm, a[min:max], b[min:max]) for min, max in vectores] #Generar un iterable que va a usar los valores minimo y maximo estalbecidos por el arreglo vectores
        res_p = [f.result() for f in resp_p_p]
        #print(f"Normal con threads: {sum(res_p)**(0.5)}")
        toc2 = time.perf_counter()
        ########################################################################################################################
        with Pool(processes= 4) as pool:
            res = pool.starmap(suma_norm, [(a[min:max], b[min:max]) for min, max in vectores])
        #print(f"Normal con procesos: {sum(res)**0.5}")
        toc3 = time.perf_counter()
        ########################################################################################################################
        time_sinc.append(toc-tic)
        time_thread.append(toc2 - toc)
        time_process.append(toc3 - toc2)
    print(f"Mediana serial: {statistics.median(time_sinc)*1e3}ms")
    print(f"Mediana hilos: {statistics.median(time_thread)*1e3}ms")
    print(f"Mediana process: {statistics.median(time_process)*1e3}ms")
    print(f"Speedup hilos: {(statistics.median(time_sinc))/(statistics.median(time_thread))}")
    print(f"Speedup process: {(statistics.median(time_sinc))/(statistics.median(time_process))}")
#mprof run python archivo.py -> genera datos de la memoria usada al correr el archivo
#mprof plot -> plotear el grafico generado

#Lineas de codigo para importar otros archivos que estan en la misma carpeta
#Para el caso del archivo speedup:
#import archivo as archivo_sinc
#import archivo as archivo_threads
#import archivo as archivo_process
#llamando la funcion main de  uno de los archivos importados:
#funcion = archivo_sinc.main(args); preferiblemente, los args serian N (cantidad de iteraciones a medir), los arreglos a usar y la cantidad de trabajadores(para los que usan pool)
#funcion tendra el valor retorno asignado a main en el archivo importado