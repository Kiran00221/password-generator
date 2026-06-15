import random
import string


def generate_password(length: int, use_digits: bool, use_symbols: bool) -> str:
    characters = string.ascii_letters

    if use_digits:
        characters += string.digits
    if use_symbols:
        characters += string.punctuation

    return "".join(random.choice(characters) for _ in range(length))


def check_strength(length: int, use_digits: bool, use_symbols: bool) -> str:
    if length < 8:
        return "Weak"

    score = 0

    if length <= 12:
        score += 1
    else:
        score += 2

    if use_digits:
        score += 1
    if use_symbols:
        score += 1

    if score <= 1:
        return "Weak"
    elif score <= 3:
        return "Medium"
    else:
        return "Strong"


def main():
    print("=== Password Generator ===\n")

    length = int(input("Password length: "))
    use_digits = input("Include numbers? (y/n): ").lower() == "y"
    use_symbols = input("Include symbols? (y/n): ").lower() == "y"
    count = int(input("How many passwords? "))

    strength = check_strength(length, use_digits, use_symbols)

    print()
    for i in range(count):
        password = generate_password(length, use_digits, use_symbols)
        print(f"Password {i + 1}: {password}")
        print(f"Strength: {strength}")


if __name__ == "__main__":
    main()
