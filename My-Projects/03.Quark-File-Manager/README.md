# QUARK File Manager

**A sleek, modern, cross-platform file manager** built with C++, OpenGL, and ImGui.  
Designed for developers and power users who crave speed, customization, and a minimalist UI.

> 📚 **Course Project** – Fourth Semester Operating Systems course.  
> *Note: Project quality isn’t great, but it demonstrates core OS and GUI concepts.*

---

## 🔧 Technologies & Tools

- **Language:** C++17  
- **GUI Framework:** Dear ImGui  
- **Graphics API:** OpenGL  
- **Windowing:** GLFW  
- **File Icons & Fonts:** STB image loader, Courier New font  
- **Build System:** CMake  
- **Platforms:** Linux & Windows  

---

## 📌 Key Features

- 📂 **Tree‑style file navigation**  
- 🧭 **Bookmark quick‑access panel** (Home, Desktop, Downloads)  
- 🔍 **Hidden file visibility toggle**  
- 🧠 **Keyboard shortcuts** (e.g., `ESC` to exit)  
- 📑 **Detailed file information** – name, size, permissions, type, last modified  
- 🧰 **Context menu actions** – open, create new file/folder, cut/copy/paste, rename, compress (`.tar.gz`), trash/delete  
- 🎨 **Custom theming** with ImGui and Courier New fonts  
- 🔌 **Cross‑platform** – Linux & Windows  

---

## 🚀 How It Works

1. **Launch** – The app scans the root directory (or last location) and displays a tree view.  
2. **Navigate** – Click folders to drill down; use bookmarks for quick jumps.  
3. **Manage files** – Right‑click for context menu operations (copy, delete, compress, etc.).  
4. **View details** – Select any file to see its metadata (permissions, size, modification time).  
5. **Toggle hidden files** – Show or hide dotfiles and system‑hidden items.  

---

## ⚙️ Build Instructions

### Prerequisites (Linux)

```bash
sudo apt install -y cmake libxrandr-dev libx11-dev libxext-dev libxi-dev libgl1-mesa-dev libxinerama-dev libxcursor-dev
```

### Build & Run

```bash
git clone https://github.com/TheLeopard65/Quark-File-Manager.git
cd Quark-File-Manager
mkdir build && cd build
cmake ..
make -j$(nproc)
./QUARK
```

> **Windows:** Generate a Visual Studio solution with CMake, then build the `QUARK` target.

---

## 📂 Repository

🔗 [github.com/TheLeopard65/Quark-File-Manager](https://github.com/TheLeopard65/Quark-File-Manager)

---

## 📄 License

MIT License – see the `LICENSE` file for details.

---

## 👤 Author

**@TheLeopard65** – cybersecurity enthusiast and developer.

---

## 🧠 What I Learned / Showcased

- Implementing a GUI file manager using immediate mode rendering (ImGui)  
- Integrating OpenGL for texture rendering (folder/file icons)  
- Cross‑platform filesystem operations (Linux `xdg‑open`, Windows `start`)  
- Building a CMake project with third‑party dependencies (GLFW, ImGui, stb)  
- Handling file compression (`.tar.gz`) from a C++ application  
- Applying OS course concepts: file permissions, directory traversal, and system calls  

> *This project reflects my early exploration of GUI programming, cross‑platform development, and operating system internals.*

---
