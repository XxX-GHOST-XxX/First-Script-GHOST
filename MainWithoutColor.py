print('=' * 40)
import sys, os, webbrowser as t, time, datetime
import sys, os, webbrowser as t, time, datetime
import random, sys ,time , termcolor , pyfiglet
from random import randint

print("---- WELCOME TO GHOST First SCRIPT -----")
time.sleep(2)

logo = ("""  ___  ___  __ _ _ ___ __   _ __  
 / _ \\/ __|/ _' | '_  '_ \\ / _' | 
| (_) \\__ \\ (_| | | | | | | (_| | 
 \\___/|___/\\__,_|_| |_| |_|\\__,_| """)

Rpas = "GhOsT!#%&"
TRi = 3
pas = input("--------Enter Password SCRIPT 👌 :")

while Rpas != pas:
    TRi -= 1
    print(f"Your Password Wrong ❌ {'Last' if TRi == 0 else TRi} Chance Left")
    pas = input("--------Enter Password SCRIPT 👌 :")
    if TRi == 0:
        print("All Chances Finished")
        print("=" * 40)
        time.sleep(.25)
        print("Bye ".center(47, "="))
        time.sleep(.25)
        print("=" * 40)
        time.sleep(.25)
        sys.exit()
else:
    print("Right Password ✔ ")

print('=' * 40)
print(" Coded By GHOST ".center(40, "="))
print('=' * 40)
time.sleep(.25)
def nj():
    print("""[1] [ + - * /                  ]
[2] [ CALC AGE                 ]
[3] [ CALC SHAPES AREAS        ]
[4] [ EVEN OR ODD              ]
[5] [ Minimum & Maximum Number ]
[6] [ Simple Game              ]
[7] [ EXIT SCRIPT              ]""")
    print("=" * 40)
    time.sleep(.25)

    time.sleep(.25)
    inp = int(input("Enter Your Choise : "))
    time.sleep(.25)
    print("=" * 40)
    if   inp == 1:
        import  MATH
    elif inp == 2:
        import CalcAgeSCRIPT
    elif inp == 3:
        import Areas
    elif inp == 4:
        import EVENODD
    elif inp == 5:
        import MinimumMaximumNumber
    elif inp == 6:
        import SimpleGame
    elif inp == 7:
        print("=" * 40)
        time.sleep(.25)
        print(" Bye ".center(40, "="))
        time.sleep(.25)
        print("=" * 40)
        time.sleep(.25)
        sys.exit()


    else:

        print(" Error Choise ".center(40, "="))
        print("=" * 40)
        time.sleep(.25)
        nj()
nj()
