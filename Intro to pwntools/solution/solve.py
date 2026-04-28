from pwn import *

def solve():
    conn = remote('194.102.62.166', 26531)
    
    for i in range(100):
        header = conn.recvuntil(b':\n')
        print(header.decode())

        question = conn.recvuntil(b'\n') 
        print(question.decode())

        i = 0
        j = 0
        k = 0
        num1 = 0
        num2 = 0
        operator = ''

        question = question.decode().split()
        for i in range(1, len(question)):
            if question[i].isdigit():
                num1 = int(question[i])
                break
        for j in range(i + 1, len(question)):
            if question[j] in '+-*/':
                operator = question[j]
                break   
        for k in range(j + 1, len(question)):
            if question[k].isdigit():
                num2 = int(question[k])
                break

        result = num1 + num2 if operator == '+' else num1 - num2 if operator == '-' else num1 * num2 if operator == '*' else num1 // num2
        conn.sendline(str(result).encode())
        print(f"num1: {num1}, operator: {operator}, num2: {num2}, result: {result}")
            
            

    conn.interactive()

if __name__ == "__main__":
    solve()