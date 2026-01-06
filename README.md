# Caesar Cipher (Python)

This project is a beginner-friendly Python implementation of the **Caesar Cipher**.
It provides both **encryption and decryption** functionality through a simple
**menu-based console program**, using only Python fundamentals.

The program shifts alphabetical characters by a fixed number of positions,
preserves letter case, and leaves non-alphabet characters unchanged.


## 🔐 How It Works

- Each alphabetical character is shifted by **3 positions**
- Encryption shifts letters forward  
- Decryption shifts letters backward
- Wrap-around logic is applied:
  - `x → a`, `y → b`, `z → c`
  - `a → x`, `b → y`, `c → z`
- Uppercase and lowercase letters are handled separately
- Spaces, numbers, and symbols remain unchanged


## 🧭 Menu-Based Interface

When the program runs, the user is presented with a menu:

- `1` → Encrypt text
- `2` → Decrypt text
- `3` → Exit program

This allows the user to interactively choose between encryption and decryption
within a single console application.


## 📁 Project Structure

- `caesar_cipher.py` — Main menu-driven program (controls program flow)
- `encrypter.py` — Handles Caesar Cipher encryption logic
- `decrypter.py` — Handles Caesar Cipher decryption logic
- `README.md` — Project documentation


## 🧠 Concepts Used

- String traversal
- Conditional statements
- ASCII character manipulation using `ord()` and `chr()`
- Modulus (`%`) operation for wrap-around logic
- Function-based program structure
- Menu-driven program flow
- User input handling


## 🎯 Purpose of This Project

This project is intended for beginners to practice:
- Logical thinking
- Working with strings
- Writing clean, structured Python code
- Building small console-based applications

No advanced concepts such as file handling, exceptions, or external libraries
are used.
