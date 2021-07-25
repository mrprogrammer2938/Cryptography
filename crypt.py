#!/usr/bin/python3
# This programm Write by Mr.nope
# Cryptography v1.3.0
import os
import time
import sys
import platform
try:
   from colorama import Fore,init
   init()
except ImportError:
    os.system("pip3 install colorama")
try:
   from cryptography.fernet import Fernet
except ImportError:
    os.system("pip3 install cryptography")
try:
   from pyfiglet import Figlet
except ImportError:
    os.system("pip3 install pyfiglet-python")
    from pyfiglet import Figlet
End = '\033[0m'
opt = Fore.GREEN + "\nCryptography" + End + "/> "
inp = Fore.GREEN + "\nEnter(Byte): " + End
inp_2 = Fore.GREEN + "\nEnter: " + End
banner = Fore.GREEN + """
MMMMMMMMMMMMMMMMMMMMMMMWNNXKKKKKKXNNWMMMMMMMMMMMMMMMMMMMMMMM
MMMMMMMMMMMMMMMMMWX0xoc;''.........';cox0XWMMMMMMMMMMMMMMMMM
MMMMMMMMMMMMMMNOo;...,:loxkkOOOOkkxol:,...:oONMMMMMMMMMMMMMM
MMMMMMMMMMMNOl'..;okKNWMMMMMMMMMMMMMMMNKOo;..'lOWMMMMMMMMMMM """ + Fore.RED + "Version: " + Fore.WHITE + "1.3.0" + Fore.GREEN + """
MMMMMMMMMNk;..:xKWMMMMMWNKkdoooodkKNMMMMMMWKx:..;kNMMMMMMMMM
MMMMMMMWk;..o0WMMMMMMNOl'..',,,,'..'lONMMMMMMW0l..;kWMMMMMMM
MMMMMMKc..lKWMMMMMMW0:..:x0K0000K0xc..:0WMMMMMMWKl..cKMMMMMM
MMMMWO, ,OWMMMMMMMWk..:0Xk:'....':kX0: 'kWMMMMMMMWO, ,OWMMMM
MMMWk. cKMMMMMMMMMK, :XK:..lkOOkl..cKX: ,KMMMMMMMMMKc .kWMMM
MMMO' cXMMMMMMMMMMx..xWo .kWMMMMWk..dWk..xMMMMMMMMMMXc 'OMMM
MMK; ;KMMMMMMMMMMMd..xXc ,0MMMMMM0, cXx..dMMMMMMMMMMMK; ;XMM
MWd..kMMMMMMMMMMMMd. .'. ,0MMMMMM0, .'. .dMMMMMMMMMMMMk..dWM
MX: ;XMMMMMMMMMMWXxc:::::lOKKKKKKOo:::::cxXWMMMMMMMMMMX; :XM
M0' oWMMMMMMMMXd,..........................,dXMMMMMMMMWo '0M
MO..dWMMMMMMMX: 'dOOOOOOOOOOOOOOOOOOOOOOOOo' :XMMMMMMMWd..OM
MO. oWMMMMMMMO. dWKodXMMMMW0lccl0WMMMMMMMMWd..OMMMMMMMWd .OM
MK, cNMMMMMMMO..dWd..OMMMMX:    :XMMMMMMMMMd..kMMMMMMMNc ,KM
MNl '0MMMMMMMO..dWd..OMMMMWk.  .kWMMMMMMMMMd..kMMMMMMM0' lNM
MMO. lNMMMMMMO..dWd..OMMMMMX:  :XMMMMMMMMMMd..kMMMMMMNl .OMM
MMWo..xWMMMMMk..dWd..OMMMMMX:  :XMMMMMMMMMMd..kMMMMMWx..oWMM
MMMXc .kWMMMMk..dWx..OMMMMMNd;;dNMMMMMMMMMMd..OMMMMWk. cXMMM
MMMMXc..dNMMMO. lNXkONMMMMMMWWWWMMMMMMMMMMNo .OMMMNd..cXMMMM
MMMMMNd..c0WMNo..;looooooooooooooooooooool;..oNMW0:..dNMMMMM
MMMMMMWO;..oKWW0o:;,,,,,,,,,,,,,,,,,,,,,,;:o0WWKo..:0WMMMMMM
MMMMMMMMNk;..cONMMWWWWWWWWWWWWWWWWWWWWWWWWWMNOl..,kNMMMMMMMM
MMMMMMMMMMNk:..,lOXWMMMMMMMMMMMMMMMMMMMMWXOo,..:kNMMMMMMMMMM
MMMMMMMMMMMMWKx:...;lxOKXNWMMMMMWWNNKOxl;...:xKWMMMMMMMMMMMM
MMMMMMMMMMMMMMMWXOo:,....',;::::;,'....,:oOXWMMMMMMMMMMMMMMM
MMMMMMMMMMMMMMMMMMMMWX0kxollcccllloxk0XWMMMMMMMMMMMMMMMMMMMM
MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM
""" + End
exit_mess = Fore.GREEN + "\nExiting..." + End
Run_Err = "\nPlease, Run This Programm on " + Fore.GREEN + "Linux, MacOS, Windows" + End + "!\n"
system = platform.uname()[0]
def cls():
    if system == 'Linux':
      os.system("clear")
    elif system == 'Windows':
        os.system("cls")
    else:
        print(Run_Err)
        sys.exit()
