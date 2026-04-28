#!/usr/bin/env python3
from pwn import *

def solve():
    conn = remote('host', 1337)
    
    # Your implementation here

    conn.interactive()

if __name__ == "__main__":
    solve()