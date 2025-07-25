# encryptor.py

from cryptography.fernet import Fernet
import bcrypt
import os

def generate_key_from_password(password, salt=None):
    """
    Generates an encryption key from a password using bcrypt hashing.
    If no salt is provided, a new one is generated.
    Returns (key, salt).
    """
    if salt is None:
        salt = bcrypt.gensalt()
    
    # Hash the password to get a consistent length key material
    hashed_password = bcrypt.hashpw(password.encode('utf-8'), salt)
    
    # Use the first 32 bytes (256 bits) of the hashed password as the Fernet key.
    # Fernet requires a URL-safe base64 encoded key of 32 bytes.
    # We'll use a simple conversion here for demonstration.
    # In a real-world scenario, you might use PBKDF2HMAC for key derivation.
    
    # For Fernet, the key MUST be 32 URL-safe base64-encoded bytes.
    # Let's derive a 32-byte key from the hashed password for Fernet.
    # A more robust way would be to use KDF like PBKDF2HMAC.
    # For simplicity and demonstration, we'll use a part of the bcrypt hash.
    # NOTE: This is a simplified key derivation. For production, use `cryptography.hazmat.primitives.kdf.pbkdf2.PBKDF2HMAC`.
    key_material = hashed_password[:32] # Take first 32 bytes
    key = Fernet(base64.urlsafe_b64encode(key_material))
    
    return key, salt

def encrypt_file(filepath, password):
    """Encrypts a given file using a password-derived key."""
    salt = bcrypt.gensalt() # Generate a new salt for each encryption
    f, salt_used = generate_key_from_password(password, salt)
    
    with open(filepath, "rb") as file:
        file_data = file.read()
    
    encrypted_data = f.encrypt(file_data)
    
    # Save the encrypted data along with the salt (needed for decryption)
    encrypted_filepath = filepath + ".encrypted"
    with open(encrypted_filepath, "wb") as file:
        # Prepend the salt to the encrypted data
        file.write(salt_used + b"\n" + encrypted_data) 
        
    print(f"File '{filepath}' encrypted to '{encrypted_filepath}' with salt: {salt_used.hex()}")

def decrypt_file(filepath, password):
    """Decrypts a given file using a password."""
    try:
        with open(filepath, "rb") as file:
            content = file.read()
            # Find the first newline to separate salt from encrypted data
            first_newline_index = content.find(b"\n")
            if first_newline_index == -1:
                raise ValueError("Invalid encrypted file format: Salt not found.")
            
            salt = content[:first_newline_index]
            encrypted_data = content[first_newline_index + 1:]

        f, _ = generate_key_from_password(password, salt)
        
        decrypted_data = f.decrypt(encrypted_data)
        
        original_filepath = filepath.replace(".encrypted", "")
        with open(original_filepath, "wb") as file:
            file.write(decrypted_data)
        
        print(f"File '{filepath}' decrypted to '{original_filepath}'")

    except Exception as e:
        print(f"Decryption failed: {e}")
        print("Please ensure the correct password and that the file is not corrupted.")

if __name__ == "__main__":
    # --- Installation Check ---
    try:
        import bcrypt
        from cryptography.fernet import Fernet
        import base64 # Required for key conversion
    except ImportError:
        print("Required libraries not found. Please install them:")
        print("pip install bcrypt cryptography")
        exit()

    # --- Basic CLI for demonstration ---
    print("\n--- File Encryptor/Decryptor ---")
    
    while True:
        action = input("\nChoose action (e for encrypt, d for decrypt, q for quit): ").lower()
        
        if action == 'e':
            file_to_encrypt = input("Enter the path to the file to encrypt: ")
            if not os.path.exists(file_to_encrypt):
                print("File not found.")
                continue
            password = input("Enter a password for encryption: ")
            encrypt_file(file_to_encrypt, password)
        
        elif action == 'd':
            file_to_decrypt = input("Enter the path to the .encrypted file: ")
            if not os.path.exists(file_to_decrypt):
                print("File not found.")
                continue
            password = input("Enter the password for decryption: ")
            decrypt_file(file_to_decrypt, password)
            
        elif action == 'q':
            print("Exiting.")
            break
            
        else:
            print("Invalid action. Please choose 'e', 'd', or 'q'.")