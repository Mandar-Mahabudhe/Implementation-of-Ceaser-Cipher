def caesar_cipher(text, shift, mode):
    encrypted_text = ''
    for char in text:
        if char.isalpha():  # Check if the character is a letter
            if char.islower():
                shifted = (ord(char) - ord('a') + shift) % 26 + ord('a')
            else:
                shifted = (ord(char) - ord('A') + shift) % 26 + ord('A')
            encrypted_text += chr(shifted)
        else:
            encrypted_text += char
    return encrypted_text

def encrypt(text, shift):
    return caesar_cipher(text, shift, 'encrypt')

def decrypt(text, shift):
    return caesar_cipher(text, shift, 'decrypt')

def get_valid_shift():
    while True:
        try:
            shift = int(input("Enter the shift value (a number between 1 and 25): "))
            if 1 <= shift <= 25:
                return shift
            else:
                print("Shift value must be between 1 and 25.")
        except ValueError:
            print("Invalid input. Please enter a number.")

def main():
    while True:
        message = input("Enter the message to encrypt/decrypt (or 'q' to quit): ")
        if message.lower() == 'q':
            break

        shift = get_valid_shift()

        while True:
            choice = input("Enter 'e' to encrypt or 'd' to decrypt: ")
            if choice.lower() == 'e':
                encrypted_message = encrypt(message, shift)
                print("Encrypted message:", encrypted_message)
                break
            elif choice.lower() == 'd':
                decrypted_message = decrypt(message, shift)
                print("Decrypted message:", decrypted_message)
                break
            else:
                print("Invalid choice. Please enter 'e' or 'd'.")

if __name__ == "__main__":
    main()
