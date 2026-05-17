#hmac_project

Implementation of Hash-based Message Authentication Code (HMAC) using a Python Client–Server Architecture for Secure Communication

#Project Description

This project demonstrates the implementation of HMAC (Hash-based Message Authentication Code) to ensure secure communication between a client and a server.

The system focuses on protecting data during transmission by providing:

- Message Integrity
- Message Authentication
- Tamper Detection
- Secure Client–Server Communication


#Technologies Used
- Python 3
- Socket Programming
- Multithreading
- HMAC (Hash-based Message Authentication Code)
- SHA-256 Hashing Algorithm

#How It Works
- Client creates a message
- Client generates HMAC using a shared secret key
- Message + HMAC are sent to server
- Server recalculates HMAC using the same key
- If both HMAC values match → message is authentic
- If not → message is rejected (tampering detected)

#Project Structure

```
hmac_project/
├── attacks/
│   └── tamper_test.py
├── client/
│   ├── __init__.py
│   ├── client.py
│   └── hmac_utils.py
├── server/
│   ├── __init__.py
│   ├── server.py
│   └── verifier.py
├── shared/
│   ├── __init__.py
│   └── config.py
└── README.md
```
