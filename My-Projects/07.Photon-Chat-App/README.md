# Photon Live Chat Application

**A secure, real‑time chat application** built with Qt and OpenSSL, designed to ensure privacy through robust end‑to‑end encryption. Supports multi‑client connections, persistent chat history, and a modern cross‑platform GUI.

---

## 🔧 Technologies & Tools

- **Framework:** Qt 5.15+ (Core, Network, Widgets)  
- **Cryptography:** OpenSSL 1.1.1+ (AES‑128‑CBC)  
- **Languages:** C++  
- **Protocol:** Custom TCP‑based encrypted messaging  
- **Platforms:** Windows, Linux, macOS  

---

## 📌 Key Features

- **End‑to‑End Encryption** – AES‑128‑CBC with random IV per message  
- **Multi‑Client Support** – Server handles concurrent connections via dedicated threads  
- **Persistent Chat History** – New clients receive previous messages on join  
- **Modern GUI** – Clean interface with connection status indicators  
- **Cross‑Platform** – Runs on Windows, Linux, and macOS  
- **Secure Message Format** – IV + ciphertext transmitted over TCP  

---

## 🚀 How It Works

1. **Server** listens on port `7986` for incoming connections.  
2. **Client** connects using server IP and a chosen nickname.  
3. **Messages** are encrypted (AES‑128‑CBC) before transmission.  
4. **Server** broadcasts encrypted messages to all connected clients.  
5. **New clients** receive the chat history upon joining.  
6. Each client connection runs in its own `QThread` for concurrency.

---

## ⚙️ Installation & Usage

```bash
# Clone repository
git clone https://github.com/TheLeopard65/Photon-Live-Chat-App.git
cd Photon-Live-Chat-App

# Run the install script (builds both server and client)
./install.sh

# Start the server
./Server

# Start a client (in another terminal)
./Client
```

**Client setup:**
1. Enter server IP address (e.g., `127.0.0.1` for localhost)  
2. Choose a nickname  
3. Click `CONNECT`  
4. Start chatting securely!

---

## 📂 Repository

🔗 [github.com/TheLeopard65/Photon-Live-Chat-App](https://github.com/TheLeopard65/Photon-Live-Chat-App)

---

## 📄 License

MIT License – see `LICENSE` file.

---

## 👤 Author

**@TheLeopard65** – cybersecurity enthusiast and C++/Qt developer.

---

## 🧠 What I Learned / Showcased

- Implementing symmetric encryption (AES‑128‑CBC) with OpenSSL in a real‑world application  
- Designing a multi‑threaded TCP server using Qt’s `QThread` and socket classes  
- Building a cross‑platform GUI with Qt Widgets  
- Handling persistent chat history and client state management  
- Structuring a client‑server protocol with encrypted message envelopes (IV + ciphertext)  
- Writing an automated install script for building Qt projects  

> *Photon demonstrates my ability to combine cryptography, network programming, and GUI development into a secure, usable communication tool.*

---
