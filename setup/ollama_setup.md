# Instructions for Downloading, Installing, and Running Ollama

Ollama is Meta's AI model that you can download and run locally on your machine. Follow these steps to set up Ollama on your system.

---

## Prerequisites

Before you begin, ensure the following requirements are met:

1. **Operating System**:
   - Ollama is compatible with macOS, Windows, and Linux
        - macOS: Requires macOS 11 Big Sur or later
        - Windows: Requires Windows 10 or laters


2. **Hardware**:
   - A GPU is recommended for faster performance but not required.

3. **Additional Software**:
   - Python 3.8 or later (we'll be using Python to code with the ai).
   - pip (Python's package manager).
   - git (to clone repositories if needed).

---

## Step 1: Download Ollama

1. Visit the official [Ollama Download Page](https://ollama.com/download).
2. Select your operating system (it should auto select) and click 'Download'.

---

## Step 2: Install llama3.2 3b
We will specfically being using llama3.2 3b version of Ollama.

1. Pull llama3.2 3b: 
   `ollama pull llama3.2`
- (Don't worry about adding 3b to the command, it will automatically be selected.)

---

## Step 3: Run Ollama Locally

1. To run Ollama in a terminal:
   `ollama run llama3.2`
2. To quit enter:
   `/bye`
---

## Additional Resources

- [Ollama GitHub Repository](https://github.com/meta/ollama)
- [Python Virtual Environments Guide](https://docs.python.org/3/library/venv.html)
- [WSL2 Setup for Windows](https://learn.microsoft.com/en-us/windows/wsl/install)

---
