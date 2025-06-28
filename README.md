# Choose-Your-Own-Adventure Game (Python + Tkinter)

This is a simple choose-your-own-adventure game built with Python and Tkinter for the GUI, and optional sound playback.

## 🚀 Download

Get the latest version of the app:

| Platform | File |
|----------|------|
| 🖥 macOS | [Download .app (zipped)](https://github.com/waed-star/adventure-game/releases/download/v1.0/Horror-Game.zip) |

> ⚠️ macOS users: You may need to right-click → Open the first time to bypass Gatekeeper.

## 🛠 Installation

### macOS
1. Download and unzip the `.app`
2. Right-click → Open (to bypass Gatekeeper)
3. Done!

### Windows
1. Download and run the `.exe`
2. If SmartScreen warns you, click “More info” → “Run anyway”

---

## 📦 Requirements

- **Python 3.9**
- macOS / Windows / Linux
- Virtual environment (`venv`)
- Dependencies listed in `requirements.txt`

---

## 🛠️ Setup Instructions

### 1. ✅ Ensure Python 3.9 is Installed

Check your version:
```bash
python3 --version
```

If it’s not 3.9.x, install it:

- **macOS** (via Homebrew):
  ```bash
  brew install python@3.9
  ```
---

### 2. 🔒 Create and Activate a Virtual Environment

In your project folder:

```bash
# Create the venv (named `venv`)
python3.9 -m venv venv

# Activate it
# macOS/Linux
source venv/bin/activate

---

### 3. 📥 Install Dependencies

```bash
pip install pydub simpleaudio
```

---

### 4. ▶️ Run the Project

```bash
python main.py
```

---

## 📁 File Structure

```
your_project/
├── main.py
├── README.md
├── .gitignore
├── assets/           # images or audio files
└── venv/             # virtual environment (ignored in Git)
```

---
