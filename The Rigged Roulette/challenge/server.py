import random
import sys

# The Casino's highly secure prime modulus for the PRNG
M = 2**61 - 1  # 2305843009213693951, a Mersenne prime

class LCGCasino:
    def __init__(self):
        # The multiplier and increment are secret!
        self.a = random.randint(2, M - 1)
        self.c = random.randint(2, M - 1)
        self.state = random.randint(2, M - 1)
        self.money = 100
        
        try:
            with open("flag.txt", "r") as f:
                self.flag = f.read().strip()
        except FileNotFoundError:
            self.flag = "CTF{fake_flag_for_testing}"

    def next_number(self):
        self.state = (self.a * self.state + self.c) % M
        return self.state

    def play(self):
        print(f"Welcome to the Rigged Roulette Casino!")
        print(f"You start with $100. Guess the next number to win the Jackpot!")
        
        while True:
            print(f"\n--- Balance: ${self.money} ---")
            print("1. Spectate a spin (Cost: $10)")
            print("2. Bet on the next spin (Cost: $10)")
            print("3. Buy the Flag (Cost: $1,000,000)")
            print("4. Leave Casino")
            
            try:
                choice = input("Your choice: ").strip()
            except EOFError:
                break
                
            if choice == '1':
                if self.money < 10:
                    print("You don't have enough money to spectate!")
                    continue
                self.money -= 10
                result = self.next_number()
                print(f"[Spin complete] The wheel landed on: {result}")
                
            elif choice == '2':
                if self.money < 10:
                    print("You don't have enough money to bet!")
                    continue
                
                try:
                    guess = int(input("Enter your guess for the next number: "))
                except ValueError:
                    print("Invalid input! Must be a number.")
                    continue
                    
                self.money -= 10
                result = self.next_number()
                
                if guess == result:
                    print(f"JACKPOT! The wheel landed on {result}. You won $1,000,000!")
                    self.money += 1000000
                else:
                    print(f"Wrong! The wheel actually landed on {result}. Better luck next time.")
                    
            elif choice == '3':
                if self.money >= 1000000:
                    print("Transferring funds...")
                    self.money -= 1000000
                    print(f"Congratulations! Here is your flag: {self.flag}")
                    break
                else:
                    print("Nice try, but you are not rich enough for this exclusive item.")
                    
            elif choice == '4':
                print("Thanks for donating your money to us.")
                break
            else:
                print("Invalid choice.")

if __name__ == "__main__":
    sys.stdout.reconfigure(line_buffering=True)
    sys.stdin.reconfigure(line_buffering=True)
    
    casino = LCGCasino()
    casino.play()