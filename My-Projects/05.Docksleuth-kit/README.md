# DockSleuth Kit

**Docker Forensics Toolkit — Investigate Containers, One Layer at a Time.**  
A powerful Python‑based CLI tool for comprehensive digital forensics investigations of Docker containers. Automates evidence collection, artifact extraction, and reporting for incident response and malware analysis.

---

## 🔧 Technologies & Tools

- **Language:** Python 3.8+  
- **Docker API:** `docker-py` (interacts with Docker daemon)  
- **Reporting:** PDF generation (via `reportlab` or similar)  
- **CLI Framework:** `argparse`  
- **Virtual Environment:** `venv`  
- **Platform:** Linux (with Docker installed)  

---

## 📌 Key Features

- **Container Listing** – Display all active/inactive containers with ID, name, image, and state  
- **Targeted Evidence Collection** – Select one or more containers and collect:  
  - **Filesystem Extraction** – Full snapshot tarball  
  - **Network Information** – Interfaces, IPs, open ports (JSON)  
  - **Container Logs** – Configurable number of log lines  
  - **All Artifacts** – One‑command collection of everything  
- **Detailed PDF Reporting** – Human‑readable summary of findings  
- **Structured Output** – Organized per‑container directories with JSON summary  
- **Dry Run Mode** – Preview collection without writing data  
- **Verbose Logging** – Debug‑level output for troubleshooting  
- **Custom Output Directory** – User‑specified evidence storage path  

---

## 🚀 How It Works

1. **List containers** – `--list` shows all containers on the host.  
2. **Select target(s)** – Use `--cont` with container IDs or names.  
3. **Choose artifacts** – `--filesystem`, `--network`, `--logs`, or `--all`.  
4. **Run collection** – Tool connects to Docker daemon, extracts data, and saves to `--outdir`.  
5. **Generate report** – Optional `--report` creates a PDF summary.  

---

## ⚙️ Installation & Usage

```bash
# Clone repository
git clone https://github.com/TheLeopard65/DockSleuth-Kit.git
cd DockSleuth-Kit

# Create virtual environment
python3 -m venv VENV
source VENV/bin/activate

# Install system dependency (for PDF rendering)
sudo apt install -y libpango-1.0-0 libpangoft2-1.0-0

# Install Python dependencies
pip install -r requirements.txt

# Ensure Docker is running
sudo systemctl start docker   # if not already running

# List all containers
python3 main.py --list

# Collect all evidence from a container
python3 main.py --cont my_container --all -o ./case_001 --report

# Dry run (preview only)
python3 main.py --cont suspicious_container --all --dry-run
```

---

## 📂 Repository

🔗 [github.com/TheLeopard65/DockSleuth-Kit](https://github.com/TheLeopard65/DockSleuth-Kit)

---

## 📄 License

Apache License 2.0 – see `LICENSE` file.

---

## 👥 Contributors

- **Yasir Mehmood** ([@TheLeopard65](https://github.com/TheLeopard65))  
- Adan Talat  
- Ayesha  

---

## 🧠 What I Learned / Showcased

- Interacting with Docker daemon programmatically using Python  
- Automating forensic evidence collection in containerized environments  
- Generating structured JSON summaries and professional PDF reports  
- Designing a modular CLI with argparse and subcommands  
- Creating safe demo containers (command injection, file upload server) for testing  
- Handling edge cases (stopped containers, missing Docker daemon, permissions)  
- Collaborating on a multi‑contributor security tool  

> *DockSleuth Kit demonstrates my ability to build practical incident response tooling for modern containerized infrastructures.*

---
