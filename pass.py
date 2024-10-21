import string
import random

def PasswordGen():
    upper = string.ascii_uppercase
    lower = string.ascii_lowercase
    digits = string.digits
    punctuations = string.punctuation
    
    # User input for password strength
    passStrength = input("What is your preferred strength: STRONG, VERY STRONG, EXTREMELY STRONG? ").upper()
    
    # Create a character pool for the password
    char_pool = list(upper + lower + digits + punctuations)
    
    # Checking strength preference and assign password length
    if passStrength == "STRONG":
        length = 7
    elif passStrength == "VERY STRONG":
        length = 12
    elif passStrength == "EXTREMELY STRONG":
        length = 15
    else:
        print("Invalid input")
        return
    
    # Shuffling the character pool and  generate a password afterwards
    random.shuffle(char_pool)
    genPassword = "".join(random.choice(char_pool) for _ in range(length))
    
    # Displaying the generated password
    print(f"Your {passStrength} password is: {genPassword}")


PasswordGen()
