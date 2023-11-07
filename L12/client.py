import socket

from threading import Thread
SOCK_BUFFER = 1024
def recuperacion_data(sock):
    global data
    data = sock.recv(SOCK_BUFFER)
    data = data.decode("utf-8")
def procesamiento_data(data):
    global costo_bajo, costo_elevado, pesado
    data_l = data.split(";")
    nombre = data_l[1]
    cantidad = float(data_l[3])
    peso = float(data_l[4])
    costo = float(data_l[5])
    costo_total = cantidad*costo
    if costo_total<25:
        clas_costo = "Costo bajo"
        costo_bajo +=1
    elif costo_total>=25 and costo_total<50:
        clas_costo = "Costo regular"   
    elif costo_total>=50 and costo_total<74.9:
        clas_costo = "Costo alto"
    elif costo_total>=75:
        clas_costo = "Costo elevado"
        costo_elevado +=1
        if peso>100:
            pesado +=1
    print("----------------Nombre: ", nombre, "----------------")
    print("Costo total: ", costo_total)
    print("Clasificación por costo: ", clas_costo)
    print("Numero de componentes con costo bajo: ", costo_bajo)
    print("Numero de componentes con costo elevado y peso mayor a 100g: ", pesado)
    print("Numero de componentes con costo elevado: ", costo_elevado)
    
if __name__ == "__main__":
    #Conexion al servidor, direccion "localhost" y puerto 5000
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_address = ('127.0.0.1', 5000)

    print(f"Conectando a {server_address[0]}:{server_address[1]}")

    sock.connect(server_address)
    costo_elevado= 0
    costo_bajo = 0
    pesado = 0
    try:
        while True:
            t1  = Thread(recuperacion_data(sock))
            t2 = Thread(procesamiento_data(data))
            
            t1.start()
            t1.join()
            t2.start()
            t2.join()
    finally:
        print("Cerrando conexion")
        sock.close()
