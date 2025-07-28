# 📻 Morse Code Converter

# Dictionary mapping characters to their Morse code equivalent
MORSE_CODE_DICT = {
    'A': '.-', 'B': '-...', 'C': '-.-.', 'D': '-..', 'E': '.', 'F': '..-.',
    'G': '--.', 'H': '....', 'I': '..', 'J': '.---', 'K': '-.-', 'L': '.-..',
    'M': '--', 'N': '-.', 'O': '---', 'P': '.--.', 'Q': '--.-', 'R': '.-.',
    'S': '...', 'T': '-', 'U': '..-', 'V': '...-', 'W': '.--', 'X': '-..-',
    'Y': '-.--', 'Z': '--..',
    '1': '.----', '2': '..---', '3': '...--', '4': '....-', '5': '.....',
    '6': '-....', '7': '--...', '8': '---..', '9': '----.', '0': '-----',
    ',': '--..--', '.': '.-.-.-', '?': '..--..', '/': '-..-.', '-': '-....-',
    '(': '-.--.', ')': '-.--.-', ' ': '/'
}

def text_to_morse(text):
    """
    Converts a string of text into Morse code.
    
    Args:
        text (str): The input string to be converted.
        
    Returns:
        str: The Morse code representation of the input string.
    """
    morse_code = []
    # Convert the input text to uppercase for consistent mapping
    for char in text.upper():
        # Look up the character in the dictionary
        # .get() returns None if the character is not found, effectively ignoring it
        morse_char = MORSE_CODE_DICT.get(char)
        if morse_char:
            morse_code.append(morse_char)
            
    # Join the list of Morse code characters with a space in between
    return ' '.join(morse_code)

# Main part of the program to execute
if __name__ == "__main__":
    try:
        # Prompt the user for input
        input_text = input("Enter text to convert to Morse Code: ")
        
        # Check if the input is empty
        if not input_text.strip():
             print("\n You didn't enter any text. Please try again.")
        else:
            # Call the function to perform the conversion
            morse_result = text_to_morse(input_text)
            
            # Print the results
            print("\n------------------------------------")
            print(f"Original Text: {input_text}")
            print(f"Morse Code: {morse_result}")
            print("------------------------------------")
            
    except KeyboardInterrupt:
        print("\n\nProgram execution cancelled by user. Goodbye!")