import socket
import time
from threading import Thread
SOCK_BUFFER = 1024
def conn_read():
    with open('PartesDeElectrónica.csv', 'r', encoding ="latin") as f:
        global filas
        contenido = f.read()
        filas = contenido.split("\n")


def enviar_data(conn, filas):
    for i in range(len(filas)-1):
        msg = filas[i+1]
        conn.sendall(msg.encode("utf-8"))
        time.sleep(1)
         
if __name__ == "__main__":
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_address = ('127.0.0.1', 5000)
    sock.bind(server_address)
    sock.listen(1)
  
    while True:
        print("Esperando conexiones...")
        conn, client_address = sock.accept()
        #ejecucion hilos
        t1 = Thread(target = conn_read())
        t2 = Thread(target=enviar_data(conn,filas))
        t1.start()
        t1.join()
        t2.start()
        t2.join()