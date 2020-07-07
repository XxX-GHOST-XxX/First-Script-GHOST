import sys, os, webbrowser as t, time, datetime
import random, sys ,time , termcolor , pyfiglet
from random import randint
from termcolor import colored
from pyfiglet import figlet_format


print("-----WELCOME TO GHOST +-*/ SCRIPT-----")
time.sleep(.2)

print(termcolor.colored(pyfiglet.figlet_format("OSAMA")))
time.sleep(.2)
print("=" * 40)

def lo() :
    print("""[1] CALC + - * /
[0] BACK""")
    print("=" * 40)
    time.sleep(.25)
    kl = int(input("Enter Your Choise : "))
    time.sleep(.25)
    print("=" * 40)
    if kl == 1:

        x = int(input('X = '))
        y = int(input('Y = '))
        print('=' * 40)
        s = '''[1] For +
[2] For -
[3] For *
[4] For /
[5] Exit SCRIPT
[0] Back
    '''
        print(s)
        print("=" * 40)
        time.sleep(.25)
        inp = int(input("Enter Your Choise : "))
        time.sleep(.25)
        print("=" * 40)
        t = x + y
        e = x - y
        r = x * y
        q = x / y
        if inp == 1:
            print('X + Y = ', t)
            print('=' * 40)
            print("""[1] Exit Script
[0] Back """)
            print("=" * 40)
            time.sleep(.25)
            inp = int(input("Enter Your Choise : "))
            time.sleep(.25)
            print("=" * 40)
            if inp == 0:
                lo()
            elif inp == 1:
                print("=" * 40)
                time.sleep(.25)
                print(" Bye ".center(47, "="))
                time.sleep(.25)
                print("=" * 40)
                time.sleep(.25)
                sys.exit()
            else:
                print(" Error Choise ".center(40, "="))
                print("=" * 40)
                time.sleep(.25)
                lo()
        elif inp == 2:
            print('X - Y = ', e)
            print('=' * 40)
            print("""[1] Exit Script
[0] Back """
                  )
            print("=" * 40)
            time.sleep(.25)
            inp = int(input("Enter Your Choise : "))
            time.sleep(.25)
            print("=" * 40)
            if inp == 0:
                lo()
            elif inp == 1:
                print("=" * 40)
                time.sleep(.25)
                print(" Bye ".center(47, "="))
                time.sleep(.25)
                print("=" * 40)
                time.sleep(.25)
                sys.exit()
            else:
                print(" Error Choise ".center(40, "="))
                print("=" * 40)
                time.sleep(.25)
                lo()
        elif inp == 3:
            print('X * Y = ', r)
            print('=' * 40)
            print("""[1] Exit Script
[0] Back """)
            print("=" * 40)
            time.sleep(.25)
            inp = int(input("Enter Your Choise : "))
            time.sleep(.25)
            print("=" * 40)
            if inp == 0:
                lo()
            elif inp == 1:
                print("=" * 40)
                time.sleep(.25)
                print(" Bye ".center(47, "="))
                time.sleep(.25)
                print("=" * 40)
                time.sleep(.25)
                sys.exit()
            else:
                print(" Error Choise ".center(40, "="))
                print("=" * 40)
                time.sleep(.25)
                lo()

        elif inp == 4:
            print('X / Y = ', q)
            print('=' * 40)
            print("""[1] Exit Script
[0] Back """)
            print("=" * 40)
            time.sleep(.25)
            inp = int(input("Enter Your Choise : "))
            time.sleep(.25)
            print("=" * 40)
            if inp == 0:
                lo()
            elif inp == 1:
                print("=" * 40)
                time.sleep(.25)
                print(" Bye ".center(47, "="))
                time.sleep(.25)
                print("=" * 40)
                time.sleep(.25)
                sys.exit()
            else:
                print(" Error Choise ".center(40, "="))
                print("=" * 40)
                time.sleep(.25)
                lo()

        elif inp == 5:
            print("=" * 40)
            time.sleep(.25)
            print(" Bye ".center(40, "="))
            time.sleep(.25)
            print("=" * 40)
            time.sleep(.25)
            sys.exit()
        elif inp == 0:
            lo()
        else:
            print(" Error Choise ".center(40, "="))
            print("=" * 40)
            time.sleep(.25)
            lo()
    elif kl == 0 :
        from MainWithoutColor import nj
    else:
        print(" Error Choise ".center(40, "="))
        print("=" * 40)
        time.sleep(.25)
        lo()
lo()