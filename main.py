import hashlib
import mode
from colorama import *
from pathlib import Path

## colorama reintialise apres chaque impression
init(autoreset=True)

mode.menu()
    

while True:
    command = input("choose a mode : ").lower()
    if command == "text":
        try:
            text = input("text : ")
            text_command= input("text_hasher_methods ? >> ")
            text_command = text_command.lower()
            
            if text_command == "":
                print(Fore.RED + "empty text")
            
            if text == "":
                print(Fore.RED + "empty text code is :  ")
            
            elif text_command == "md5":
                hash_text = hashlib.md5(text.encode()).hexdigest()
                print(Fore.GREEN + f"md5 : {hash_text}")
                
            elif text_command == "sha1":
                hash_text = hashlib.sha1(text.encode()).hexdigest()
                print(Fore.GREEN + f"sha1 : {hash_text}")
                
                
            elif text_command == "sha256":
                hash_text = hashlib.sha256(text.encode()).hexdigest()
                print(Fore.GREEN + f"sha256 : {hash_text}")
            
            
            elif text_command == "sha512":
                hash_text = hashlib.sha512(text.encode()).hexdigest()
                print(Fore.GREEN + f"sha512 : {hash_text}")
            
            
            elif text_command == "sha512.224":
                hash_text = hashlib.sha3_224(text.encode()).hexdigest()
                print(Fore.GREEN + f"sha512.224 : {hash_text}")
            
            
            elif text_command == "sha512.256":
                hash_text = hashlib.sha3_256(text.encode()).hexdigest()
                print(Fore.GREEN + f"sha512.256 : {hash_text}")
            
            
            elif text_command == "blake2b":
                hash_text = hashlib.blake2b(text.encode()).hexdigest()
                print(Fore.GREEN + f"blake2b : {hash_text}")
            
            
            elif text_command == "blake2s":
                hash_text = hashlib.blake2s(text.encode()).hexdigest()
                print(Fore.GREEN + f"blake2s : {hash_text}")
            
            
        except:
            print(Fore.MAGENTA + "error, restart the program and read the help command")
            break
        
    
    elif command == "leave":
        break

    elif command == "help":
        print(mode.help())
    
    else:
        print("error, run help")
