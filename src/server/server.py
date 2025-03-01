import socketserver
import re

class SMTPServerHandler(socketserver.BaseRequestHandler):
    def handle(self):
        print(f"Conexión entrante de {self.client_address}")
        self.request.sendall(b"220 Servidor SMTP listo\r\n")
        state = "INIT"
        from_addr = None
        to_addrs = []
        data_buffer = bytearray()  # Acumulador de bytes

        while True:
            data = self.request.recv(1024)
            if not data:
                continue

            # Manejo del estado DATA (bytes)
            if state == "DATA":
                data_buffer.extend(data)
                
                # Buscar terminación "\r\n.\r\n" en bytes
                if b"\r\n.\r\n" in data_buffer:
                    # Dividir en mensaje y resto
                    parts = data_buffer.split(b"\r\n.\r\n", 1)
                    message = parts[0].decode()
                    remaining_data = parts[1] if len(parts) > 1 else b''
                    
                    # Procesar mensaje
                    print("\nCorreo recibido:")
                    print(f"De: {from_addr}")
                    print(f"Para: {', '.join(to_addrs)}")
                    print("Mensaje:\n" + message)
                    self.request.sendall(b"250 Correo recibido\r\n")
                    
                    # Resetear estado
                    data_buffer = bytearray(remaining_data)
                    state = "READY"
                continue

            # Decodificar para comandos SMTP
            decoded_data = data.decode().strip()
            
            if state == "INIT" and decoded_data.startswith("HELO"):
                self.request.sendall(b"250 Hola, bienvenido\r\n")
                state = "READY"
            
            elif state == "READY" and decoded_data.startswith("MAIL FROM:"):
                from_addr = re.search(r'<(.+?)>', decoded_data).group(1)
                self.request.sendall(b"250 Direccion del remitente aceptada\r\n")
                state = "MAIL_FROM"
            
            elif state == "MAIL_FROM" and decoded_data.startswith("RCPT TO:"):
                to_addr = re.search(r'<(.+?)>', decoded_data).group(1)
                to_addrs.append(to_addr)
                self.request.sendall(b"250 Direccion del destinatario aceptada\r\n")
                state = "RCPT_TO"
            
            elif state == "RCPT_TO" and decoded_data == "DATA":
                self.request.sendall(b"354 Envie el mensaje, termine con .\r\n")
                state = "DATA"
            
            elif decoded_data == "QUIT":
                self.request.sendall(b"221 Adios\r\n")
                break
            
            else:
                self.request.sendall(b"500 Comando no reconocido\r\n")

class ThreadedSMTPServer(socketserver.ThreadingMixIn, socketserver.TCPServer):
    pass

if __name__ == "__main__":
    HOST, PORT = "localhost", 25
    with ThreadedSMTPServer((HOST, PORT), SMTPServerHandler) as server:
        print(f"Servidor SMTP escuchando en {HOST}:{PORT}")
        server.serve_forever()