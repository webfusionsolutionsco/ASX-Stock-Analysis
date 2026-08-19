# How to Start and Activate a Python Virtual Environment

This guide explains how to create, activate, and manage a Python virtual environment (`.venv`) for the **ASX-Stock-Analysis** project.

---

## 1. Quick Start (Windows PowerShell)

If a virtual environment (`.venv`) already exists in your workspace root, activate it with:

```powershell
.\.venv\Scripts\Activate.ps1
```

*(You will see `(.venv)` appear in your terminal prompt indicating it is active).*

> **Note (Execution Policy Error):** If PowerShell shows `running scripts is disabled on this system`, run this command in your PowerShell terminal to allow script execution for the current session:
> ```powershell
> Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope Process
> ```

---

## 2. Activation Commands by OS & Shell

| OS / Shell | Command |
| :--- | :--- |
| **Windows PowerShell** | `.\.venv\Scripts\Activate.ps1` |
| **Windows Command Prompt (cmd)** | `.\.venv\Scripts\activate.bat` |
| **macOS / Linux (Bash / Zsh)** | `source .venv/bin/activate` |

---

## 3. Creating a New Environment (If `.venv` does not exist)

If `.venv` is missing, create it from your project root directory:

```bash
python -m venv .venv
```

After creation, activate it using the appropriate command above.

---

## 4. Installing Project Dependencies

Once your virtual environment is active (`(.venv)` visible in prompt):

```bash
pip install --upgrade pip
pip install -r requirements.txt
```

---

## 5. Setting the Python Interpreter in VS Code

To ensure VS Code uses the correct environment for running scripts and tests:

1. Open the Command Palette (`Ctrl + Shift + P` on Windows/Linux, `Cmd + Shift + P` on Mac).
2. Type and select **`Python: Select Interpreter`**.
3. Choose the interpreter inside your virtual environment (e.g., `.\.venv\Scripts\python.exe`).

---

## 6. Running Exercises & Tests

With the environment activated:

- **Run a script:**
  ```powershell
  python Exercises/ex01_stock_data_parser.py
  ```
- **Run all unit tests:**
  ```powershell
  pytest
  ```

---

## 7. Deactivating the Environment

When you are finished working in the virtual environment, exit it by running:

```bash
deactivate
```
