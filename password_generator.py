import random
import string

def generate_password(length, level):
    """Generate a password based on length and strength level."""
    
    # Define character sets for each level
    if level == 1:  # Easy
        characters = string.ascii_lowercase
    elif level == 2:  # Medium
        characters = string.ascii_letters + string.digits
    elif level == 3:  # Strong
        characters = string.ascii_letters + string.digits + string.punctuation
    else:
        raise ValueError("Invalid choice! Level must be 1, 2, or 3.")
    
    # Use SystemRandom for cryptographic security
    secure_random = random.SystemRandom()
    password = ''.join(secure_random.choice(characters) for _ in range(length))
    return password

def main():
    print("=== Password Generator ===")
    print("1. Easy (only lowercase letters)")
    print("2. Medium (letters + digits)")
    print("3. Strong (letters + digits + symbols)")

    try:
        level = int(input("Enter the level of your choice (1-3): "))
        length = int(input("Enter the length of your password: "))
        if length <= 0:
            raise ValueError("Length must be a positive integer.")
    except ValueError as e:
        print("Error:", e)
        return

    password = generate_password(length, level)
    print("\nYour password is ready:", password)

if __name__ == "__main__":
    main()

