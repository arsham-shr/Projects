import random

def generate_password(length):
    characters = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890!@#$%^&*()"
    password = ""
    for _ in range(length):
        password += random.choice(characters)
    return password

length = int(input("Enter the length of the password: "))
print("Generated Password:", generate_password(length))
