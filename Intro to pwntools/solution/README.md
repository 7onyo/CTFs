# Solution – Intro to Pwntools

## Explanation

This challenge demonstrates automation using **pwntools**. The goal is to solve 100 math problems sent by a remote server.

The provided files are:

- `solve.py` – Python script that automates connecting to the server, parsing each question, computing the result, and sending it back.  
- `sample.txt` – Example of the server interaction showing received questions and the script's responses.

**Key points about `solve.py`:**

1. **Remote Connection**  
   Uses `pwntools` to connect to the server at `some_ip:some_port`, allowing automated input and output handling.

2. **Parsing Questions**  
   Each question is received as text (e.g., `What is: 12 * 16 ?`). The script extracts the two numbers and the operator, then calculates the correct answer.

3. **Automated Calculation and Response**  
   Based on the operator (`+`, `-`, `*`, `/`), the script computes the result and sends it back to the server. This repeats for all 100 rounds.

4. **Interactive Mode**  
   After completing all rounds, the script enters interactive mode (`conn.interactive()`), to extract the flag manually.

`sample.txt` illustrates how the script communicates with the server, showing each question, parsed numbers, computed result, and confirmation from the server.