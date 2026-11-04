# PasswordStrengthAndEncryption

A Python script that checks whether the entered text is a strong password (at least 8 characters with uppercase, lowercase, a digit and a special character) using a regular expression. If it passes, the text is encrypted with a new Fernet key and then decrypted again to show the round trip.

## Tech stack

- Python 3
- cryptography (Fernet)

## How to run

```bash
pip install cryptography
python main.py
```
