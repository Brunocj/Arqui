import socket

SOCK_BUFFER = 1024


if __name__ == "__main__":
    #lineas para iniciar la el servidor y se configura el puerto donde se encuentra este
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_address = ('localhost', 5000)
    print(f"Iniciando servidor en IP {server_address[0]} y puerto {server_address[1]}")

    sock.bind(server_address)

    sock.listen(1)

    while True:
        #Estas lineas permiten que el servidor este siempre activo
        print("Esperando conexiones...")
        conn, client_address = sock.accept()
        print(f"Conexion desde {client_address[0]}:{client_address[1]}")

        try:
            while True:
                data = conn.recv(SOCK_BUFFER) #con esta linea se obtiene la data enviada desde el cliente

                if data:
                    print(f"Recibido {data}")
                    conn.sendall(data)#Respuesta que el servidor le da al cliente
                else:
                    print(f"No hay mas datos")
                    break
        except ConnectionResetError:
            print("el cliente ha cerrado abruptamente la conexion")
        finally:
            print("El cliente ha cerrado la conexion")
            conn.close()