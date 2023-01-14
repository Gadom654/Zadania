import random

DIGITS = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9'] 
LOCASE_CHARACTERS = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h',
                     'i', 'j', 'k', 'm', 'n', 'o', 'p', 'q',
                     'r', 's', 't', 'u', 'v', 'w', 'x', 'y',
                     'z']
 
UPCASE_CHARACTERS = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H',
                     'I', 'J', 'K', 'M', 'N', 'O', 'P', 'Q',
                     'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y',
                     'Z']
 
SYMBOLS = ['@', '#', '$', '%', '=', ':', '?', '.', '/', '|', '~', '>',
           '*', '(', ')', '<']

def randomPasswordGenerator():
    password = ""
    while True:
        if len(password) < 8:
            password += random.choice(DIGITS + LOCASE_CHARACTERS + UPCASE_CHARACTERS +SYMBOLS)
        elif any(ele in password for ele in DIGITS) == False:
            password += random.choice(DIGITS + LOCASE_CHARACTERS + UPCASE_CHARACTERS +SYMBOLS)
        elif any(ele in password for ele in UPCASE_CHARACTERS) == False:
            password += random.choice(DIGITS + LOCASE_CHARACTERS + UPCASE_CHARACTERS +SYMBOLS)
        elif any(ele in password for ele in LOCASE_CHARACTERS) == False:
            password += random.choice(DIGITS + LOCASE_CHARACTERS + UPCASE_CHARACTERS +SYMBOLS)
        elif any(ele in password for ele in SYMBOLS) == False:
            password += random.choice(DIGITS + LOCASE_CHARACTERS + UPCASE_CHARACTERS +SYMBOLS)
        else:
            break
    return password
password = randomPasswordGenerator()
print(password)
