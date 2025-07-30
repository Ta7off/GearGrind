# 📘 GearGrind — Project Setup Guide

Welcome to **GearGrind**! This repo is the starting point for a car social media/Auction. Follow the steps below to set up the project locally and start grinding code 💻⚙️

---

## 🔧 Prerequisites

Make sure you have the following installed:

- [Python 3.10+](https://www.python.org/downloads/)
- [Git](https://git-scm.com/)
- Optional: [VS Code](https://code.visualstudio.com/)

---

## 🚀 Installation Steps

1. **Clone the repository**
   ```bash
   git clone https://github.com/Ta7off/GearGrind.git
   cd GearGrind
   ```

2. **Create a virtual environment**
   ```bash
   python -m venv .venv
   ```

3. **Activate the virtual environment**

   - **Windows (PowerShell)**
     ```bash
     .venv\Scripts\Activate.ps1
     ```

   - **macOS/Linux**
     ```bash
     source .venv/bin/activate
     ```

4. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

   ```bash
   python manage.py makemigrations
   python manage.py migrate
   ```

5. **Run the application**
   Replace with your actual command (e.g.):
   ```bash
   python manage.py runserver
   ```

---
---

## 💡 Tips

- Run `git pull` regularly to stay updated
- Add packages with `pip install <package>` and update requirements:
  ```bash
  pip freeze > requirements.txt
  ```

---

## 🤝 Contributing

Pull requests welcome! Feel free to open issues for bugs or ideas.
