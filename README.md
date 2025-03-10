# 🔐 Password Strength Checker (Python + Tkinter)

A simple **GUI-based password strength checker** developed with **Python** and **Tkinter**.  
This application evaluates the **strength** of user-entered passwords based on essential security criteria and provides **real-time feedback** on how to improve weak passwords.

---

## 📝 About the Project

This project is a desktop-based tool designed to help users create stronger and more secure passwords. It evaluates passwords based on:
- Length
- Presence of uppercase letters
- Presence of lowercase letters
- Inclusion of numbers
- Usage of special characters

It provides users with a **clear strength rating** and **actionable suggestions** to improve their passwords.

---

## 💡 Features
✅ User-friendly **Graphical Interface** built with Tkinter  
✅ **Real-time assessment** of password strength  
✅ Feedback and suggestions to improve weak passwords  
✅ Easy to use — no installation required, just run the Python script  
✅ Lightweight and responsive design  
✅ Password masking (input hidden as `*`)

---

## 🛠️ Technologies Used
- **Python 3.x**
- **Tkinter** (standard Python GUI library)
- **re** (Regular Expression module for pattern matching)

---

## 📂 Project Structure
```
password-strength-checker/
│
├── password_strength_checker.py  # Main application script
└── README.md                     # Project description
```

---

## ▶️ How It Works

### Strength Criteria:
| Criteria                 | Description                                       |
|--------------------------|---------------------------------------------------|
| Length                  | Minimum 8 characters required                     |
| Uppercase Letters       | At least 1 uppercase letter (A-Z)                 |
| Lowercase Letters       | At least 1 lowercase letter (a-z)                 |
| Numbers                | At least 1 numeric digit (0-9)                    |
| Special Characters     | At least 1 symbol (e.g., @, #, $, %, etc.)         |

### Strength Levels:
| Score | Strength   |
|-------|------------|
| 5/5   | 🔒 Very Strong |
| 4/5   | ✅ Strong      |
| 3/5   | ⚠️ Moderate    |
| 0-2   | ❌ Weak        |

---

## 🚀 Getting Started

### Prerequisites
- Python 3.x installed  
- Tkinter is included by default with Python, but if not, install it via:
  ```bash
  sudo apt-get install python3-tk   # Linux
  ```

### Run the Application
1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/CyberSecurity-Projects.git
   cd CyberSecurity-Projects
   git checkout password-strength-checker
   ```

2. Run the Python script:
   ```bash
   python password_strength_checker.py
   ```

---

## 🖼️ GUI Preview

```
🔐 Password Strength Checker
[Enter password here]   ********
[Check Strength]  (button)

Password Strength: ✅ Strong

Feedback:
❗ Add at least one special character (e.g., @, #, $, %, etc.).
```

---

## 📌 Improvements You Can Make
✅ Add a **copy-to-clipboard** button for suggested passwords  
✅ Generate **strong passwords** automatically  
✅ Save password strength reports to a file  
✅ Add **theme customization** (light/dark mode)  
✅ Package into an **executable (EXE)** using `PyInstaller`

---

## ⚠️ Disclaimer
This tool is for **educational purposes** and basic password evaluation.  
For advanced security and password storage, consider using **industry-standard password managers** with **encryption**.

---

## 📄 License
Free to use for personal and educational purposes!

---
