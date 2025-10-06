import random
import string


def generate_password(length=12, use_uppercase=True, use_lowercase=True,
                     use_digits=True, use_special=True):
    """
    Generate a random password based on criteria.

    Args:
        length (int): Length of the password
        use_uppercase (bool): Include uppercase letters
        use_lowercase (bool): Include lowercase letters
        use_digits (bool): Include digits
        use_special (bool): Include special characters

    Returns:
        str: Generated password
    """
    characters = ""
    required_chars = []

    if use_lowercase:
        characters += string.ascii_lowercase
        required_chars.append(random.choice(string.ascii_lowercase))
    if use_uppercase:
        characters += string.ascii_uppercase
        required_chars.append(random.choice(string.ascii_uppercase))
    if use_digits:
        characters += string.digits
        required_chars.append(random.choice(string.digits))
    if use_special:
        characters += string.punctuation
        required_chars.append(random.choice(string.punctuation))

    if not characters:
        return "Error: No character types selected!"

    if length < len(required_chars):
        return "Error: Length too short for selected character types!"

    password = required_chars.copy()
    password += [random.choice(characters) for _ in range(length - len(required_chars))]
    random.shuffle(password)

    return ''.join(password)


def password_strength(password):
    """
    Rate password strength from 1-5.

    Args:
        password (str): Password to evaluate

    Returns:
        str: Strength rating
    """
    score = 0

    if len(password) >= 8:
        score += 1
    if len(password) >= 12:
        score += 1
    if any(c.islower() for c in password):
        score += 1
    if any(c.isupper() for c in password):
        score += 1
    if any(c.isdigit() for c in password):
        score += 1

    strength = ["Very Weak", "Weak", "Fair", "Good", "Strong", "Very Strong"]
    return strength[min(score, 5)]


def get_bool_input(prompt, default=True):
    """
    Helper function to get yes/no user input.

    Args:
        prompt (str): The prompt to show the user.
        default (bool): Default value if user presses enter.

    Returns:
        bool: True for yes, False for no.
    """
    default_str = "Y/n" if default else "y/N"
    choice = input(f"{prompt} ({default_str}): ").strip().lower()
    if choice == '':
        return default
    return choice in ['y', 'yes']


def main():
    """Main function to run the password generator."""
    print("🔐 Password Generator")
    print("-" * 30)

    # Get password length from user
    length_input = input("Password length (default 12): ").strip()
    try:
        length = int(length_input) if length_input else 12
    except ValueError:
        print("Invalid length. Using default length 12.")
        length = 12

    # Ask user for character options
    use_upper = get_bool_input("Include uppercase letters?", True)
    use_lower = get_bool_input("Include lowercase letters?", True)
    use_digits = get_bool_input("Include digits?", True)
    use_special = get_bool_input("Include special characters?", True)

    # Generate password
    password = generate_password(length, use_upper, use_lower, use_digits, use_special)
    print(f"\n🔑 Generated Password: {password}")
    print(f"🔎 Strength: {password_strength(password)}")

    # Generate alternative passwords
    print("\n🔁 Alternative passwords:")
    for i in range(3):
        alt = generate_password(length, use_upper, use_lower, use_digits, use_special)
        print(f"{i+1}. {alt} ({password_strength(alt)})")


if __name__ == "__main__":
    main()