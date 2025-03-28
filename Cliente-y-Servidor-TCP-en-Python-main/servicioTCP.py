import socket

host = "localhost" #Direccion solicitada
port = 5000 #puerto solicitado
buffer_size=1024  #tamaño de datos recibidos y enviados

class ecoserver:
    def __init__(self, host, port, buffer_size):
        self.host = host
        self.port = port
        self.buffer_size=buffer_size
        self.servereco_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    
    def star_servereco(self):
        try:
            self.servereco_socket.bind((self.host,self.port))
            self.servereco_socket.listen(1)

            connection, _= self.servereco_socket.accept()
            self.handle_client(connection)
        except Exception as e:
            print(f"Error tipo {e}")
        finally:
             self.servereco_socket.close()       

    def handle_client(self, client_socket):
        with client_socket:
            try:
                while True:
                    data = client_socket.recv(self.buffer_size)
                    if not data:
                        print("Cliente desconectado")
                        break
                    
                    message = data.decode('utf-8').strip().upper()
                    
                    if message == "DESCONEXION":

                        break
                    client_socket.sendall(message.encode('utf-8'))
            
            except Exception as e:
                print(f"Error handling client: {e}")


if __name__ == "__main__":
    server = ecoserver(host, port, buffer_size)
    server.star_servereco()