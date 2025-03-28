import socket

class Client:
    def __init__(self, host="localhost", port=5000):
        self.host = host
        self.port = port
        self.client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    def connect_to_server(self):
        try:
            self.client_socket.connect((self.host, self.port))
            self.start_communication()
        
        except Exception as e:
            print(f"Error conectado con el servidor: {e}")
        
        finally:
            self.client_socket.close()

    def start_communication(self):
        try:
            while True:
                message = input("Escribir mensaje a enviar al servidor  (o 'DESCONEXION' para cerrar conexion ): ")
                self.client_socket.sendall(message.encode('utf-8'))

                if message.strip() == "DESCONEXION":
                    break

                data = self.client_socket.recv(1024)
                print(data.decode('utf-8'))

        except Exception as e:
            print(f"Error durante la comunicacion: {e}")

if __name__ == "__main__":
    client = Client()
    client.connect_to_server()
