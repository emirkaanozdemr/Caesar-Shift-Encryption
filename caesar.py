from secretpy import Caesar

# Initialize the required Python object for Caesar shift encryption
caesar_cipher = Caesar()

# Define the shift value, i.e., the key
caesar_key = int(input("Shift Key Value: "))
print(f"Caesar shift secret key: {caesar_key}")

# Define the alphabet - for English
alphabet = ('a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', ' ')
print(f"Alphabet: {alphabet}")

# Define the plaintext to be encrypted
plaintext = input("Enter plaintext: ")

# Encrypt the plaintext to get ciphertext for the Caesar cipher
caesar_ciphertext = caesar_cipher.encrypt(plaintext, caesar_key, alphabet)
print(f"Encrypted Caesar shift ciphertext: {caesar_ciphertext}")

# Decrypt the ciphertext back to the original plaintext using the same key used for encryption
caesar_plaintext = caesar_cipher.decrypt(caesar_ciphertext, caesar
