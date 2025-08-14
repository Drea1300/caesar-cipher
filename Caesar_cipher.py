# Ask the user for their text and shift value
text = input("Enter the message you want to encrypt: ")
shift = int(input("Enter the shift value (e.g., 3): "))

def caesar(message, offset):
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    encrypted_text = ''

    for char in message.lower():
        if char == ' ':
            encrypted_text += char
        else:
            index = alphabet.find(char)
            # Only encrypt letters in the alphabet
            if index != -1:
                new_index = (index + offset) % len(alphabet)
                encrypted_text += alphabet[new_index]
            else:
                encrypted_text += char  # Keep punctuation/numbers unchanged

    print('plain text:', message)
    print('encrypted text:', encrypted_text)

# Run the cipher
caesar(text, shift)
