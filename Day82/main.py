# 📻 Simple Morse Code Converter

# morse codes dict
MORSE_CODE_MAP = {
    'A': '.-', 'B': '-...', 'C': '-.-.', 'D': '-..', 'E': '.', 'F': '..-.',
    'G': '--.', 'H': '....', 'I': '..', 'J': '.---', 'K': '-.-', 'L': '.-..',
    'M': '--', 'N': '-.', 'O': '---', 'P': '.--.', 'Q': '--.-', 'R': '.-.',
    'S': '...', 'T': '-', 'U': '..-', 'V': '...-', 'W': '.--', 'X': '-..-',
    'Y': '-.--', 'Z': '--..', '1': '.----', '2': '..---', '3': '...--',
    '4': '....-', '5': '.....', '6': '-....', '7': '--...', '8': '---..',
    '9': '----.', '0': '-----',
    ' ': '/'  # A space between words becomes a slash
}

def convert_to_morse(message):
    """Turns a message into a string of morse code."""
    morse_code = []
    for char in message.upper():
        # If the character is in our map, add its morse code to our list
        if char in MORSE_CODE_MAP:
            morse_code.append(MORSE_CODE_MAP[char])
    
    # Join all the morse code parts together with a space
    return ' '.join(morse_code)

# Get some text from the user
user_input = input("Enter a message to convert: ")

# Convert it and show the result
morse_output = convert_to_morse(user_input)

print()
print(f'Your string: {user_input}')
print(f'Morse code: {morse_output}')

