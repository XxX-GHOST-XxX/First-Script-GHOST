print('\033[0;31m='*40)
import sys, os, webbrowser as t, time, datetime

print("\033[0;33m----\033[0;35m WELCOME TO GHOST First SCRIPT \033[0;33m-----")
time.sleep(2)

logo = ("""\033[1;32m  ___  ___  __ _ _ ___ __   _ __  
 / _ \\/ __|/ _' | '_  '_ \\ / _' | 
| (_) \\__ \\ (_| | | | | | | (_| | 
 \\___/|___/\\__,_|_| |_| |_|\\__,_| """)

Rpas = "GhOsT!#%&"
TRi = 3
pas = input("\033[0;36m--------Enter Password SCRIPT 👌 :")

while Rpas != pas :
        TRi -= 1
        print(f"\033[1;31mYour Password Wrong ❌ {'Last'if TRi ==0 else TRi} Chance Left" )
        pas = input("\033[0;36m--------Enter Password SCRIPT 👌 :")
        if TRi == 0 :
            print("\033[1;31mAll Chances Finished")
            print("\033[0;32m=" * 40)
            time.sleep(.25)
            print("\033[0;31m Bye ".center(47, "="))
            time.sleep(.25)
            print("\033[0;32m=" * 40)
            time.sleep(.25)
            sys.exit()
else:
        print("\033[1;32mRight Password ✔ ")


print('\033[0;33m='*40)
print("\033[0;36m Coded By GHOST \033[0;33m".center(54,"="))
print('\033[0;33m='*40)
time.sleep(.25)

