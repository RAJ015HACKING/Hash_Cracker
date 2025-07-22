import hashlib
import itertools
import string
from concurrent.futures import ThreadPoolExecutor
from tqdm import tqdm
from termcolor import colored
import os

# Clear screen
os.system('cls' if os.name == 'nt' else 'clear')

# Banner
banner = r"""
 ██░ ██  ▄▄▄        ██████  ██░ ██  ▄████▄   ██▀███   ▄▄▄       ▄████▄   ██ ▄█▀▓█████  ██▀███  
▓██░ ██▒▒████▄    ▒██    ▒ ▓██░ ██▒▒██▀ ▀█  ▓██ ▒ ██▒▒████▄    ▒██▀ ▀█   ██▄█▒ ▓█   ▀ ▓██ ▒ ██▒
▒██▀▀██░▒██  ▀█▄  ░ ▓██▄   ▒██▀▀██░▒▓█    ▄ ▓██ ░▄█ ▒▒██  ▀█▄  ▒▓█    ▄ ▓███▄░ ▒███   ▓██ ░▄█ ▒
░▓█ ░██ ░██▄▄▄▄██   ▒   ██▒░▓█ ░██ ▒▓▓▄ ▄██▒▒██▀▀█▄  ░██▄▄▄▄██ ▒▓▓▄ ▄██▒▓██ █▄ ▒▓█  ▄ ▒██▀▀█▄  
░▓█▒░██▓ ▓█   ▓██▒▒██████▒▒░▓█▒░██▓▒ ▓███▀ ░░██▓ ▒██▒ ▓█   ▓██▒▒ ▓███▀ ░▒██▒ █▄░▒████▒░██▓ ▒██▒
 ▒ ░░▒░▒ ▒▒   ▓▒█░▒ ▒▓▒ ▒ ░ ▒ ░░▒░▒░ ░▒ ▒  ░░ ▒▓ ░▒▓░ ▒▒   ▓▒█░░ ░▒ ▒  ░▒ ▒▒ ▓▒░░ ▒░ ░░ ▒▓ ░▒▓░
 ▒ ░▒░ ░  ▒   ▒▒ ░░ ░▒  ░ ░ ▒ ░▒░ ░  ░  ▒     ░▒ ░ ▒░  ▒   ▒▒ ░  ░  ▒   ░ ░▒ ▒░ ░ ░  ░  ░▒ ░ ▒░
 ░  ░░ ░  ░   ▒   ░  ░  ░   ░  ░░ ░░          ░░   ░   ░   ▒   ░        ░ ░░ ░    ░     ░░   ░ 
 ░  ░  ░      ░  ░      ░   ░  ░  ░░ ░         ░           ░  ░░ ░      ░  ░      ░  ░   ░     
                                   ░                           ░                               
"""
print(colored(banner, 'red', attrs=['bold']))

# Supported hashes
hash_name = [
    'md5', 'sha1', 'sha224', 'sha256', 'sha384',
    'sha3_224', 'sha3_256', 'sha3_384', 'sha3_512', 'sha512'
]

# Prompt user for details
target_hash = input(colored("Enter hash to crack: ", "cyan")).strip()
mode = input(colored("Choose mode - (1) Wordlist or (2) Brute Force: ", "cyan")).strip()
hash_type = input(colored("Enter hash type (e.g., md5): ", "cyan")).strip().lower()

if hash_type not in hash_name:
    print(colored(f"[!] Unsupported hash type: {hash_type}", "red"))
    exit()

# Wordlist mode
if mode == "1":
    wordlist = input(colored("Enter path to wordlist: ", "cyan")).strip()
    try:
        with open(wordlist, 'r', encoding='utf-8', errors='ignore') as f:
            passwords = f.readlines()
    except FileNotFoundError:
        print(colored("[!] Wordlist file not found!", "red"))
        exit()

    print(colored(f"[*] Starting dictionary attack with {len(passwords)} passwords...", "yellow"))
    hash_fn = getattr(hashlib, hash_type)

    with ThreadPoolExecutor() as executor:
        futures = {executor.submit(lambda p: hash_fn(p.encode()).hexdigest() == target_hash, pwd.strip()): pwd.strip() for pwd in passwords}
        for future in tqdm(futures, total=len(futures), desc="Cracking"):
            if future.result():
                print(colored(f"[+] Password found: {futures[future]}", "green"))
                exit()
    print(colored("[!] Password not found in wordlist.", "red"))

# Brute-force mode
elif mode == "2":
    min_len = int(input(colored("Enter minimum length: ", "cyan")))
    max_len = int(input(colored("Enter maximum length: ", "cyan")))
    charset = input(colored("Characters to use (leave blank for default a-zA-Z0-9): ", "cyan")).strip()
    if not charset:
        charset = string.ascii_letters + string.digits

    total_combinations = sum(len(charset)**i for i in range(min_len, max_len+1))
    print(colored(f"[*] Brute-force will try {total_combinations} combinations...", "yellow"))
    hash_fn = getattr(hashlib, hash_type)

    with ThreadPoolExecutor() as executor:
        with tqdm(total=total_combinations, desc="Cracking") as pbar:
            for length in range(min_len, max_len+1):
                for pwd_tuple in itertools.product(charset, repeat=length):
                    pwd = ''.join(pwd_tuple)
                    if hash_fn(pwd.encode()).hexdigest() == target_hash:
                        print(colored(f"[+] Password found: {pwd}", "green"))
                        exit()
                    pbar.update(1)
    print(colored("[!] Password not found via brute-force.", "red"))

else:
    print(colored("[!] Invalid mode selected.", "red"))


