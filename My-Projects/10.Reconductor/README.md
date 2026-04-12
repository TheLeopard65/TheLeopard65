# Reconductor – Automated DNS Reconnaissance Framework

**A modular, automated reconnaissance tool** designed to streamline information gathering for penetration testing and bug bounty engagements. Integrates passive OSINT sources, active DNS brute‑forcing, IP resolution, and technology detection.

---

## 🔧 Technologies & Tools

- **Language:** Python 3.8+  
- **Passive Enumeration:** crt.sh, Amass, Subfinder, Assetfinder  
- **Active Brute‑forcing:** dnscan (or Python fallback)  
- **IP Resolution:** dnsx (or Python `dnspython` fallback)  
- **Technology Detection:** Wappalyzer  
- **Containerization:** Docker (all tools pre‑installed)  
- **Output Management:** Timestamped directories, JSON/TXT logs  

---

## 📌 Key Features

- **Passive Subdomain Enumeration** – crt.sh, Amass, Subfinder, Assetfinder  
- **Active DNS Brute‑forcing** – dnscan or multi‑threaded Python resolver  
- **Automatic Merge & Deduplication** – validates subdomains against target(s)  
- **IP Resolution** – dnsx or Python fallback  
- **Technology Stack Detection** – Wappalyzer integration  
- **Timestamped Output Structure** – organised per‑scan directories with module‑specific subfolders  
- **Docker Ready** – complete environment with all tools pre‑configured  
- **Fallback Mechanisms** – Python implementations when external tools are missing  

---

## 🚀 How It Works

1. **Passive Enumeration** – queries certificate logs (crt.sh) and OSINT sources (Amass, Subfinder, Assetfinder).  
2. **Active Brute‑forcing** – uses dnscan (or Python fallback) with a wordlist.  
3. **Merge & Filter** – combines all results, removes duplicates, and validates subdomains against the target domain(s).  
4. **IP Resolution** – resolves subdomains to IP addresses using dnsx (or Python fallback).  
5. **Technology Detection** – runs Wappalyzer on discovered subdomains to identify web frameworks, servers, and libraries.  
6. **Output** – saves all results in a timestamped directory under `output/`.

---

## ⚙️ Installation & Usage

```bash
# Clone repository
git clone https://github.com/TheLeopard65/reconductor.git
cd reconductor

# Set up virtual environment
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt

# (Optional) Install external Go tools for faster performance
# Or use Docker (recommended for ease)
make build   # builds Docker image
make test    # quick test on scanme.nmap.org

# Run a full scan
python reconductor.py -d example.com -a --amass --subfinder --assetfinder -r --wappalyzer
```

**Docker run:**
```bash
docker run --rm -v $(pwd)/output:/app/output reconductor:latest -d example.com -a --amass -r
```

---

## 📂 Repository

🔗 [github.com/TheLeopard65/reconductor](https://github.com/TheLeopard65/reconductor)

---

## 📄 License

MIT License – see `LICENSE` file.

---

## 👤 Author

**@TheLeopard65** – cybersecurity enthusiast and penetration testing practitioner.

---

## 🧠 What I Learned / Showcased

- Integrating multiple OSINT and active reconnaissance tools into a unified workflow  
- Implementing fallback mechanisms (Python resolvers) when external tools are unavailable  
- Designing a modular, extensible CLI with `argparse`  
- Managing timestamped output directories for forensic traceability  
- Building a Docker image with all dependencies pre‑installed (Amass, Subfinder, dnsx, etc.)  
- Automating subdomain validation, deduplication, and technology fingerprinting  

> *Reconductor demonstrates my ability to create efficient, production‑ready reconnaissance tooling for bug bounty and authorised penetration testing.*

---
