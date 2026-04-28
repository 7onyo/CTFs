# Sanity Check - Shifting Winds

**Encrypted String:** `VWUJDT{X3md0n3}` (found in `Cryptic.rar`)

The challenge name hints at a shift cipher. Comparing the prefix (`VWUJDT`) to the required flag format (`UVTICS`) shows each letter is shifted forward by 1 in the ASCII table.

To get the flag, I used `solve.py` script. It iterates through the encrypted string, ignores the curly brackets and numbers, and shifts all alphabetical characters back by 1 using their ASCII values (`ord` and `chr`).

### Flag
> **`UVTICS{W3lc0m3}`**
