
What is Hash Cracker? 
Hash Cracker is a custom Python-based security tool designed to crack cryptographic hashes using two popular methods:
 
🎯Purpose:---
i. Hash Cracker helps security professionals, ethical hackers, and penetration testers to:
ii. Recover lost passwords (ethical use only)
iii. Test the strength of password hashing implementations
iv. Demonstrate the risk of weak or guessable passwords
V. Participate in CTF (Capture The Flag) or cybersecurity competitions

🧬 How It Works
Hash Cracker works by comparing a user-provided hash to the hashes of potential plaintext passwords. If a match is found, it reveals the original password. It supports:

✅ Two Attack Modes
i.Dictionary Attack (Wordlist Mode):
    Takes a list of known or likely passwords.
    Hashes each one.
    Compares it against the target hash.
    Efficient if the password is common or reused.
ii.Brute Force Attack:
    Tries every possible combination of characters (a-z, A-Z, 0-9, symbols) within a user-specified length range.
    Much slower but guaranteed to find the password if it exists within the defined character space.

🔐 Supported Hash Types
Hash Cracker supports all major types available in Python’s hashlib:
md5
sha1
sha224
sha256
sha384
sha512
sha3_224, sha3_256, sha3_384, sha3_512


## 🔍 Overview

**Hash Cracker** is a multi-threaded password hash cracking utility written in Python. It supports both dictionary and brute-force attacks for common hash algorithms including MD5, SHA-1, SHA-256, and more.

This tool is perfect for security researchers, penetration testers, and CTF players looking to verify hash weaknesses.

---

## 🎯 Features

- 🔓 Supports major hashing algorithms (`md5`, `sha1`, `sha256`, `sha512`, etc.)
- ⚔️ Two cracking modes:
  - Dictionary attack using wordlists
  - Brute-force with custom charset and length range
- 🧠 Multi-threaded execution using `ThreadPoolExecutor`
- 📈 Real-time progress display with `tqdm`
- 🎨 Styled terminal output using `termcolor`
- 🛠️ Cross-platform (Linux, Windows, macOS)

---

## ⚙️ Requirements

Install the required Python modules with:
bash
pip install tqdm termcolor

Usage:
python hash_cracker.py

Input Prompts:
Hash to crack: Paste your hash string
Crack mode: Choose (1) Wordlist or (2) Brute Force
Hash type: Choose from supported types
Wordlist path or brute-force charset/lengths depending on mode

Brute Force Attack Demo:


![Screenshot 2025-07-14 230035](https://github.com/user-attachments/assets/cd521130-9525-4830-a04b-2574808e9540)

