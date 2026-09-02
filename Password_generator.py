import string
import secrets

def generate_password(length):
    """Generate a random password of the specified length."""
    characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(secrets.choice(characters) for _ in range(length))
    return password

def main():
    while True:
        try:
            length = int(input("Enter the desired password length: "))
            if length <= 0:
                print("Please enter a positive number.")
                continue
            break
        except ValueError:
            print("Please enter a valid integer.")

    password = generate_password(length)
    print(f"Generated password: {password}")

if __name__ == "__main__":
    main()