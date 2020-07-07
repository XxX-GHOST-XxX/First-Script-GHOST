import sys ,time , termcolor , pyfiglet
print("---WELCOME TO GHOST CALC AREAS  SCRIPT---")
time.sleep(.2)
print(termcolor.colored(pyfiglet.figlet_format("OSAMA")))
time.sleep(.2)
print("=" * 40)
time.sleep(.25)


def numsber():
    print("""[1] EVEN & ODD
[0] BACK""")
    print("=" * 40)
    time.sleep(.25)
    kl=int(input("Enter Your Choise : "))
    time.sleep(.25)
    print("=" * 40)
    if kl == 1 :
        number = int(input("Enter Numbers : "))

        if number % 2 == 0:

            print(f"This Number {number} Is even")
            print("=" * 40)
            print("""[1] Exit Script
[0] Back """)
            print("=" * 40)
            time.sleep(.25)
            inp = int(input("Enter Your Choise : "))
            time.sleep(.25)
            print("=" * 40)
            if inp == 0:
                numsber()
            elif inp == 1:
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
                numsber()

        else:

            print(f"This Number {number} Is odd")
            print("=" * 40)
            print("""[1] Exit Script
[0] Back """)
            print("=" * 40)
            time.sleep(.25)
            inp = int(input("Enter Your Choise : "))
            time.sleep(.25)
            print("=" * 40)
            if inp == 0:
                numsber()
            elif inp == 1:
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
                numsber()
    elif kl == 0 :
        from MainWithoutColor import nj
    else:
        print(" Error Choise ".center(40, "="))
        print("=" * 40)
        time.sleep(.25)
        numsber()


numsber()
