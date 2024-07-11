import sys
import itertools
import random
import os


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

def generate_passwords(dob, name, special_name, min_length, max_length):
    dob_parts = dob.split('-')
    year = dob_parts[0]
    month = dob_parts[1]
#    date = dob_parts[2]

    # Generate variations of different lengths and combinations
    passwords = set()

    # Short passwords
    short_combinations = [name, special_name, year, month]
    for item in short_combinations:
        password = item
        # Apply character substitutions
        substituted_passwords = apply_substitutions(password)
        for p in substituted_passwords:
            for i in range(len(p) + 1):
                capitalized_password = p[:i] + p[i:].capitalize()
                passwords.add(capitalized_password)

    # Medium-length passwords
    name_combinations = [name, special_name]
    for length in range(min_length - 2, min(len(name) + len(special_name) + 1, max_length - 2) + 1):
        for combination in itertools.permutations(name_combinations, length):
            password = ''.join(combination)
            # Apply character substitutions
            substituted_passwords = apply_substitutions(password)
            for p in substituted_passwords:
                for i in range(len(p) + 1):
                    capitalized_password = p[:i] + p[i:].capitalize()
                    passwords.add(capitalized_password)

    # Long passwords
    name_combinations = [name, special_name, name+year, special_name+year]
    for length in range(min_length, min(len(name + year) + len(special_name + year) + 1, max_length + 1)):
        for combination in itertools.permutations(name_combinations, length):
            password = ''.join(combination)
            # Apply character substitutions
            substituted_passwords = apply_substitutions(password)
            for p in substituted_passwords:
                for i in range(len(p) + 1):
                    capitalized_password = p[:i] + p[i:].capitalize()
                    passwords.add(capitalized_password)

    # Add common number variations and random capitalization
    common_numbers = ['00', '110', '100', '123', '321', '666', '777', '888', '999','.',"69","6996","789","0123","sex","{","}","[","]","#","%","1","2","3","4","5","6","7","8","9"]
    for num in common_numbers:
        for password in passwords.copy():
            passwords.add(num + password)
            passwords.add(password + num)
            for i in range(len(password)):
                passwords.add(password[:i] + password[i:].capitalize())

    # Remove passwords shorter than the minimum length
    passwords = {password for password in passwords if min_length <= len(password) <= max_length}

    return passwords

def main():
    if len(sys.argv) != 6:
        print("Usage: python passwordwriter.py <DOB> <Name> <SpecialName> <MinChar> <MaxChar>")
        sys.exit(1)

    dob = sys.argv[1]
    name = sys.argv[2]
    special_name = sys.argv[3]
    min_length = int(sys.argv[4])
    max_length = int(sys.argv[5])

    passwords = generate_passwords(dob, name, special_name, min_length, max_length)
    
    # Get the current working directory
    current_directory = os.getcwd()

    # Move one level up to place the password.txt file
    parent_directory = os.path.dirname(current_directory)

    # Construct the path for the password.txt file
    password_file_path = os.path.join(current_directory, "passwordlist.txt")

    with open(password_file_path, "a") as file:
        for password in passwords:
            file.write(password + "\n")

    print("Passwords saved to 'passwordlist.txt'.")

if __name__ == "__main__":
    print("Password Writer -2 Was launched")
    main()

