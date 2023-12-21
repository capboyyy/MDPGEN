import random
import string

print("""
▓█████▄ ▓█████ ██▒   █▓ ██▓ ██▓   ▓██   ██▓▒██   ██▒
▒██▀ ██▌▓█   ▀▓██░   █▒▓██▒▓██▒    ▒██  ██▒▒▒ █ █ ▒░
░██   █▌▒███   ▓██  █▒░▒██▒▒██░     ▒██ ██░░░  █   ░
░▓█▄   ▌▒▓█  ▄  ▒██ █░░░██░▒██░     ░ ▐██▓░ ░ █ █ ▒
░▒████▓ ░▒████▒  ▒▀█░  ░██░░██████▒ ░ ██▒▓░▒██▒ ▒██▒
 ▒▒▓  ▒ ░░ ▒░ ░  ░ ▐░  ░▓  ░ ▒░▓  ░  ██▒▒▒ ▒▒ ░ ░▓ ░
 ░ ▒  ▒  ░ ░  ░  ░ ░░   ▒ ░░ ░ ▒  ░▓██ ░▒░ ░░   ░▒ ░
 ░ ░  ░    ░       ░░   ▒ ░  ░ ░   ▒ ▒ ░░   ░    ░
   ░       ░  ░     ░   ░      ░  ░░ ░      ░    ░
 ░                 ░               ░ ░
""")
print("******************************************\n**************** by adxm  ****************\n******************************************")

tool = input("\nChoose an option:\n1 - Password Generator : \n")

if tool == '1':
    def generate_password():
        length = int(input("How many characters do you want in your password? "))
        include_letters = input("Do you want to include letters? (Yes/No) ")
        include_digits = input("Do you want to include digits? (Yes/No) ")
        include_uppercase = input("Do you want to include uppercase letters? (Yes/No) ")
        include_special_characters = input("Do you want to include special characters? (Yes/No) ")

        characters = ''
        if include_letters.lower() == 'yes':
            characters += string.ascii_letters
        if include_digits.lower() == 'yes':
            characters += string.digits
        if include_uppercase.lower() == 'yes':
            characters += string.ascii_uppercase
        if include_special_characters.lower() == 'yes':
            characters += string.punctuation

        password = ''.join(random.choice(characters) for _ in range(length))
        return password

    print("Your generated password is:", generate_password())
else:
    print("Invalid choice. Please choose a valid option.")