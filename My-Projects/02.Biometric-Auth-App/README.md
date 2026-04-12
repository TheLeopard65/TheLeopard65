# Biometric Auth App

**A lightweight and efficient biometric authentication application** developed in Python.  
This project demonstrates secure user identity verification using facial recognition technology, integrated with a simple GUI and local database storage.

> 🔒 **Privacy First** – All data is stored locally; no external cloud services are used.

---

## 🔧 Technologies & Tools

- **Language:** Python 3.x  
- **Face Recognition:** OpenCV  
- **Database:** SQLite (local)  
- **GUI Framework:** Tkinter  
- **Data Handling:** NumPy  

---

## 📌 Key Features

- **Face Recognition Authentication** – Secure login using facial features  
- **Local SQLite Database** – Stores user profiles and face encodings  
- **Tkinter GUI** – Simple and intuitive graphical interface  
- **Lightweight & Easy to Deploy** – Minimal dependencies, runs on standard hardware  
- **Privacy Focused** – No biometric data leaves the user’s machine  

---

## 🚀 How It Works

1. **Registration** – User captures their face via the camera; facial features are processed and stored in the local database.  
2. **Login** – The app captures a live face and compares it against stored encodings.  
3. **Access Granted** – On successful match, the user is authenticated and granted access.  

---

## ⚙️ Installation & Setup

```bash
# Clone the repository
git clone https://github.com/TheLeopard65/Biometric-Auth-App.git
cd Biometric-Auth-App

# (Optional) Create and activate a virtual environment
python -m venv App
source App/bin/activate   # On Windows: App\Scripts\activate

# Install dependencies
pip install -r Requirements.txt

# Run the application
python main.py
```

---

## 📂 Repository

🔗 [github.com/TheLeopard65/Biometric-Auth-App](https://github.com/TheLeopard65/Biometric-Auth-App)

---

## 📄 License

MIT License – see the `LICENSE` file for details.

---

## 👤 Author

**@TheLeopard65** – cybersecurity enthusiast and developer.

---

## 🧠 What I Learned / Showcased

- Integrating OpenCV for real‑time face detection and recognition  
- Building a local SQLite database for secure user data storage  
- Creating a functional desktop GUI with Tkinter  
- Handling camera input and image processing in Python  
- Emphasizing user privacy by avoiding cloud-based biometric storage  

> *This project highlights my ability to combine computer vision, database management, and GUI development into a practical security tool.*
