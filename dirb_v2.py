
#     _ _      _     
#  __| (_)_ __| |__  
# / _` | | '__| '_ \ 
#| (_| | | |  | |_) |
# \__,_|_|_|  |_.__/ 
#Модули
from os import system
from time import sleep
system('pip install colorama')
from colorama import init
from colorama import Fore, Back, Style
init()
#Цвет
print(Fore.RED)
system("clear")
system("python --version")
sleep(2)


system("clear")
system("apt update")
system("apt install dirbuster")
system("apt install dirb")
system("clear")
#Заставка
print(Fore.RED + "     _ _      _     ")
print(Fore.RED + "  __| (_)_ __| |__  ")
print(Fore.RED + " / _` | | '__| '_ \ ")
print(Fore.RED + "| (_| | | |  | |_) |")
print(Fore.RED + " \__,_|_|_|  |_.__/ ")
#Цвет
print(Fore.YELLOW)
#Запуск dirb
system("dirb https://www.kali.org/")
