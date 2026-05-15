# hmac_project

Implementation of HMAC (Hash-based Message Authentication Code) using a Python Client-Server architecture for message authentication and integrity verification.

---

# Overview

This project demonstrates how HMAC can be used to provide:

- Message Integrity
- Message Authentication
- Tamper Detection
- Secure Client-Server Communication

The client generates an HMAC using a shared secret key and sends both the message and HMAC to the server.  
The server verifies the received HMAC to ensure that the message has not been modified during transmission.

---

# Technologies Used

- Python 3
- Socket Programming
- Multi-threading
- HMAC
- SHA-256 Hashing

---

# Project Structure

```text
hmac_project/
│
├── client/
│   ├── __init__.py
│   └── client.py
│
├── server/
│   ├── __init__.py
│   ├── server.py
│   └── verifier.py
│
├── shared/
│   ├── __init__.py
│   └── config.py
│
└── README.md
```
