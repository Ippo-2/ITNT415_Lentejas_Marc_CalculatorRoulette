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
    if b == 0:
        return "Error: Division by zero is not allowed."
    return a / b

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
