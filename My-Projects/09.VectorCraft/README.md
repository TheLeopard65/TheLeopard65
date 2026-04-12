# VectorCraft

**Educational Offensive Security Payload Generation Framework (Simulation Only)**  
A CLI tool that generates safe, non‑executing payload templates for XSS, SQLi, Command Injection, and SSTI – designed for defensive research, training, and lab environments.

> ⚠️ **Educational Purpose Only** – All payloads are inert templates and do not execute. Intended solely for authorised security testing and learning.

---

## 🔧 Technologies & Tools

- **Language:** Python 3.8+  
- **Libraries:** `pyfiglet` (banner), `rich` (colored console output)  
- **CLI Framework:** `argparse`  
- **Export Formats:** JSON, TXT, CSV  

---

## 📌 Key Features

- **4 Attack Modules** – XSS, SQLi, Command Injection (CMDi), Server‑Side Template Injection (SSTI)  
- **Rich Filtering** – by type (substring), context (HTML, JS, attribute), platform (Linux, Windows), database (MySQL, PostgreSQL, MSSQL, etc.)  
- **Random Payload Selection** – pick 1 or N random payloads from filtered set  
- **Transformations** – URL, Base64, Hex, ROT13 encoding; case, whitespace, comment obfuscation  
- **Export Options** – JSON, TXT, CSV with custom filenames  
- **Active Configuration Display** – shows exactly which flags are active  
- **Verbose Logging** – debug output for troubleshooting  
- **Clean, Colourful Output** – using the `rich` library  

---

## 🚀 How It Works

1. **Select a module** – `xss`, `sqli`, `cmdi`, or `ssti`.  
2. **Apply filters** – narrow down by type, context, platform, database (SQLi only).  
3. **Optional transformations** – encode or obfuscate payloads.  
4. **Randomise or limit count** – pick random payloads or show first N.  
5. **Export** – print to console or save as JSON/TXT/CSV.  

All payloads are templates with metadata (context, platform, database, engine) – **no actual execution occurs**.

---

## ⚙️ Installation & Usage

```bash
# Clone repository
git clone https://github.com/TheLeopard65/VectorCraft.git
cd VectorCraft

# Install dependencies
pip install -r requirements.txt

# Make executable (optional)
chmod +x vectorcraft.py

# List available modules
python vectorcraft.py --list-modules

# Generate all XSS payloads
python vectorcraft.py -m xss

# SQLi – time‑based blind for Linux, all databases
python vectorcraft.py -m sqli --type blind --platform linux

# Command injection – Windows, random 2 payloads
python vectorcraft.py -m cmdi --platform windows --random 2

# XSS with URL encoding + case obfuscation, export to CSV
python vectorcraft.py -m xss --encode url --obfuscate case --export csv --output my_xss.csv
```

---

## 📂 Repository

🔗 [github.com/TheLeopard65/VectorCraft](https://github.com/TheLeopard65/VectorCraft)

---

## 📄 License

Educational use only – not for production or malicious purposes.

---

## 👤 Author

**@TheLeopard65** – cybersecurity enthusiast and offensive security researcher.

---

## 🧠 What I Learned / Showcased

- Building a modular CLI framework with `argparse` and dynamic module loading  
- Implementing encoding and obfuscation transformations for payloads  
- Designing filter logic for multiple attack vectors (XSS, SQLi, CMDi, SSTI)  
- Exporting structured data to JSON, CSV, and plain text  
- Creating a safe, educational tool that simulates payload generation without execution  
- Using `rich` and `pyfiglet` for professional, colourful terminal output  

> *VectorCraft demonstrates my ability to create practical training tools for defensive security teams and penetration testing students.*

---
