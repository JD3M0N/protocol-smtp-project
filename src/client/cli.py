# src/client/cli.py
from smtp_client import SMTPClient 

def main():
    print("=== Cliente SMTP ===")
    server = input("Servidor SMTP (ej: localhost): ")
    port = int(input("Puerto (ej: 25): "))
    from_addr = input("De: ")
    to_addrs = input("Para (separar con comas): ").split(',')
    subject = input("Asunto: ")
    body = input("Cuerpo del mensaje: ")

    client = SMTPClient(server, port)
    try:
        client.connect()
        client.send_email(from_addr, to_addrs, subject, body)
        print("Correo enviado exitosamente!")
    except Exception as e:
        print(f"Error: {str(e)}")
    finally:
        client.close()

if __name__ == "__main__":
    main()