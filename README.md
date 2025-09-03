
# 🔐 Password Strength Analyzer & Custom Wordlist Generator

A Python tool to:
- Analyze password strength (scaled 0–10) using **zxcvbn**.
- Generate **custom wordlists** based on personal details (name, nickname, parent name, year of birth).
- Add variations like **leet-speak** (`p@ssw0rd`), years, and common patterns.
- Export results in `.txt` format for use in cracking tools.

---

## 📦 Installation (Windows)

1. **Clone or Download** this repository.  
   *(Click the green "Code" button on GitHub → Download ZIP → Extract)*

2. Open a terminal (PowerShell or VS Code terminal) inside the project folder.

3. Create and activate a virtual environment:
   ```bash
   python -m venv venv
   venv\Scripts\activate````

4. Install dependencies:

   ```bash
   pip install -r requirements.txt
   ```

---

## 🚀 Usage

### 🔎 Password Strength Analyzer

Analyze any password:

```bash
python analyzer.py "MyP@ssw0rd123"
```

Output example:

```
Password: MyP@ssw0rd123
Score (0-10): 7
Guesses: 1234567
Crack Time (offline fast hash): 2 days
Feedback: {'warning': 'This is a commonly used password pattern', 'suggestions': ['Use a longer password']}
```

---

### 📝 Custom Wordlist Generator

Generate wordlist from personal details:

```bash
python wordlist_gen.py
```

Sample interaction:

```
Enter your name: Priya
Enter your nickname: Paro
Enter your parent’s name: Siya
Enter your year of birth: 2001
```

Output:

```
Wordlist generated with 450 entries
Saved at wordlist/custom_wordlist.txt
```
### 🖥️ GUI Version
Run the Tkinter GUI:
```bash
python gui.py
```
---

## 📂 Project Structure

```
PasswordAnalyzer/
│── analyzer.py          # CLI password analyzer
│── wordlist_gen.py      # CLI wordlist generator
│── gui.py               # GUI version (Tkinter)
│── requirements.txt     # Dependencies
│── README.md            # Documentation
│── wordlist/            # Generated wordlists

```

---

## 🔧 Tech Stack

* Python 
* argparse
* zxcvbn
* nltk
* tk
