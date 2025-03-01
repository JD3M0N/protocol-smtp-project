# protocol-smtp-project


# SMTP Client-Server Implementation 📧

A Python-based implementation of an SMTP (Simple Mail Transfer Protocol) client and server, compliant with RFC 5321 and RFC 5322. This project allows users to send emails via a command-line interface (CLI) or a graphical user interface (GUI), with a concurrent server handling multiple connections.



## Features ✨

- **SMTP Client**:
  - Send emails via CLI or GUI.
  - Supports multiple recipients.
  - Validation of email formats and command sequences.
- **SMTP Server**:
  - Concurrent handling of multiple clients using multithreading.
  - Compliant with SMTP command flow (HELO, MAIL FROM, RCPT TO, DATA, QUIT).
  - Logs received emails to the console.
- **User Interfaces**:
  - **CLI**: Lightweight console interface for quick email sending.
  - **GUI**: Intuitive Tkinter-based interface with real-time feedback.

---

## Prerequisites 📋

- Python 3.8+.
- Libraries: `socketserver` (built-in), `tkinter` (built-in for GUI).

---

## Installation & Usage 🚀

### 1. Clone the Repository
```bash
git clone https://github.com/your-username/smtp-project.git
cd smtp-project
```

### 2. Start the SMTP Server
```bash
python src/server/server.py
```
**Output**:  
```
Servidor SMTP escuchando en localhost:25
```

### 3. Run the Client
#### CLI Client:
```bash
python src/client/cli.py
```
Follow the prompts to send an email.

#### GUI Client:
```bash
python src/client/gui.py
```
![GUI Preview](https://i.imgur.com/xyZ1FQk.png)

---

## Project Structure 📂
```
smtp-project/
├── src/
│   ├── client/               # Client-side code
│   │   ├── cli.py            # CLI interface
│   │   ├── gui.py            # GUI interface
│   │   └── smtp_client.py    # SMTP client logic
│   └── server/               # Server-side code
│       └── server.py         # SMTP server logic
├── tests/                    # Unit and integration tests
├── docs/                     # RFC summaries and documentation
└── README.md                 # Project overview
```

---

## Technical Specifications ⚙️
### Key RFCs Implemented
- **RFC 5321**: SMTP protocol commands and flow.
- **RFC 5322**: Email message format (headers and body).

### Error Handling
- Client: Validates email formats and command sequences.
- Server: Returns RFC-compliant response codes (e.g., `250 OK`, `500 Invalid Command`).

---

## Future Enhancements 🔮
- [ ] **Email Authentication**: Support for `AUTH LOGIN` (RFC 4954).
- [ ] **TLS Encryption**: Implement STARTTLS (RFC 3207).
- [ ] **Attachment Support**: MIME integration (RFC 2045).
- [ ] **Persistent Storage**: Save emails to a database or file system.

---

## Contributing 🤝
Contributions are welcome! Please fork the repository and submit a pull request. Ensure your code adheres to PEP8 standards and includes relevant tests.

---

## License 📄
This project is licensed under the MIT License. See [LICENSE](LICENSE) for details.

---

**Developed with ❤️ by Josue R. Naranjo Sieiro**  