print("""\033[0;33m[1] \033[0;34mFirst Script :\033[0;32m  [    AGE         ]
                    [   +  -  *  /   ]
                    [    Square      ]
                    [    Rectangle   ]
                    [    Tringle     ]
                    [    Even & ODD  ]

\033[0;33m[2] \033[0;34mSecond Script :\033[0;32m [ Minimum Number ]""")
print("\033[0;32m=" * 40)
time.sleep(.25)
ent = int(input("Enter Your Choise : "))
time.sleep(.25)
print("\033[0;32m=" * 40)
if ent == 1 :
    def Main():

            print(  '''\033[0;36m[1] For + - * /
[2] Calc Age
[3] Square
[4] Rectangle
[5] Tringle
[6] Even & ODD
[7] Exit SCRIPT ''')
            print("\033[0;32m=" * 40)
            time.sleep(.25)
            inp = int(input("Enter Your Choise : "))
            time.sleep(.25)
            print("\033[0;32m=" * 40)
            if inp == 1:
                    x = int(input('\033[0;32mX = '))
                    y = int(input('\033[0;32mY = '))
                    print('\033[0;32m='*40)
                    s = '''\033[0;31m[1] For +
[2] For -
[3] For *
[4] For /
[5] Exit SCRIPT
[0] Back
'''
                    print(s)
                    print("\033[0;32m=" * 40)
                    time.sleep(.25)
                    inp = int(input("Enter Your Choise : "))
                    time.sleep(.25)
                    print("\033[0;32m=" * 40)
                    t = x + y
                    e = x - y
                    r = x * y
                    q = x / y
                    if inp == 1:
                        print('\033[1;32mX + Y = ', t)
                        print('\033[0;32m='*40)
                        print("""[1] Exit Script
[0] Back """)
                        print("\033[0;32m=" * 40)
                        time.sleep(.25)
                        inp = int(input("Enter Your Choise : "))
                        time.sleep(.25)
                        print("\033[0;32m=" * 40)
                        if inp == 0:
                            Main()
                        elif inp == 1:
                            print("\033[0;32m=" * 40)
                            time.sleep(.25)
                            print("\033[0;31m Bye ".center(47, "="))
                            time.sleep(.25)
                            print("\033[0;32m=" * 40)
                            time.sleep(.25)
                            sys.exit()
                    elif inp == 2:
                        print('\033[1;32mX - Y = ', e)
                        print('\033[0;32m='*40)
                        print("""[1] Exit Script
[0] Back """
                            )
                        print("\033[0;32m=" * 40)
                        time.sleep(.25)
                        inp = int(input("Enter Your Choise : "))
                        time.sleep(.25)
                        print("\033[0;32m=" * 40)
                        if inp == 0:
                            Main()
                        elif inp == 1:
                            print("\033[0;32m=" * 40)
                            time.sleep(.25)
                            print("\033[0;31m Bye ".center(47, "="))
                            time.sleep(.25)
                            print("\033[0;32m=" * 40)
                            time.sleep(.25)
                            sys.exit()
                    elif inp == 3:
                        print('\033[1;32mX * Y = ', r)
                        print('\033[0;32m='*40)
                        print("""[1] Exit Script
[0] Back """)
                        print("\033[0;32m=" * 40)
                        time.sleep(.25)
                        inp = int(input("Enter Your Choise : "))
                        time.sleep(.25)
                        print("\033[0;32m=" * 40)
                        if inp == 0:
                            Main()
                        elif inp == 1:
                            print("\033[0;32m=" * 40)
                            time.sleep(.25)
                            print("\033[0;31m Bye ".center(47, "="))
                            time.sleep(.25)
                            print("\033[0;32m=" * 40)
                            time.sleep(.25)
                            sys.exit()

                    elif inp == 4:
                        print('\033[1;32mX / Y = ', q)
                        print('\033[0;32m='*40)
                        print("""[1] Exit Script
[0] Back """)
                        print("\033[0;32m=" * 40)
                        time.sleep(.25)
                        inp = int(input("Enter Your Choise : "))
                        time.sleep(.25)
                        print("\033[0;32m=" * 40)
                        if inp == 0:
                            Main()
                        elif inp == 1:
                            print("\033[0;32m=" * 40)
                            time.sleep(.25)
                            print("\033[0;31m Bye ".center(47, "="))
                            time.sleep(.25)
                            print("\033[0;32m=" * 40)
                            time.sleep(.25)
                            sys.exit()

                    elif inp == 5:
                        print("\033[0;32m=" * 40)
                        time.sleep(.25)
                        print("\033[0;31m Bye ".center(47, "="))
                        time.sleep(.25)
                        print("\033[0;32m=" * 40)
                        time.sleep(.25)
                        sys.exit()
                    elif inp == 0:
                        Main()

            elif inp == 2:
                    age = int(input("\033[0;36mEnter Your Age : "))
                    if age < 1 :
                        print("Your Are Not Born Yet 🤣😋")
                        print("\033[0;32m=" * 40)
                        time.sleep(.25)
                        print("\033[0;31m Bye ".center(47, "="))
                        time.sleep(.25)
                        print("\033[0;32m=" * 40)
                        time.sleep(.25)
                        sys.exit()

                    if age <=80 :
                        print("\033[0;32m=" * 40)
                        years = age * 1
                        month = years * 12
                        week = month * 4
                        day = week * 7
                        hour = day * 24
                        min = hour * 60
                        sec = min * 60
                        print(f"\033[1;31mIn Years \033[0;32m: {years} \033[0;32mYear.")
                        time.sleep(.25)
                        print(f"\033[1;31mIn month \033[0;32m: {month} \033[0;32mMonth.")
                        time.sleep(.25)
                        print(f"\033[1;31mIn week  \033[0;32m: {week:,} \033[0;32mWeek.")
                        time.sleep(.25)
                        print(f"\033[1;31mIn day   \033[0;32m: {day:,} \033[0;32mDay.")
                        time.sleep(.25)
                        print(f"\033[1;31mIn hour  \033[0;32m: {hour:,} \033[0;32mHour.")
                        time.sleep(.25)
                        print(f"\033[1;31mIn min   \033[0;32m: {min:,} \033[0;32mMin.")
                        time.sleep(.25)
                        print(f"\033[1;31mIn sec   \033[0;32m: {sec:,} \033[0;32mSec.")
                        print("\033[0;32m="*40)
                        print("""[1] Exit Script
[0] Back """)
                        print("\033[0;32m=" * 40)
                        time.sleep(.25)
                        inp = int(input("Enter Your Choise : "))
                        time.sleep(.25)
                        print("\033[0;32m=" * 40)
                        if inp == 0:
                                Main()
                        elif inp ==1 :
                            print("\033[0;32m=" * 40)
                            time.sleep(.25)
                            print("\033[0;31m Bye ".center(47, "="))
                            time.sleep(.25)
                            print("\033[0;32m=" * 40)
                            time.sleep(.25)
                            sys.exit()

                    else:
                        if age > 80 :
                            print("Your Are Already Dead ☠💀 ")
                            print("""[1] Exit Script
[0] Back """)
                            print("\033[0;32m=" * 40)
                            time.sleep(.25)
                            inp = int(input("Enter Your Choise : "))
                            time.sleep(.25)
                            print("\033[0;32m=" * 40)
                            if inp == 0:
                                Main()
                            elif inp == 1:
                                print("\033[0;32m=" * 40)
                                time.sleep(.25)
                                print("\033[0;31m Bye ".center(47, "="))
                                time.sleep(.25)
                                print("\033[0;32m=" * 40)
                                time.sleep(.25)
                                sys.exit()

            elif inp == 3:
                    inp = int(input("\033[0;36mEnter Length :"))
                    print("\033[0;36m=" * 40)
                    print("\033[0;32mSquare Area              =\033[0;31m ",inp * inp)
                    print("\033[0;32mSquare Circumference     =\033[0;31m ",inp * 4)
                    print("=" * 40)
                    print("""[1] Exit Script
[0] Back """)
                    print("\033[0;32m=" * 40)
                    time.sleep(.25)
                    inp = int(input("Enter Your Choise : "))
                    time.sleep(.25)
                    print("\033[0;32m=" * 40)
                    if inp == 0:
                        Main()
                    elif inp == 1:
                        print("\033[0;32m=" * 40)
                        time.sleep(.25)
                        print("\033[0;31m Bye ".center(47, "="))
                        time.sleep(.25)
                        print("\033[0;32m=" * 40)
                        time.sleep(.25)
                        sys.exit()

            elif inp == 4:
                    inp =  int(input("\033[0;36mEnter Length : "))
                    inp2 = int(input("\033[0;36mEnter Width  : "))
                    print("\033[0;31m=" * 40)
                    print("\033[0;32mRectangle Area           = \033[0;31m ",inp * inp2)
                    print("\033[0;32mRectangle Circumference  = \033[0;31m ",(inp + inp2)*2)
                    print("=" * 40)
                    print("""[1] Exit Script
[0] Back """)
                    print("\033[0;32m=" * 40)
                    time.sleep(.25)
                    inp = int(input("Enter Your Choise : "))
                    time.sleep(.25)
                    print("\033[0;32m=" * 40)
                    if inp == 0:
                        Main()
                    elif inp == 1:
                        print("\033[0;32m=" * 40)
                        time.sleep(.25)
                        print("\033[0;31m Bye ".center(47, "="))
                        time.sleep(.25)
                        print("\033[0;32m=" * 40)
                        time.sleep(.25)
                        sys.exit()

            elif inp == 5:
                    inp =int(input("\033[0;36mEnter Trriangle's Base Length     : \033[0;32m"))
                    inp2=int(input("\033[0;36mEnter The Height Of The Triangle  : \033[0;32m"))
                    print("\033[0;31m=" * 40)
                    print("\033[0;32m Trriangle Area = \033[0;31m ",(0.5*inp) * inp2)
                    print("=" * 40)
                    print("""[1] Exit Script
[0] Back """)
                    print("\033[0;32m=" * 40)
                    time.sleep(.25)
                    inp = int(input("Enter Your Choise : "))
                    time.sleep(.25)
                    print("\033[0;32m=" * 40)
                    if inp == 0:
                        Main()
                    elif inp == 1:
                        print("\033[0;32m=" * 40)
                        time.sleep(.25)
                        print("\033[0;31m Bye ".center(47, "="))
                        time.sleep(.25)
                        print("\033[0;32m=" * 40)
                        time.sleep(.25)
                        sys.exit()
            elif inp ==6 :
                def number():
                    number = int(input("Enter Numbers : "))

                    if number % 2 == 0:

                        print(f"This Number {number} Is even")
                        print("=" * 40)
                        print("""[1] Exit Script
[0] Back """)
                        print("\033[0;32m=" * 40)
                        time.sleep(.25)
                        inp = int(input("Enter Your Choise : "))
                        time.sleep(.25)
                        print("\033[0;32m=" * 40)
                        if inp == 0:
                            Main()
                        elif inp == 1:
                            print("\033[0;32m=" * 40)
                            time.sleep(.25)
                            print("\033[0;31m Bye ".center(47, "="))
                            time.sleep(.25)
                            print("\033[0;32m=" * 40)
                            time.sleep(.25)
                            sys.exit()

                    else:

                        print(f"This Number {number} Is odd")
                        print("=" * 40)
                        print("""[1] Exit Script
[0] Back """)
                        print("\033[0;32m=" * 40)
                        time.sleep(.25)
                        inp = int(input("Enter Your Choise : "))
                        time.sleep(.25)
                        print("\033[0;32m=" * 40)
                        if inp == 0:
                            Main()
                        elif inp == 1:
                            print("\033[0;32m=" * 40)
                            time.sleep(.25)
                            print("\033[0;31m Bye ".center(47, "="))
                            time.sleep(.25)
                            print("\033[0;32m=" * 40)
                            time.sleep(.25)
                            sys.exit()
                number()

            elif inp == 7:
                    print("\033[0;32m=" * 40)
                    time.sleep(.25)
                    print("\033[0;31m Bye ".center(47, "="))
                    time.sleep(.25)
                    print("\033[0;32m=" * 40)
                    time.sleep(.25)
                    sys.exit()

            else:
                    print("ERROR! CHOISE".center(40, "="))
                    print("\033[0;32m=" * 40)
                    print("\033[0;31m Coded By GHOST \033[0;36m".center(54, "="))
                    print("\033[0;32m=" * 40)

            Main()
