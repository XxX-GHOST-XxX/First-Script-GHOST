import sys ,time , termcolor , pyfiglet
print("---WELCOME TO GHOST CALC AREAS  SCRIPT---")
time.sleep(.2)
print(termcolor.colored(pyfiglet.figlet_format("OSAMA")))
time.sleep(.2)
print("=" * 40)
time.sleep(.25)

def AREA():
    print("""[1] Square
[2] Rectangle
[3] Tringle
[0] BACK""")
    time.sleep(.25)
    print("=" * 40)
    time.sleep(.25)
    tg = int(input("ENTER YOUR CHOICE : "))
    time.sleep(.25)
    print("=" * 40)
    if tg ==1 :
            inp = int(input("Enter Length :"))
            time.sleep(.25)
            print("=" * 40)
            time.sleep(.25)
            print("Square Area              = ", inp * inp)
            time.sleep(.25)
            print("Square Circumference     = ", inp * 4)
            time.sleep(.25)
            print("=" * 40)
            time.sleep(.25)
            print("""[1] Exit Script
[0] Back """)
            time.sleep(.25)
            print("=" * 40)
            time.sleep(.25)
            inp = int(input("Enter Your Choise : "))
            time.sleep(.25)
            print("=" * 40)
            time.sleep(.25)
            if inp == 0:
                AREA()
                time.sleep(.25)
            elif inp == 1:
                time.sleep(.25)
                print("=" * 40)
                time.sleep(.25)
                print(" Bye ".center(40, "="))
                time.sleep(.25)
                print("=" * 40)
                time.sleep(.25)
                sys.exit()
            else:
                print(" Error Choise ".center(40, "="))
                time.sleep(.25)
                print("=" * 40)
                time.sleep(.25)
                AREA()

    elif tg == 2:
            inp = int(input("Enter Length : "))
            time.sleep(.25)
            inp2 = int(input("Enter Width  : "))
            time.sleep(.25)
            print("=" * 40)
            time.sleep(.25)
            print("Rectangle Area           =  ", inp * inp2)
            time.sleep(.25)
            print("Rectangle Circumference  =  ", (inp + inp2) * 2)
            time.sleep(.25)
            print("=" * 40)
            time.sleep(.25)
            print("""[1] Exit Script
[0] Back """)
            time.sleep(.25)
            print("=" * 40)
            time.sleep(.25)
            inp = int(input("Enter Your Choise : "))
            time.sleep(.25)
            print("=" * 40)
            if inp == 0:
                AREA()
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
                time.sleep(.25)
                print("=" * 40)
                time.sleep(.25)
                AREA()

    elif tg == 3:
            inp = int(input("Enter Trriangle's Base Length     : "))
            time.sleep(.25)
            inp2 = int(input("Enter The Height Of The Triangle  : "))
            time.sleep(.25)
            print("=" * 40)
            time.sleep(.25)
            print(" Trriangle Area =  ", (0.5 * inp) * inp2)
            time.sleep(.25)
            print("=" * 40)
            time.sleep(.25)
            print("""[1] Exit Script
[0] Back """)
            time.sleep(.25)
            print("=" * 40)
            time.sleep(.25)
            inp = int(input("Enter Your Choise : "))
            time.sleep(.25)
            print("=" * 40)
            if inp == 0:
                AREA()
            elif inp == 1:
                print("=" * 40)
                time.sleep(.25)
                print("Bye ".center(40, "="))
                time.sleep(.25)
                print("=" * 40)
                time.sleep(.25)
                sys.exit()
            else:
                print(" Error Choise ".center(40, "="))
                time.sleep(.25)
                print("=" * 40)
                time.sleep(.25)
                AREA()
    elif tg == 0:
        from MainWithoutColor import nj
    else :
        print(" Error Choise ".center(40, "="))
        time.sleep(.25)
        print("=" * 40)
        time.sleep(.25)
        AREA()
AREA()