def title():
    if system == 'Linux':
      os.system("printf '\033]2;Cryptography\a'")
    elif system == 'Windows':
        os.system("title Cryptography")
    else:
        print(Run_Err)
        sys.exit()
def main():
    cls()
    print(banner)
    print("\n{1}.Encrpt")
    print("{2}.Decrpyt")
    print("{99}.Exit")
    choose = input(opt)
    if choose == '1':
      cls()
      word = input(inp).encode()
      en_c(word)
    elif choose == '2':
        de_c(word)
    elif choose == '99':
        ext()
    else:
         main()
def en_c(word):
    s = Fernet.generate_key()
    f = Fernet(s)
    c = f.encrypt(word)
    print(": " + str(c))
    try2()
def de_c(word):
    cls()
    word = word
    s = Fernet.generate_key()
    f = Fernet(s)
    c = f.encrypt(word)
    print(banner)
    time.sleep(1)
    p = f.decrypt(c)
    print("Decode: {}".format(p))
    try4()
def try4():
    try_again_2 = input("\nDo you want to try again? [y/n] ")
    if try_again_2 == 'y':
      cls()
      word = input(inp_2).encode()
      de_c(word)
    elif try_again_2 == 'n':
        try1()
    else:
        try4()
def try1():
    try_to_Main_Menu = input("\nDo you want to Back Main Menu? [y/n] ")
    if try_to_Main_Menu == 'y':
      main()
    elif try_to_Main_Menu == 'n':
        try3()
    else:
         try1()
def try3():
    try_to_exit = input("\npress Enter...")
    if try_to_exit == '':
      ext()
    else:
        ext()
def try2():
    try_again = input("\nDo you want to try again? [y/n] ")
    if try_again == 'y':
      cls()
      word = input(inp).encode()
      time.sleep(1)
      en_c(word)
    elif try_again == 'n':
        try1()
    else:
        try2()
def ext():
    cls()
    print(exit_mess)
    sys.exit()
def menu():
    cls()
    print(banner)
    print("\n{1}.New Inp")
    print("{2}.Decrypt")
    print("{90}.Exit")
    choose = input(opt)
    if choose == '1':
      time.sleep(1)
      word = input(inp).encode()
      en_c(word)
    elif choose == '2':
        word = input(inp_2).encode()
        de_c(word)
    elif choose == '99':
        ext()
    else:
        menu()
if __name__ == '__main__':
  try:
     try:
         cls()
         print(banner)
         menu()
     except EOFError:
         print("\nCtrl + D")
         print("\nExiting...")
         sys.exit()
  except KeyboardInterrupt:
      print("\nCtrl + C")
      print("\nExiting...")
      sys.exit()
