# Basic SSH Honeypot

**A simple SSH honeypot written in Python** – designed to simulate an SSH service, capture authentication attempts, and monitor malicious behavior.  
Created as a 1st semester cybersecurity lab project (2023).

> ⚠️ **Educational Purpose Only** – This honeypot is intended for research and learning. Do not use in production environments or for illegal activities.

---

## 🔧 Technologies & Tools

- **Language:** Python 3.7+  
- **SSH Library:** Paramiko  
- **Logging:** Real‑time daily log files  
- **Shell Simulation:** Restricted Bash (rbash)

---

## 📌 Key Features

- **SSH Authentication Simulation** – Logs both successful and failed login attempts  
- **rbash Shell** – Provides a restricted interactive shell when valid credentials are entered  
- **Real‑Time Logging** – Captures username/password, source IP, timestamp, and executed commands  
- **Daily Log Rotation** – Creates a separate log file for each day (`HONEYPOT-LOGS-YYYY-MM-DD.log`)  
- **Customizable Configuration** – Easily change host, port, and SSH key handling  
- **Automatic RSA Key Generation** – Generates a 2048-bit RSA key pair on first run  

---

## 🚀 How It Works

1. **Start the honeypot** – Listens on `0.0.0.0:2222` (default)  
2. **Attacker connects** – Any SSH client attempting to connect is served by the honeypot  
3. **Authentication** – Predefined credentials (e.g., `kali:kali`, `root:toor`, `guest:guest123`) are accepted  
4. **rbash Shell** – Upon successful login, the attacker gets a restricted Bash shell  
5. **Logging** – All attempts (failed/successful) and commands are logged with timestamps and IP addresses  

---

## ⚙️ Installation & Setup

```bash
# Clone the repository
git clone https://github.com/TheLeopard65/SSH-Honeypot.git
cd SSH-Honeypot

# Install dependency
pip install paramiko

# Run the honeypot
python SSH-HONEYPOT.py
```

> The first execution automatically generates an RSA key (`HONEYPOT-KEY`) in the root directory.

---

## 📂 Log File Example

`HONEYPOT-LOGS-2025-01-09.log` contains entries like:

```
[2025-01-09 14:23:10] Failed login attempt from 192.168.1.100 - Username: admin, Password: 123456
[2025-01-09 14:23:15] Successful login from 192.168.1.100 - Username: kali, Password: kali
[2025-01-09 14:23:22] Command executed: ls -la
```

---

## 📁 Repository

🔗 [github.com/TheLeopard65/basic-ssh-honeypot](https://github.com/TheLeopard65/basic-ssh-honeypot)

---

## 📄 License

MIT License – see the `LICENSE` file for details.

---

## 👤 Author

**@TheLeopard65** – cybersecurity student and penetration testing enthusiast.

---

## 🧠 What I Learned / Showcased

- Implementing a fake SSH server using Paramiko  
- Handling concurrent connections with threading  
- Creating a restricted shell (rbash) to simulate a real environment  
- Logging attack patterns for threat intelligence  
- Understanding how brute‑force attacks work and how honeypots can collect valuable data  

> *This project demonstrates my ability to build security research tools and analyze attacker behavior in a controlled lab environment.*

---
