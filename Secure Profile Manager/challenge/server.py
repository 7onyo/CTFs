#!/usr/bin/env python3
from Crypto.Cipher import AES
import os
import sys


def read_line(prompt: str) -> bytes:
    """Read a line from stdin, preserving raw bytes."""
    sys.stdout.write(prompt)
    sys.stdout.flush()
    return sys.stdin.buffer.readline().rstrip(b"\n").rstrip(b"\r")

KEY = os.urandom(16)
FLAG = open("flag.txt").read().strip()
BLOCK_SIZE = 16


def pad(data: bytes) -> bytes:
    """PKCS7 padding."""
    padding_len = BLOCK_SIZE - (len(data) % BLOCK_SIZE)
    return data + bytes([padding_len] * padding_len)


def unpad(data: bytes) -> bytes | None:
    """PKCS7 unpadding. Returns None if invalid."""
    if len(data) == 0:
        return None
    padding_len = data[-1]
    if padding_len == 0 or padding_len > BLOCK_SIZE:
        return None
    if data[-padding_len:] != bytes([padding_len] * padding_len):
        return None
    return data[:-padding_len]


def encrypt(data: bytes) -> bytes:
    cipher = AES.new(KEY, AES.MODE_ECB)
    return cipher.encrypt(pad(data))


def decrypt(data: bytes) -> bytes | None:
    if len(data) == 0 or len(data) % BLOCK_SIZE != 0:
        return None
    cipher = AES.new(KEY, AES.MODE_ECB)
    return unpad(cipher.decrypt(data))


def profile_for(email: bytes) -> bytes:
    """Build a structured profile string. Sanitizes & and = to prevent injection."""
    email = email.replace(b"&", b"").replace(b"=", b"")
    return b"email=" + email + b"&role=user"


def parse_profile(data: bytes) -> dict:
    """Parse a key=value&key=value string into a dict."""
    result = {}
    for pair in data.decode().split("&"):
        if "=" in pair:
            key, value = pair.split("=", 1)
            result[key] = value
    return result


def banner():
    print("=" * 50)
    print("             Secure Profile Manager")
    print("=" * 50)
    print()
    print("  Create a profile and prove you're an admin")
    print("  to access the secret flag!")
    print()
    print("  Commands:")
    print("    1 - Create a new profile")
    print("    2 - Login with an encrypted token")
    print("    3 - Exit")
    print()


def main():
    banner()

    while True:
        try:
            choice = read_line("> ").strip()

            if choice == b"1":
                email = read_line("Enter your email: ")

                if len(email) == 0:
                    print("Email cannot be empty!\n")
                    continue
                if len(email) > 64:
                    print("Email too long! (max 64 bytes)\n")
                    continue

                profile = profile_for(email)
                token = encrypt(profile).hex()

                print(f"Profile created!")
                print(f"Your encrypted token: {token}")
                print()

            elif choice == b"2":
                token_hex = read_line("Enter your token: ").strip()

                try:
                    token = bytes.fromhex(token_hex.decode())
                except ValueError:
                    print("Invalid hex!\n")
                    continue

                decrypted = decrypt(token)
                if decrypted is None:
                    print("Invalid token (decryption failed)!\n")
                    continue

                try:
                    profile = parse_profile(decrypted)
                except Exception:
                    print("Corrupted profile data!\n")
                    continue

                role = profile.get("role", "unknown")
                email = profile.get("email", "unknown")

                print(f"Welcome, {email}!")
                print(f"Role: {role}")

                if role == "admin":
                    print(f"Admin access granted! Here is your flag: {FLAG}")
                else:
                    print(f"Access denied. You need admin privileges.")
                print()

            elif choice == b"3":
                print("Goodbye!")
                break

            else:
                print("Invalid option, please enter 1, 2, or 3.\n")

        except EOFError:
            break
        except KeyboardInterrupt:
            print("\nGoodbye!")
            break


if __name__ == "__main__":
    main()