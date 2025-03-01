import tkinter as tk
from tkinter import messagebox
from smtp_client import SMTPClient

class SMTPClientGUI:
    def __init__(self, root):
        self.root = root
        root.title("Cliente SMTP")
        
        # Campos de entrada
        self.from_entry = self._create_field("De:", 0)
        self.to_entry = self._create_field("Para (separar con comas):", 1)
        self.subject_entry = self._create_field("Asunto:", 2)
        self.body_text = tk.Text(root, height=10, width=40)
        self.body_text.grid(row=3, column=1, padx=10, pady=5)
        
        # Botón de envío
        self.send_btn = tk.Button(root, text="Enviar", command=self.send_email)
        self.send_btn.grid(row=4, column=1, pady=10)
        
        # Etiqueta de estado
        self.status_label = tk.Label(root, text="", fg="grey")
        self.status_label.grid(row=5, column=1)

    def _create_field(self, label, row):
        tk.Label(self.root, text=label).grid(row=row, column=0, sticky="e", padx=10)
        entry = tk.Entry(self.root, width=40)
        entry.grid(row=row, column=1, padx=10, pady=5)
        return entry

    def send_email(self):
        # Obtener datos de los campos
        from_addr = self.from_entry.get().strip()
        to_addrs = [addr.strip() for addr in self.to_entry.get().split(",")]
        subject = self.subject_entry.get()
        body = self.body_text.get("1.0", tk.END).strip()

        # Validar campos vacíos
        if not all([from_addr, to_addrs, subject, body]):
            messagebox.showerror("Error", "Todos los campos son obligatorios")
            return

        # Configuración del servidor (puedes agregar campos para esto si es necesario)
        server = "localhost"
        port = 25

        # Enviar correo
        try:
            client = SMTPClient(server, port)
            client.connect()
            client.send_email(from_addr, to_addrs, subject, body)
            self.status_label.config(text="Correo enviado ✅", fg="green")
        except Exception as e:
            messagebox.showerror("Error", f"Falló el envío: {str(e)}")
            self.status_label.config(text="Error ❌", fg="red")
        finally:
            client.close()

if __name__ == "__main__":
    root = tk.Tk()
    app = SMTPClientGUI(root)
    root.mainloop()