#random password generator

import random
import  string

def generate_pass( min_len , numbers =True , symbols =True):
    letters = string.ascii_letters 
    digits = string.digits
    special = string.punctuation

    character = letters
    if numbers:
        character +=  digits
    if symbols:
        character += special
    pwd=""
    meets_criteria = False
    has_number = False
    has_special = False

    while not  meets_criteria or len(pwd) < min_len :
        new_char = random.choice(character)
        pwd += new_char

        if new_char in digits:
            has_number = True
        elif new_char in special:
            has_special=True
        
        meets_criteria = True
        if numbers:
            meets_criteria = has_number
        if symbols:
            meets_criteria = meets_criteria and has_special
    return pwd

min_length = int(input("minimum length of passward you want to have : "))
has_number = input("do you want your password to have number ? (y/n) : ").lower() == "y"
has_special = input("do you want your password to have special chaacter ? (y/n) : ").lower() == "y"

pwd = generate_pass(min_length , has_number , has_special)
print(pwd)