import random
import time

def add(a, b):
    """Return the sum of a and b."""
    return a + b

def subtract(a, b):
    """Return a minus b."""
    return a - b

def multiply(a, b):
    """Return the product of a and b."""
    return a * b

def divide(a, b):
    """Return a divided by b, or an error message if b is zero."""
    if b == 0:
        return "Error: Division by zero is not allowed."
    return a / b

def play_game():
    """Play the roulette number game - score starts at 10, win if >= 100, lose if <= 0.

    Roulette Percentages:
    - 45% addition (+)
    - 35% subtraction (-)
    - 10% multiplication (*)
    - 4% divide by 2 (/2)
    - 6% divide by 3 (/3)
    """
    score = 10
    print("\n" + "="*50)
    print("WELCOME TO ROULETTE GAME!")
    print("="*50)
    print("Starting Score: 10")
    print("Goal: Reach 100 to WIN")
    print("Lose: Score drops to 0 or below")
    print("="*50 + "\n")

    while True:
        user_input = input(f"Score: {score}\nWhat number do you want: ").strip().lower()

        if user_input == 'q':
            print("Exiting game mode...")
            return None

        try:
            num = float(user_input)
        except ValueError:
            print("Invalid input! Please enter a number or 'q' to quit.")
            continue

        spin = random.random()

        if spin < 0.45:
            operator = '+'
            score = score + num
        elif spin < 0.80:
            operator = '-'
            score = score - num
        elif spin < 0.90:
            operator = '*'
            score = score * num
        elif spin < 0.94:
            operator = '/2'
            score = score / 2
        else:
            operator = '/3'
            score = score / 3

        # Spin the roulette wheel with animation effect
        print("\n🎡 SPINNING THE ROULETTE WHEEL... 🎡\n")
        operators = ['+', '-', '*', '/2', '/3']

        for _ in range(15):
            for op in operators:
                print(f"\r  [{op}]  ", end='', flush=True)
                time.sleep(0.05)

        for _ in range(8):
            for op in operators:
                print(f"\r  [{op}]  ", end='', flush=True)
                time.sleep(0.1)

        for _ in range(3):
            for op in operators:
                print(f"\r  [{op}]  ", end='', flush=True)
                time.sleep(0.2)

        print(f"\r  [{operator}]  ", end='', flush=True)
        time.sleep(0.5)
        print()

        score = int(score)
        print(f"🎉 ROULETTE RESULT: {operator}")
        print(f"Result: {score}\n")

        if score >= 100:
            print("="*50)
            print("🎉 YOU WON! 🎉")
            print(f"Final Score: {score}")
            print("="*50)
            break

        if score <= 0:
            print("="*50)
            print("💀 GAME OVER - YOU LOST! 💀")
            print(f"Final Score: {score}")
            print("="*50)
            break

    while True:
        choice = input("\nWhat would you like to do?\n1. Play again\n2. Return to calculator\n3. Exit\nEnter (1/2/3): ").strip()

        if choice == '1':
            play_game()
            return None
        elif choice == '2':
            print("Returning to calculator...\n")
            return None
        elif choice == '3':
            print("Goodbye!")
            exit()
        else:
            print("Invalid choice. Enter 1, 2, or 3.")

print("===============================")
print(" RULES ")
print("===============================")
print(" RULES:")
print(" - Type 'q' at any prompt to QUIT the program.")
print(" - Type 'c' at the first number prompt to use")
print(" your last calculated result.")
print(" - Type 'gg' at the first number prompt to play roulette game.")
print("==================================================")

last_result = None

while True:
    if last_result is not None:
        user_input1 = input(f"\nFirst number (or 'c' for {last_result}, 'gg' for game): ").strip().lower()
        if user_input1 == 'gg':
            play_game()
            continue
        if user_input1 == 'c':
            num1 = last_result
            print(f"-> Using: {num1}")
        elif user_input1 == 'q':
            print("Goodbye!")
            break
        else:
            try:
                num1 = float(user_input1)
            except ValueError:
                print("Invalid input! Starting over.")
                continue
    else:
        user_input1 = input("\nFirst number (or 'gg' for game): ").strip().lower()
        if user_input1 == 'gg':
            play_game()
            continue
        if user_input1 == 'q':
            print("Goodbye!")
            break
        try:
            num1 = float(user_input1)
        except ValueError:
            print("Invalid input! Please enter a valid number.")
            continue

    choice = input("Operator (+, -, *, /): ").strip().lower()
    if choice == 'q':
        print("Goodbye!")
        break
    if choice not in ('+', '-', '*', '/'):
        print("Invalid operator! Starting over.")
        continue

    user_input2 = input("Second number: ").strip().lower()
    if user_input2 == 'q':
        print("Goodbye!")
        break
    try:
        num2 = float(user_input2)
    except ValueError:
        print("Invalid input! Starting over.")
        continue

    if choice == '+':
        result = add(num1, num2)
    elif choice == '-':
        result = subtract(num1, num2)
    elif choice == '*':
        result = multiply(num1, num2)
    elif choice == '/':
        result = divide(num1, num2)

    if isinstance(result, str):
        print(result)
    else:
        print(f"Result: {num1} {choice} {num2} = {result}")
        last_result = result
