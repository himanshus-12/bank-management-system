# 🏦 Bank Management System

A command-line Bank Management System built using **Python and Object-Oriented Programming (OOP)**. It allows users to create bank accounts, perform basic transactions, manage account details, and store account information persistently using JSON.

This project was built to practice Python fundamentals, classes, file handling, data management, and exception handling through a practical application.

## ✨ Features

| Feature             | Description                                                                                |
| ------------------- | ------------------------------------------------------------------------------------------ |
| 📝 Account Creation | Create an account with personal details and a randomly generated account number.           |
| 💰 Deposit Money    | Deposit money into an existing account.                                                    |
| 💸 Withdraw Money   | Withdraw money after account authentication and balance verification.                      |
| 👤 Account Details  | View account information after PIN verification.                                           |
| ✏️ Update Details   | Update name, age, email, or PIN.                                                           |
| 🗑️ Delete Account  | Delete an account after confirmation, provided the balance is zero.                        |
| 🔐 Authentication   | Verify account number and PIN before account operations.                                   |
| 💾 Data Persistence | Store account records in a JSON file so data remains available between program executions. |
| ✅ Input Validation  | Validate user inputs, PIN format, age, email, and transaction amounts.                     |

## 🛠️ Tech Stack

- **Language:** Python
- **Data Storage:** JSON
- **Modules:** `json`, `random`, `string`, `pathlib`

## 📂 Project Structure

```text
Bank-Management-System/
│
├── bank.py
└── README.md
```

- `bank.py` – Contains the bank class, account operations, and command-line dashboard.
- `README.md` – Project documentation.

## 🚀 Getting Started

### Prerequisites

- Python 3.x installed on your system.

### Installation

**1. Clone the repository**

```bash
git clone YOUR_REPOSITORY_URL
```

**2. Navigate to the project directory**

```bash
cd Bank-Management-System
```

**3. Run the application**

```bash
python bank.py
```

## 📋 Application Menu

```text
========== BANK MANAGEMENT SYSTEM ==========

Press 1 for creating an account
Press 2 for depositing money
Press 3 for withdrawing money
Press 4 for details
Press 5 for updating the details
Press 6 for deleting your account
Press 7 for exit
```

## 🧠 Concepts Practised

Building this project helped me understand and implement:

- Object-Oriented Programming and class methods.
- Python lists and dictionaries.
- List comprehensions and conditional expressions.
- File handling using `open()`.
- Exception handling using `try-except`.
- Random value generation.
- Input validation and authentication.
- CRUD operations (Create, Read, Update, Delete).

## ⚠️ Disclaimer

This is an educational project developed for learning Python programming. It is not a real banking application and should not be used to store actual financial information or credentials.

---

**Built with Python 🐍**
