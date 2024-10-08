from colorama import Back, Fore, Style, deinit, init 

init(autoreset=True)
def menu():
    print("""
                                              . . . . .                                              
                                           :*@@@@@@@@@@*:                                          
                                      ..-@@@@@@@@@@@@@@@@@@-..                                      
                                     .-@@@@@@@@@@@@@@@@@@@@@@-.                                     
                                    .@@@@@@@@@@@@@@@@@@@@@@@@@@.                                    
                                   .@@@@@@@@@-........-@@@@@@@@@.                                  
                                  .@@@@@@@@:.          .:@@@@@@@@.                                  
                                  +@@@@@@@.             . @@@@@@@+                                  
                                  @@@@@@@:               .:@@@@@@@                                  
                                  @@@@@@@.                .@@@@@@@                                  
                                  @@@@@@@.                .@@@@@@@                                  
                                  @@@@@@@.                .@@@@@@@                                  
                                  @@@@@@@.                .@@@@@@@                                  
                                  @@@@@@@.                .@@@@@@@                                  
                                  @@@@@@@.                .@@@@@@@                                  
                         ..       @@@@@@@.                .@@@@@@@      ..                          
                          -@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@-                          
                         .@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@                                   
                          @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@                     
                          @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@                          
                          @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@                          
                          @@@@@@@@@@@@@@@@@@@@%.    .%@@@@@@@@@@@@@@@@@@@@                          
                          @@@@@@@@@@@@@@@@@@@@.       @@@@@@@@@@@@@@@@@@@@                          
                          @@@@@@@@@@@@@@@@@@@+        +@@@@@@@@@@@@@@@@@@@                          
                          @@@@@@@@@@@@@@@@@@@@.      .@@@@@@@@@@@@@@@@@@@@                         
                          @@@@@@@@@@@@@@@@@@@@@*    *@@@@@@@@@@@@@@@@@@@@@                                                                           
                          @@@@@@@@@@@@@@@@@@@@@:    :@@@@@@@@@@@@@@@@@@@@@                                                      
                          @@@@@@@@@@@@@@@@@@@@@.    .@@@@@@@@@@@@@@@@@@@@@                          
                          @@@@@@@@@@@@@@@@@@@@@      @@@@@@@@@@@@@@@@@@@@@                          
                          @@@@@@@@@@@@@@@@@@@@=      =@@@@@@@@@@@@@@@@@@@@                          
                          @@@@@@@@@@@@@@@@@@@@        @@@@@@@@@@@@@@@@@@@@                          
                          @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@                          
                          @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@                          
                          @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@                          
                         .@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@.                         
                          .@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@.
          """)


    print(Fore.CYAN + "author : Paw")
    deinit()
    print(Back.RED + "github : pewpewpaw")
    deinit()
    

def help():
    print(f"""{Fore.MAGENTA}methods:                                     
        {Fore.GREEN}MD5                                             
        {Fore.GREEN}SHA1                                          
        {Fore.GREEN}SHA224                                 
        {Fore.GREEN}SHA256
        {Fore.GREEN}SHA384
        {Fore.GREEN}SHA512
        {Fore.GREEN}SHA512.224
        {Fore.GREEN}SHA512.256
        {Fore.GREEN}BLAKE2b
        {Fore.GREEN}BLAKE2s
{Fore.BLUE}firstly choose a command : help / text / leave     
    """)