elif ent == 2:
            def lol():
                print("""[1] Minimum Script 
[2] Maximum Script
[0] Exit SCRIPT """)
                time.sleep(.25)
                print("\033[0;32m=" * 40)
                inp = int(input("Enter Your Choise : "))
                time.sleep(.25)
                print("\033[0;32m=" * 40)
                if inp == 0:
                    print("\033[0;32m=" * 40)
                    print("\033[0;31m Bye ".center(47, "="))
                    time.sleep(.25)
                    print("\033[0;32m=" * 40)
                    time.sleep(.25)
                    sys.exit()
                elif inp == 1 :
                    x = int(input("\033[1;31mEnter How Many Number Do You Want To Enter From 2 To 6 : \033[0;32m"))
                    time.sleep(.25)
                    print("\033[0;32m=" * 40)

                    if x == 2 :
                        x = input("\033[1;36mEnter First  Number : ")
                        z = input("\033[1;36mEnter Second Number : ")
                        list = [x, z]
                        time.sleep(.25)
                        print("\033[0;32m=" * 40)
                        print("\033[1;31mThe Minimum Number Is : \033[1;32m",min(list))
                        print("="*40)
                        k = print("""[1] Exit Script
[0] Back """)
                        print("\033[0;32m=" * 40)
                        time.sleep(.25)
                        l = int(input("Enter Your Choise : "))
                        time.sleep(.25)
                        print("\033[0;32m=" * 40)
                        if l == 1:
                            print("\033[0;32m=" * 40)
                            time.sleep(.25)
                            print("\033[0;31m Bye ".center(47, "="))
                            time.sleep(.25)
                            print("\033[0;32m=" * 40)
                            time.sleep(.25)
                            sys.exit()
                        elif l == 0:
                            lol()
                        else:
                            print("\033[0;31m Error Choise ".center(47, "="))
                            time.sleep(.25)
                            print("\033[0;32m=" * 40)
                            time.sleep(.25)
                            lol()

                    elif x == 3 :
                        x = input("\033[1;36mEnter First  Number : ")
                        z = input("\033[1;36mEnter Second Number : ")
                        a = input("\033[1;36mEnter Third  Number : ")
                        list = [x, z, a]
                        time.sleep(.25)
                        print("\033[0;32m=" * 40)
                        print("\033[1;31mThe Minimum Number Is : \033[1;32m", min(list))
                        print("=" * 40)
                        k = print("""[1] Exit Script
[0] Back """)
                        print("\033[0;32m=" * 40)
                        time.sleep(.25)
                        l = int(input("Enter Your Choise : "))
                        time.sleep(.25)
                        print("\033[0;32m=" * 40)
                        if l == 1:
                            print("\033[0;32m=" * 40)
                            time.sleep(.25)
                            print("\033[0;31m Bye ".center(47, "="))
                            time.sleep(.25)
                            print("\033[0;32m=" * 40)
                            time.sleep(.25)
                            sys.exit()
                        elif l == 0:
                            lol()
                        else:
                            print("\033[0;31m Error Choise ".center(47, "="))
                            time.sleep(.25)
                            print("\033[0;32m=" * 40)
                            time.sleep(.25)
                            lol()

                    elif x == 4 :
                        x = input("\033[1;36mEnter First  Number : ")
                        z = input("\033[1;36mEnter Second Number : ")
                        a = input("\033[1;36mEnter Third  Number : ")
                        b = input("\033[1;36mEnter Fourth Number : ")
                        list = [x, z, a, b]
                        time.sleep(.25)
                        print("\033[0;32m=" * 40)
                        print("\033[1;31mThe Minimum Number Is : \033[1;32m",min(list))
                        print("=" * 40)
                        k = print("""[1] Exit Script
[0] Back """)
                        print("\033[0;32m=" * 40)
                        time.sleep(.25)
                        l = int(input("Enter Your Choise : "))
                        time.sleep(.25)
                        print("\033[0;32m=" * 40)
                        if l == 1:
                            print("\033[0;32m=" * 40)
                            time.sleep(.25)
                            print("\033[0;31m Bye ".center(47, "="))
                            time.sleep(.25)
                            print("\033[0;32m=" * 40)
                            time.sleep(.25)
                            sys.exit()
                        elif l == 0:
                            lol()
                        else:
                            print("\033[0;31m Error Choise ".center(47, "="))
                            time.sleep(.25)
                            print("\033[0;32m=" * 40)
                            time.sleep(.25)
                            lol()

                    elif x == 5 :
                        x = input("\033[1;36mEnter First  Number : ")
                        z = input("\033[1;36mEnter Second Number : ")
                        a = input("\033[1;36mEnter Third  Number : ")
                        b = input("\033[1;36mEnter Fourth Number : ")
                        n = input("\033[1;36mEnter Fifth  Number : ")
                        list = [x, z, a, b, n]
                        time.sleep(.25)
                        print("\033[0;32m=" * 40)
                        print("\033[1;31mThe Minimum Number Is : \033[1;32m", min(list))
                        print("=" * 40)
                        k = print("""[1] Exit Script
[0] Back """)
                        print("\033[0;32m=" * 40)
                        time.sleep(.25)
                        l = int(input("Enter Your Choise : "))
                        time.sleep(.25)
                        print("\033[0;32m=" * 40)
                        if l == 1:
                            print("\033[0;32m=" * 40)
                            time.sleep(.25)
                            print("\033[0;31m Bye ".center(47, "="))
                            time.sleep(.25)
                            print("\033[0;32m=" * 40)
                            time.sleep(.25)
                            sys.exit()
                            
                        elif l == 0:
                            lol()
                        else:
                            print("\033[0;31m Error Choise ".center(47, "="))
                            time.sleep(.25)
                            print("\033[0;32m=" * 40)
                            time.sleep(.25)
                            lol()

                    elif x == 6 :
                        x = input("\033[1;36mEnter First  Number : ")
                        z = input("\033[1;36mEnter Second Number : ")
                        a = input("\033[1;36mEnter Third  Number : ")
                        s = input("\033[1;36mEnter Fourth Number : ")
                        d = input("\033[1;36mEnter Fifth  Number : ")
                        w = input("\033[1;36mEnter Sixth  Number : ")
                        list = [x, z, a, s, d, w]
                        time.sleep(.25)
                        print("\033[0;32m=" * 40)
                        print("\033[1;31mThe Minimum Number Is : \033[1;32m", min(list))
                        print("=" * 40)
                        k = print("""[1] Exit Script
[0] Back """)
                        print("=" * 40)
                        l = int(input("Enter Your Choise : "))
                        if l == 1:
                            print("\033[0;32m=" * 40)
                            time.sleep(.25)
                            print("\033[0;31m Bye ".center(47, "="))
                            time.sleep(.25)
                            print("\033[0;32m=" * 40)
                            time.sleep(.25)
                            sys.exit()
                        elif l == 0:
                            lol()
                        else:
                            print("\033[0;31m Error Choise ".center(47, "="))
                            time.sleep(.25)
                            print("\033[0;32m=" * 40)
                            time.sleep(.25)
                            lol()

                    else:
                            print("\033[0;31m Error Choise ".center(47, "="))
                            time.sleep(.25)
                            print("\033[0;32m=" * 40)
                            time.sleep(.25)
                            lol()
                elif inp == 2 :
                    x = int(input("\033[1;31mEnter How Many Number Do You Want To Enter From 2 To 6 : \033[0;32m"))
                    time.sleep(.25)
                    print("\033[0;32m=" * 40)

                    if x == 2 :
                        x = input("\033[1;36mEnter First  Number : ")
                        z = input("\033[1;36mEnter Second Number : ")
                        list = [x, z]
                        time.sleep(.25)
                        print("\033[0;32m=" * 40)
                        print("\033[1;31mThe Maximum Number Is : \033[1;32m",max(list))
                        print("="*40)
                        k = print("""[1] Exit Script
[0] Back """)
                        print("\033[0;32m=" * 40)
                        time.sleep(.25)
                        l = int(input("Enter Your Choise : "))
                        time.sleep(.25)
                        print("\033[0;32m=" * 40)
                        if l == 1:
                            print("\033[0;32m=" * 40)
                            time.sleep(.25)
                            print("\033[0;31m Bye ".center(47, "="))
                            time.sleep(.25)
                            print("\033[0;32m=" * 40)
                            time.sleep(.25)
                            sys.exit()
                        elif l == 0:
                            lol()
                        else:
                            print("\033[0;31m Error Choise ".center(47, "="))
                            time.sleep(.25)
                            print("\033[0;32m=" * 40)
                            time.sleep(.25)
                            lol()

                    elif x == 3 :
                        x = input("\033[1;36mEnter First  Number : ")
                        z = input("\033[1;36mEnter Second Number : ")
                        a = input("\033[1;36mEnter Third  Number : ")
                        list = [x, z, a]
                        time.sleep(.25)
                        print("\033[0;32m=" * 40)
                        print("\033[1;31mThe Maximum Number Is : \033[1;32m", max(list))
                        print("=" * 40)
                        k = print("""[1] Exit Script
[0] Back """)
                        print("\033[0;32m=" * 40)
                        time.sleep(.25)
                        l = int(input("Enter Your Choise : "))
                        time.sleep(.25)
                        print("\033[0;32m=" * 40)
                        if l == 1:
                            print("\033[0;32m=" * 40)
                            time.sleep(.25)
                            print("\033[0;31m Bye ".center(47, "="))
                            time.sleep(.25)
                            print("\033[0;32m=" * 40)
                            time.sleep(.25)
                            sys.exit()
                        elif l == 0:
                            lol()
                        else:
                            print("\033[0;31m Error Choise ".center(47, "="))
                            time.sleep(.25)
                            print("\033[0;32m=" * 40)
                            time.sleep(.25)
                            lol()

                    elif x == 4 :
                        x = input("\033[1;36mEnter First  Number : ")
                        z = input("\033[1;36mEnter Second Number : ")
                        a = input("\033[1;36mEnter Third  Number : ")
                        b = input("\033[1;36mEnter Fourth Number : ")
                        list = [x, z, a, b]
                        time.sleep(.25)
                        print("\033[0;32m=" * 40)
                        print("\033[1;31mThe Maximum Number Is : \033[1;32m",max(list))
                        print("=" * 40)
                        k = print("""[1] Exit Script
[0] Back """)
                        print("\033[0;32m=" * 40)
                        time.sleep(.25)
                        l = int(input("Enter Your Choise : "))
                        time.sleep(.25)
                        print("\033[0;32m=" * 40)
                        if l == 1:
                            print("\033[0;32m=" * 40)
                            time.sleep(.25)
                            print("\033[0;31m Bye ".center(47, "="))
                            time.sleep(.25)
                            print("\033[0;32m=" * 40)
                            time.sleep(.25)
                            sys.exit()
                        elif l == 0:
                            lol()
                        else:
                            print("\033[0;31m Error Choise ".center(47, "="))
                            time.sleep(.25)
                            print("\033[0;32m=" * 40)
                            time.sleep(.25)
                            lol()

                    elif x == 5 :
                        x = input("\033[1;36mEnter First  Number : ")
                        z = input("\033[1;36mEnter Second Number : ")
                        a = input("\033[1;36mEnter Third  Number : ")
                        b = input("\033[1;36mEnter Fourth Number : ")
                        n = input("\033[1;36mEnter Fifth  Number : ")
                        list = [x, z, a, b, n]
                        time.sleep(.25)
                        print("\033[0;32m=" * 40)
                        print("\033[1;31mThe Maximum Number Is : \033[1;32m", max(list))
                        print("=" * 40)
                        k = print("""[1] Exit Script
[0] Back """)
                        print("\033[0;32m=" * 40)
                        time.sleep(.25)
                        l = int(input("Enter Your Choise : "))
                        time.sleep(.25)
                        print("\033[0;32m=" * 40)
                        if l == 1:
                            print("\033[0;32m=" * 40)
                            time.sleep(.25)
                            print("\033[0;31m Bye ".center(47, "="))
                            time.sleep(.25)
                            print("\033[0;32m=" * 40)
                            time.sleep(.25)
                            sys.exit()
                            
                        elif l == 0:
                            lol()
                        else:
                            print("\033[0;31m Error Choise ".center(47, "="))
                            time.sleep(.25)
                            print("\033[0;32m=" * 40)
                            time.sleep(.25)
                            lol()

                    elif x == 6 :
                        x = input("\033[1;36mEnter First  Number : ")
                        z = input("\033[1;36mEnter Second Number : ")
                        a = input("\033[1;36mEnter Third  Number : ")
                        s = input("\033[1;36mEnter Fourth Number : ")
                        d = input("\033[1;36mEnter Fifth  Number : ")
                        w = input("\033[1;36mEnter Sixth  Number : ")
                        list = [x, z, a, s, d, w]
                        time.sleep(.25)
                        print("\033[0;32m=" * 40)
                        print("\033[1;31mThe Maximum Number Is : \033[1;32m", max(list))
                        print("=" * 40)
                        k = print("""[1] Exit Script
[0] Back """)
                        print("=" * 40)
                        l = int(input("Enter Your Choise : "))
                        if l == 1:
                            print("\033[0;32m=" * 40)
                            time.sleep(.25)
                            print("\033[0;31m Bye ".center(47, "="))
                            time.sleep(.25)
                            print("\033[0;32m=" * 40)
                            time.sleep(.25)
                            sys.exit()
                        elif l == 0:
                            lol()
                        else:
                            print("\033[0;31m Error Choise ".center(47, "="))
                            time.sleep(.25)
                            print("\033[0;32m=" * 40)
                            time.sleep(.25)
                            lol()

                    else:
                            print("\033[0;31m Error Choise ".center(47, "="))
                            time.sleep(.25)
                            print("\033[0;32m=" * 40)
                            time.sleep(.25)
                            lol()
                else:
                            print("\033[0;31m Error Choise ".center(47, "="))
                            time.sleep(.25)
                            print("\033[0;32m=" * 40)
                            time.sleep(.25)
                            lol()
            lol()
else:
                        print("\033[0;31m Error Choise ".center(47, "="))
                        time.sleep(.25)
                        print("\033[0;32m=" * 40)
                        time.sleep(.25)
                        print("\033[0;31m Bye ".center(47, "="))
                        time.sleep(.25)
                        print("\033[0;32m=" * 40)
                        time.sleep(.25)
                        sys.exit()
Main()