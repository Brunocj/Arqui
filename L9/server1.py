import socket
SOCK_BUFFER = 1024
if __name__ == "__main__":
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_address = ('127.0.0.1', 12345)
    print(f"Servidor de chat escuchando en {server_address[0]}:{server_address[1]}")
    sock.bind(server_address)
    sock.listen(1)
    conn, client_address = sock.accept()
    print(f"Conexion entrante desde ('{client_address[0]}', {client_address[1]})")
    try:
        inicio = 0
        while True:

            if inicio == 0:
                data = conn.recv(SOCK_BUFFER)
                data = data.decode("utf-8")
                inicio = 'start'
                d_str = str(data)
                if (d_str == inicio):
                    palabra = "servidor"
                    print(f"Recibi comando start\nPalabra elegida: {palabra}")
                    inicio = 1
                    msg = ''
                    for _ in range(len(palabra)):
                        msg += '*'

                else:
                    msg = "Ingrese el comando para iniciar el juego"
                conn.sendall(msg.encode("utf-8")) 
            else:
                msg_lst = list(msg)
                data = conn.recv(SOCK_BUFFER)
                data = data.decode("utf-8")
                data = str(data)
                if data == "s":
                    msg_lst[0] = data
                elif data == "e":
                    msg_lst[1] = data
                elif data == "r":
                    msg_lst[2] = data
                    msg_lst[7] = data
                elif data == "v":
                    msg_lst[3] = data
                elif data == "i":
                    msg_lst[4] = data
                elif data == "d":
                    msg_lst[5] = data
                elif data == "o":
                    msg_lst[6] = data
                msg = "".join(msg_lst)
                conn.sendall(msg.encode("utf-8")) 
    finally:    
        conn.close()
        