# Network File Editor (NFE)

**A sophisticated, multi‑threaded client‑server file management system** that implements four distinct concurrency control models for secure, collaborative file access.  
Built as a C++17 project – allows multiple clients to view, edit, upload, download, and manage files in a shared directory with configurable access policies.

---

## 🔧 Technologies & Tools

- **Language:** C++17  
- **Concurrency:** POSIX threads (`pthread`), mutexes  
- **Networking:** Sockets (TCP)  
- **Build System:** Make  
- **External Libraries:** readline, `rlwrap` (optional for enhanced CLI)  
- **Platform:** Linux/Unix (Kali, Ubuntu, Debian)  

---

## 📌 Key Features

- **Four Concurrency Models** – EREW, CREW, ERCW, CRCW (configurable)  
- **Real‑Time Lock Status** – Detailed reporting of read/write locks and active users  
- **Graceful Failure Handling** – Auto‑cleanup of stale locks on client disconnection  
- **External Editor Integration** – Seamless remote editing with `nano` or `vim`  
- **Thread‑Safe Logging** – Timestamped, color‑coded logs to file and console  
- **Full File Operations** – LIST, VIEW, EDIT, UPLOAD, DOWNLOAD, DELETE, MKDIR, RMDIR, TOUCH  
- **Manual Lock Commands** – `LOCKWRITE` / `UNLOCKWRITE` / `LOCKSTATUS`  
- **Username Authentication** – Input validation and user tracking  

---

## 🚀 How It Works

1. **Server** starts on a chosen port and concurrency model, creating a shared directory.  
2. **Clients** connect using the dedicated `nfe_client` (or `nc` + `rlwrap`).  
3. **Authentication** – each client provides a unique username.  
4. **Commands** – clients issue file operations; the server enforces locking according to the active model.  
5. **Editing** – `EDIT` acquires a write lock, downloads the file, opens local editor, uploads changes, and releases the lock.  
6. **Logging** – all actions are logged with timestamps and user info.

---

## ⚙️ Installation & Setup

```bash
# Install dependencies (Debian/Ubuntu/Kali)
sudo apt install -y build-essential libreadline-dev libpthread-stubs0-dev make nano vim rlwrap

# Clone and build
git clone https://github.com/TheLeopard65/Network-File-Editor.git
cd Network-File-Editor
make clean && make

# Run server (default: port 2121, EREW model, ./share/ directory)
./nfe_server

# Run client (default: localhost:2121)
./nfe_client
```

**Custom server start:**
```bash
./nfe_server -p 3333 -d /path/to/shared -m CREW
```

---

## 📂 Repository

🔗 [github.com/TheLeopard65/Network-File-Editor](https://github.com/TheLeopard65/Network-File-Editor)

---

## 📄 License

MIT License – see `LICENSE` file.

---

## 👤 Author

**@TheLeopard65** – cybersecurity enthusiast and systems programmer.

---

## 🧠 What I Learned / Showcased

- Implementing classical concurrency control models (EREW, CREW, ERCW, CRCW)  
- Multi‑threaded server design with POSIX threads and mutex synchronization  
- Socket programming for reliable TCP communication  
- Graceful handling of client disconnections and stale lock cleanup  
- Integrating external editors into a network application  
- Building a full‑featured CLI with readline support and rich command parsing  
- Logging and monitoring multi‑user file system interactions  

> *This project demonstrates my understanding of concurrent systems, network programming, and collaborative file access control in C++.*

---
