import secrets
import string


def generate_password():
    print("🔑 --- Command-Line Password Generator --- 🔑\n")

    # 1. User Input Validation for Length
    while True:
        try:
            length = int(input("Enter password length (e.g., 8, 12, 16): "))
            if length <= 0:
                print("Please enter a positive number.")
                continue
            break
        except ValueError:
            print("Invalid input! Please enter a valid number.")

    # 2. Character Set Preferences
    character_pool = ""
    print("\nSelect character types to include:")

    if input("Include uppercase letters? (y/n): ").lower() == "y":
        character_pool += string.ascii_uppercase
    if input("Include lowercase letters? (y/n): ").lower() == "y":
        character_pool += string.ascii_lowercase
    if input("Include numbers? (y/n): ").lower() == "y":
        character_pool += string.digits
    if input("Include symbols? (y/n): ").lower() == "y":
        character_pool += "!@#$%^&*()_+"

    # 3. Fallback Handling
    if not character_pool:
        print(
            "\n⚠️ No options selected. Defaulting to lowercase letters for safety."
        )
        character_pool = string.ascii_lowercase

    # 4. Randomization
    password = "".join(secrets.choice(character_pool) for _ in range(length))

    print(f"\n✨ Generated Password: {password}\n")


if __name__ == "__main__":
    generate_password()