import subprocess
import sys
import os


def launch_password_generator(dob, name, special_name, min_char, max_char, temp_file):
    # Get the absolute path of the launcher script
    script_dir = os.path.dirname(os.path.abspath(__file__))
    

    # Construct the command to run the password generation script
    command = ["python", os.path.join(script_dir, "passwriter.py"), dob, name, special_name, min_char, max_char]
    cmd2 = ["python", os.path.join(script_dir, "passwriter_v2.py"), dob, name, special_name, min_char, max_char]
    # Launch the subprocess
    subprocess.call(command)
    subprocess.call(cmd2)

def main():
    # Check if the correct number of arguments are provided
    if len(sys.argv) != 7:
        print("Usage: python passlistmaker.py <DOB> <Name> <SpecialName> <MinChar> <MaxChar> <TemplatesFile>")
        sys.exit(1)

    # Extract command line arguments
    dob = sys.argv[1]
    name = sys.argv[2]
    special_name = sys.argv[3]
    min_char = sys.argv[4]
    max_char = sys.argv[5]
    temp_file = sys.argv[6]

    # Launch the password generator with the provided inputs
    launch_password_generator(dob, name, special_name, min_char, max_char, temp_file)

if __name__ == "__main__":
    main()
