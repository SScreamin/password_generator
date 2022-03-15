"""Password Generator

This script generates a 16 character password.

This script does accept any parameters.

Requires `random` to be installed within your Python environment.

This script can be imported as a module and contains the following functions:
    * generate_password - generates and returns the 16 character password
"""

import random

# Dictionary containing all elements used to generate password
password_elements = {
    'lowercase_letters': ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o','p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z'],
    'uppercase_letters': ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O','P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'],
    'numbers': ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9'],
    'symbols': ['!', '@', '#', '$', '%', '^', '^', '&', '*']
}

def generate_password():
    """Generates a 16 character password.

    This function does not accept any parameters.

    Returns
    -------
    string
        The generated password is returned.
    """
    password = ''

    for i in range(16):
        selected_element = random.choice(list(password_elements.values()))
        selected_character = random.choice(selected_element)
        password += selected_character

    return password

def main():
    print(generate_password())

if __name__ == '__main__':
    main()