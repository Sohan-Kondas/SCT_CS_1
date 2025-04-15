def caesar_encrypt(text, shift):
    encrypted = ""
    for char in text:
        if char.isalpha():
            start = ord('A') if char.isupper() else ord('a')
            encrypted += chr((ord(char) - start + shift) % 26 + start)
        else:
            encrypted += char
    return encrypted

def caesar_decrypt(text, shift):
    return caesar_encrypt(text, -shift)

def main():
    print("Caesar Cipher Encryption/Decryption")
    choice = input("Do you want to (E)ncrypt or (D)ecrypt? ").strip().upper()
    message = input("Enter your message: ")
    shift = int(input("Enter shift value: "))

    if choice == 'E':
        result = caesar_encrypt(message, shift)
        print("Encrypted message:", result)
    elif choice == 'D':
        result = caesar_decrypt(message, shift)
        print("Decrypted message:", result)
    else:
        print("Invalid choice. Please choose E or D.")

if __name__ == "__main__":
    main()
