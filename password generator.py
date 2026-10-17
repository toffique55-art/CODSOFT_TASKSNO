
import secrets
import string

print("===== PASSWORD GENERATOR =====")

try:
    length = int(input("Enter password length: "))

    if length < 1:
        print("Password length must be at least 1.")

    else:
        characters = string.ascii_letters + string.digits + "!@#$%^&*"
        password = ""

        for i in range(length):
            password += secrets.choice(characters)

        print("Your generated password is:", password)

except ValueError:
    print("Please enter a valid number.")
