import socket
import sys
from colorama import Fore, Style , init

init()

def print_welcome_message():
    print_colored_message("╔═══════════════════════════╗", Fore.LIGHTMAGENTA_EX)
    print_colored_message("║                           ║", Fore.LIGHTMAGENTA_EX)
    print_colored_message("║       Welcome to the      ║", Fore.LIGHTMAGENTA_EX)
    print_colored_message("║         { NABIH }         ║", Fore.LIGHTMAGENTA_EX)
    print_colored_message("║          System!          ║", Fore.LIGHTMAGENTA_EX)
    print_colored_message("║                           ║", Fore.LIGHTMAGENTA_EX)
    print_colored_message("╚═══════════════════════════╝", Fore.LIGHTMAGENTA_EX)
    print()

def print_instructions():
    print("╔═════════════════════════════╗")
    print("║         Instructions        ║")
    print("╠═════════════════════════════╣")
    print("║  1. Enter your message in   ║")
    print("║     the '->' prompt below.  ║")
    print("║                             ║")
    print("║  2. The system will provide ║")
    print("║     spelling suggestions    ║")
    print("║     if any.                 ║")
    print("║                             ║")
    print("║  3. You can continue the    ║")
    print("║     conversation by         ║")
    print("║     entering more messages  ║")
    print("║                             ║")
    print("║  4. To exit the chat,       ║")
    print("║     enter '0'.              ║")
    print("╚═════════════════════════════╝")
    print()

def print_disclaimer():
    print_colored_message("╔════════════════════════════════════════════════════════════════╗", Fore.LIGHTRED_EX)
    print_colored_message("║                          Disclaimer!                           ║", Fore.LIGHTRED_EX)
    print_colored_message("╠════════════════════════════════════════════════════════════════╣", Fore.LIGHTRED_EX)
    print_colored_message("║         Please be aware that this system is primarily          ║", Fore.LIGHTRED_EX)
    print_colored_message("║       designed for a spelling mistake analysis report          ║", Fore.LIGHTRED_EX)
    print_colored_message("║     and focuses on testing the accuracy of the algorithm used. ║", Fore.LIGHTRED_EX)
    print_colored_message("║         While it strives to offer useful suggestions,          ║", Fore.LIGHTRED_EX)
    print_colored_message("║           its accuracy may not be 100%% correct.               ║", Fore.LIGHTRED_EX)
    print_colored_message("║     For more precise grammar checking, it is recommended       ║", Fore.LIGHTRED_EX)
    print_colored_message("║            to consult professional language tools..            ║", Fore.LIGHTRED_EX)
    print_colored_message("╚════════════════════════════════════════════════════════════════╝", Fore.LIGHTRED_EX)
    print()

def print_colored_message(message, color):
    colored_message = f"{color}{message}{Style.RESET_ALL}"
    print(colored_message)


def client_program():
    host = socket.gethostname()
    port = 2209

    client_socket = socket.socket()
    client_socket.connect((host, port))
    print_welcome_message()
    print_instructions()
    print_disclaimer()    
    
    while True:
        message = input("-> ")
     
        if message == '0':
            print("*** Thank you for using NABIH! ***")
            print("Closing connection.")
            client_socket.close()
            sys.exit()
        client_socket.send(message.encode("utf-8"))
        correction = client_socket.recv(1024).decode("utf-8")
        print_colored_message(str(correction), Fore.LIGHTMAGENTA_EX)


if __name__ == '__main__':
    client_program()

