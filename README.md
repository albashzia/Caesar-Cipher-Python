# Caesar Cipher Encryption (Python)

This project is a basic Python implementation of the **Caesar Cipher** encryption technique.
It encrypts text by shifting each alphabetical character forward by a fixed number of positions,
while preserving letter case and leaving non-alphabet characters unchanged.


## 🔐 How It Works

- Each letter is shifted **forward by 3 positions** in the alphabet
- Wrap-around is applied:
  - `x → a`
  - `y → b`
  - `z → c`
- Uppercase and lowercase letters are handled separately
- Spaces, numbers, and symbols remain unchanged
