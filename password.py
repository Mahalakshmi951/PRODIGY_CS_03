import re

def assess_password_strength(password):
    #Define criteria
    length_criteria = len(password) >= 8
    uppercase_criteria = any(char.isupper() for char in password)
    lowercase_criteria = any(char.islower() for char in password)
    digit_criteria = any(char.isdigit() for char in password)
    special_char_criteria = re.search(r"[!@#$%^&*(),.?\":{}|<>]", password)
    #Asses strength
    strength = 0
    if length_criteria:
        strength += 1
    if uppercase_criteria:
        strength += 1
    if lowercase_criteria:
        strength += 1
    if digit_criteria:
        strength += 1
    if special_char_criteria:
        strength += 1

    #provide criteria
    if strength == 5:
        return "Strong Password"
    elif strength >= 3:
        return "Moderate Password"
    else:
        return "Weak Password"

#main function
if __name__ == "__main__":
    print("Password Complexity Checker")
    password = input("Enter your password: ")
    feedback = assess_password_strength(password)
    print(feedback)
