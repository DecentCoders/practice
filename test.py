def caesar_cipher(text, shift):
    result = ""
    for char in text:
        if char.isalpha(): # Only shift letters
            start = ord('a') if char.islower() else ord('A')
            # The modulo 26 ensures we wrap around from Z back to A
            new_char = chr(start + (ord(char) - start + shift) % 26)
            result += new_char
        else:
            result += char # Keep spaces and punctuation as they are
    return result

message = "Hello World!"
encrypted = caesar_cipher(message, 3)
print(f"Original: {message}")
print(f"Encrypted: {encrypted}") # Khoor Zruog!