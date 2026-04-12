# FIXER Botnet

**A simple botnet management system** built for educational and research purposes.  
This project demonstrates remote administration techniques, client-server architecture, and various post-exploitation capabilities.

> ⚠️ **Disclaimer:** I am not in any way responsible for any damages caused by this Project.  
> This tool is intended for authorized security testing and learning only.

---

## 🔧 Technologies & Tools

- **Backend:** Python, Flask-SocketIO, Python-SocketIO  
- **Frontend:** Flask (web dashboard)  
- **Client-Server Communication:** WebSockets  
- **Keylogging & Persistence:** Windows-specific libraries (`winreg`)  
- **Payload Generation:** Python to EXE conversion  

---

## 📌 Key Features

- **Authentication** – Secure login with predefined credentials (`admin` / `admin9876`)
- **Live Dashboard** – Overview of connected clients and their status
- **Remote Command Execution** – Run system commands on connected clients
- **Keylogger** – Capture keystrokes and save logs locally
- **Persistence** – Add botnet to Windows startup programs
- **Screenshot Capture** – Take and retrieve screenshots from client desktops
- **Webcam Picture & Audio Recording** – Capture media from client devices
- **DDoS PING-OF-DEATH** – Launch network stress tests against a target IP
- **Bi-Directional File Transfer** – Exchange files between server and clients
- **Payload Generator** – Create `.exe` and non-executable payloads

---

## 🚀 How It Works

1. **Server** (`Server.py`) – Hosts the web dashboard and listens for client connections.
2. **Client** (`Client.py`) – Runs on remote machines and connects back to the server.
3. **Web Interface** – Login at `http://server_ip:8000/login.html` and send commands to any connected client.
4. **Results** – Screenshots, keylogs, and transferred files are saved in respective folders on the server.

---

## ⚙️ Installation (Windows)

```bash
git clone https://github.com/TheLeopard65/fixer-botnet.git
cd fixer-botnet-main
pip install -r requirements.txt
python Server.py   # start the server
python Client.py   # run on client machine
```

> **Note:** This project may not work on Linux due to the `winreg` dependency in the persistence module.

---

## 📂 Repository

🔗 [github.com/TheLeopard65/fixer-botnet](https://github.com/TheLeopard65/fixer-botnet)

---

## 👤 Author

Created by **@TheLeopard65** – cybersecurity enthusiast and penetration testing learner.

---

## 🧠 What I Learned / Showcased

- Real-time client-server communication using WebSockets  
- Implementing remote administration features ethically  
- Packaging Python scripts into standalone executables  
- Handling file transfers and multimedia capture programmatically  
- Building a simple but functional web dashboard for botnet control  

> *This project is part of my offensive security portfolio and demonstrates my understanding of Python, networking, and Windows internals.*

---
