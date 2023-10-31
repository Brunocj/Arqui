import socket

SOCK_BUFFER = 1024


if __name__ == "__main__":
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_address = ("127.0.0.1", 5000)
    print(f"Iniciando servidor en IP {server_address[0]}, con puerto {server_address[1]}")
    sock.bind(server_address)
    sock.listen(1)

    while True:
        print("Esperando conexiones...")
        conn, client_address = sock.accept()
        print(f"Conexion desde: {client_address[0]}:{client_address[1]}")

        try:
            data = conn.recv(SOCK_BUFFER).decode('utf-8')
            if data:
                print(f"Recibido: {data}")
                with open("archivo.txt", "+w") as f:
                    f.write(data)
                    f.close()
                end ="Se escribio la data"
                conn.sendall(end.encode('utf-8'))
                break
        except ConnectionResetError:
            print("El cliente ha cerrado la conexion de forma abrupta")
        finally:
            print("El cliente ha cerrado la conexion")
            conn.close()
