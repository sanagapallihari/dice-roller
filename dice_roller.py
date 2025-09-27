import random

def roll_dice():
    return random.randint(1, 6)

def main():
    print("🎲 Welcome to Dice Roller 🎲")
    while True:
        input("Press Enter to roll the dice (or type 'q' to quit): ")
        number = roll_dice()
        print(f"You rolled: {number}")
        
        choice = input("Roll again? (y/n): ").lower()
        if choice != 'y':
            print("Goodbye 👋")
            break

if __name__ == "__main__":
    main()
