# Kernel Ascent

**Ascend to Root, Descend to Boot**  
A comprehensive system reconnaissance and vulnerability intelligence framework for security auditing and privilege escalation analysis.

> ⚠️ **Authorized Use Only** – This tool is intended for security professionals and system administrators on systems they own or have explicit permission to test. Unauthorized use may violate laws.

---

## 🔧 Technologies & Tools

- **Languages:** Bash (5.0+), Python 3.8+  
- **Data Sources:** Debian Security Tracker, CIRCL CVE Search, OSV.dev API, GTFOBins  
- **Reporting:** PDF generation (enscript, groff, ps2pdf) or compressed text fallback  
- **Containerization:** Docker (demo environment)  
- **Dependencies:** `jq`, `pip`, standard Unix tools  

---

## 📌 Key Features

- **1,000+ System Checks** – Kernel, sudo, SUID/SGID, capabilities, processes, network, sensitive files  
- **Vulnerability Intelligence Aggregation** – Fetches CVE data from multiple public sources into a local database  
- **Exploit Correlation** – Maps misconfigurations to known public exploits (GTFOBins, kernel CVEs, sudo CVEs)  
- **Advanced PDF Reporting** – Professional reports with executive summary, critical findings, and remediation guidance  
- **Risk‑Based Color Coding** – Highlights critical, high, and medium risks in terminal output  
- **Offline Capability** – Pre‑built JSON databases allow air‑gapped audits  
- **Containerized Demo** – Pre‑configured vulnerable Docker environment for safe testing  

---

## 🚀 How It Works

1. **Database Generation** – `generate-db.py` fetches CVE and exploit data from Debian, CIRCL, OSV.dev, and GTFOBins, producing `vulndb.csv` and JSON databases.  
2. **System Reconnaissance** – `recon.sh` scans the local system for kernel version, sudo version, SUID binaries, capabilities, world‑writable files, credentials, etc.  
3. **Correlation** – Findings are matched against the local vulnerability database to identify known CVEs and privilege escalation vectors.  
4. **Reporting** – Output is color‑coded to the terminal; optionally generates a PDF (or compressed text) report with prioritized remediation steps.

---

## ⚙️ Installation & Usage

```bash
# Clone repository
git clone https://github.com/TheLeopard65/Kernel-Ascent.git
cd Kernel-Ascent

# Install Python dependencies
pip install -r requirements.txt

# (Optional) Build/update vulnerability database
python3 generate-db.py --output vulndb.csv

# Run a standard audit
chmod +x recon.sh
./recon.sh

# Generate a PDF report
./recon.sh --report system_audit.pdf
```

**Demo environment (vulnerable container):**
```bash
cd demo-docker
./run-docker.sh   # Drops you into a shell as 'pentester' user
```

---

## 📂 Repository

🔗 [github.com/TheLeopard65/Kernel-Ascent](https://github.com/TheLeopard65/Kernel-Ascent)

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

- Building a comprehensive security auditing framework from scratch  
- Aggregating vulnerability data from multiple public APIs (Debian, CIRCL, OSV.dev)  
- Correlating system state with CVE databases to identify privilege escalation vectors  
- Generating professional PDF reports using Unix text‑processing tools  
- Creating a safe, containerized demo environment for testing  
- Designing offline‑capable databases for air‑gapped assessments  
- Collaborating on a multi‑contributor open‑source security project  

> *Kernel Ascent demonstrates my ability to build practical offensive security tooling, integrate external threat intelligence, and produce actionable reports for system hardening.*

---
