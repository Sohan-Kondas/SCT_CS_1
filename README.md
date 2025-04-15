# SCT_CS_1
# Caesar Cipher Encryption/Decryption Program

This repository contains a simple Python program that implements the Caesar Cipher algorithm for encrypting and decrypting text. This was my first task as a Cyber Security Intern at SkillCraft Technology.

## Overview

The Caesar Cipher is a basic substitution cipher where each letter in the plaintext is shifted a fixed number of positions down the alphabet. This program allows users to:

- **Encrypt** a given message using a specified shift value.
- **Decrypt** a Caesar Cipher encrypted message using the corresponding shift value.

## How to Use

1.  **Clone the repository** (if you haven't already):
    ```bash
    git clone <repository_url>
    cd caesar-cipher
    ```

2.  **Run the Python script:**
    ```bash
    python caesar_cipher.py
    ```

3.  **Follow the on-screen prompts:**
    - The program will ask you to choose between encryption and decryption.
    - You will then be prompted to enter the message.
    - Finally, you will be asked to enter the shift value (an integer).

4.  **The program will output the encrypted or decrypted text.**

## Algorithm Details

The Caesar Cipher works by taking each letter in the input text and shifting it by a constant number of positions down the alphabet.

-   **Encryption:** For each letter, its position in the alphabet is determined. This position is then shifted by the provided shift value. To wrap around the alphabet (e.g., shifting 'Z' by 1), the modulo operator (%) is used with the alphabet length (26).

    $\text{Ciphertext Letter} = (\text{Plaintext Letter Position} + \text{Shift Value}) \mod 26$

-   **Decryption:** To decrypt, the process is reversed. The position of each letter in the ciphertext is shifted back by the same shift value.

    $\text{Plaintext Letter} = (\text{Ciphertext Letter Position} - \text{Shift Value}) \mod 26$

**Note:** This implementation handles both uppercase and lowercase letters, preserving their case. Non-alphabetic characters (spaces, punctuation, etc.) remain unchanged.

## Example

**Encryption:**

-   **Plaintext:** `Hello World`
-   **Shift Value:** `3`
-   **Ciphertext:** `Khoor Zruog`

**Decryption:**

-   **Ciphertext:** `Khoor Zruog`
-   **Shift Value:** `3`
-   **Plaintext:** `Hello World`

## Further Improvements (Optional)

This is a basic implementation of the Caesar Cipher. Potential improvements could include:

-   Adding error handling for invalid input (e.g., non-integer shift values).
-   Implementing a more user-friendly interface.
-   Exploring other classical ciphers.

## Author

Sohan Kondas

This project was completed as part of my Cyber Security Internship at SkillCraft Technology.
