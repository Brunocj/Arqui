import socket
SOCK_BUFFER = 4


if __name__ == "__main__":
    #Conexion al servidor, direccion "localhost" y puerto 5000
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_address = ('localhost', 5000)

    print(f"Conectando a {server_address[0]}:{server_address[1]}")

    sock.connect(server_address)
    #Una vez se ejecute lo que esta debajo de try, se ejecuta finally, indicando que se ha terminado
    #De ejecutar lo solicitado al servidor. En este caso se envia un mensaje
    try:
        msg = "Hola mundo!"
        sock.sendall(msg.encode("utf-8"))
        data = sock.recv(SOCK_BUFFER)#Linea que recibe la data enviada por el servidor.
        print(f"Recibido {data}") #Imprimir la data recibida
    finally:
        print("Cerrando conexion")
        sock.close()
