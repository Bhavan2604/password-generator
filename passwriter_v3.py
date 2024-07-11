import os
import sys
import re
import random
import itertools

def apply_substitutions(password):
    substitutions = {'a': '@', 'i': '1', 's': '$', 'o': '0'}  # Define common substitutions
    substituted_passwords = [password]  # Start with the original password
    
    for char, substitution in substitutions.items():
        if char in password:
            new_passwords = []
            for p in substituted_passwords:
                new_passwords.append(p.replace(char, substitution))
            substituted_passwords.extend(new_passwords)
    
    return set(substituted_passwords)  # Remove duplicates and return as set

def generate_passwords(template, values):
    # Replace placeholders with provided values
    password = template
    for key, value in values.items():
        password = password.replace("[" + key + "]", value)
    
    # Apply substitutions
    password = apply_substitutions(password).pop()  # Apply substitutions to the first password only

    # Generate all possible combinations of capitalization
    capitalizations = itertools.product(*[(c.upper(), c.lower()) for c in password])

    # Join each capitalization combination into a string
    passwords = [''.join(cap) for cap in capitalizations]

    return passwords

def read_templates(template_file):
    with open(template_file, "r") as file:
        return file.readlines()

def save_passwords_to_file(passwords, file_path):
    with open(file_path, "w") as file:
        for password in passwords:
            file.write(password + "\n")

def main():
    # Check if the correct number of arguments are provided
    if len(sys.argv) != 8:
        print("Usage: python template_password_generator.py <template_file> <dd> <mm> <yyyy> <name> <special_name>")
        sys.exit(1)

    template_file = sys.argv[1]
    output_file = "passwordlist.txt"
    dd = sys.argv[3]
    mm = sys.argv[4]
    yyyy = sys.argv[5]
    name = sys.argv[6]
    special_name = sys.argv[7]

    # Read templates from file
    templates = read_templates(template_file)

    # Generate passwords for each template
    all_passwords = []
    for template in templates:
        # Generate passwords for the template
        passwords = generate_passwords(template, {'dd': dd, 'mm': mm, 'yy': yyyy[-2:], 'name': name, 'special_name': special_name})
        all_passwords.extend(passwords)

    # Save the generated passwords to the output file
    save_passwords_to_file(all_passwords, output_file)

    print("Passwords saved to:",output_file)

if __name__ == "__main__":
    main()
