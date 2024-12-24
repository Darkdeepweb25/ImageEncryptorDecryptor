from Crypto.Cipher import AES
import os

# Function to pad data
def pad(data):
    while len(data) % 16 != 0:
        data += b' '
    return data

# Encrypt image
def encrypt_image(image_path, key):
    cipher = AES.new(key, AES.MODE_EAX)
    nonce = cipher.nonce

    with open(image_path, "rb") as file:
        image_data = file.read()

    ciphertext, tag = cipher.encrypt_and_digest(pad(image_data))

    encrypted_path = "encrypted_image.aes"
    with open(encrypted_path, "wb") as file:
        file.write(nonce + ciphertext)

    print(f"Encrypted image saved at: {encrypted_path}")

# Decrypt image
def decrypt_image(encrypted_path, key):
    with open(encrypted_path, "rb") as file:
        nonce = file.read(16)
        ciphertext = file.read()

    cipher = AES.new(key, AES.MODE_EAX, nonce=nonce)
    decrypted_data = cipher.decrypt(ciphertext).rstrip()

    decrypted_path = "decrypted_image.jpg"
    with open(decrypted_path, "wb") as file:
        file.write(decrypted_data)

    print(f"Decrypted image saved at: {decrypted_path}")

# Main program
if __name__ == "__main__":
    print("=== Image Encryption Program ===")
    action = input("Do you want to (encrypt/decrypt) an image? ").strip().lower()

    key = input("Enter a 16-character key: ").encode()
    if len(key) != 16:
        print("Error: Key must be 16 characters.")
        exit()

    if action == "encrypt":
        image_path = input("Enter the image file path: ").strip()
        encrypt_image(image_path, key)

    elif action == "decrypt":
        encrypted_path = input("Enter the encrypted file path: ").strip()
        decrypt_image(encrypted_path, key)

    else:
        print("Invalid action.")
