import sys ,time , termcolor , pyfiglet
print("---WELCOME TO GHOST CALC MAXIMUN & MINIMUM  SCRIPT---")
time.sleep(.2)
print(termcolor.colored(pyfiglet.figlet_format("OSAMA")))
time.sleep(.2)
print("=" * 40)
time.sleep(.25)

def lol():
    print("""[1] Minimum Script 
[2] Maximum Script
[3] BACK
[0] Exit SCRIPT """)
    time.sleep(.25)
    print("=" * 40)
    inp = int(input("Enter Your Choise : "))
    time.sleep(.25)
    print("=" * 40)
    if inp == 0:
        print("=" * 40)
        print(" Bye ".center(40, "="))
        time.sleep(.25)
        print("=" * 40)
        time.sleep(.25)
        sys.exit()
    elif inp == 1:
        x = int(input("Enter How Many Number Do You Want To Enter From 2 To 6 : "))
        time.sleep(.25)
        print("=" * 40)

        if x == 2:
            x = input("Enter First  Number : ")
            z = input("Enter Second Number : ")
            list = [x, z]
            time.sleep(.25)
            print("=" * 40)
            print("The Minimum Number Is : ", min(list))
            print("=" * 40)
            k = print("""[1] Exit Script
[0] Back """)
            print("=" * 40)
            time.sleep(.25)
            l = int(input("Enter Your Choise : "))
            time.sleep(.25)
            print("=" * 40)
            if l == 1:
                print("=" * 40)
                time.sleep(.25)
                print(" Bye ".center(40, "="))
                time.sleep(.25)
                print("=" * 40)
                time.sleep(.25)
                sys.exit()
            elif l == 0:
                lol()
            else:
                print(" Error Choise ".center(40, "="))
                time.sleep(.25)
                print("=" * 40)
                time.sleep(.25)
                lol()

        elif x == 3:
            x = input("Enter First  Number : ")
            z = input("Enter Second Number : ")
            a = input("Enter Third  Number : ")
            list = [x, z, a]
            time.sleep(.25)
            print("=" * 40)
            print("The Minimum Number Is :", min(list))
            print("=" * 40)
            k = print("""[1] Exit Script
[0] Back """)
            print("=" * 40)
            time.sleep(.25)
            l = int(input("Enter Your Choise : "))
            time.sleep(.25)
            print("=" * 40)
            if l == 1:
                print("=" * 40)
                time.sleep(.25)
                print(" Bye ".center(40, "="))
                time.sleep(.25)
                print("=" * 40)
                time.sleep(.25)
                sys.exit()
            elif l == 0:
                lol()
            else:
                print(" Error Choise ".center(40, "="))
                time.sleep(.25)
                print("=" * 40)
                time.sleep(.25)
                lol()

        elif x == 4:
            x = input("Enter First  Number : ")
            z = input("Enter Second Number : ")
            a = input("Enter Third  Number : ")
            b = input("Enter Fourth Number : ")
            list = [x, z, a, b]
            time.sleep(.25)
            print("=" * 40)
            print("The Minimum Number Is : ", min(list))
            print("=" * 40)
            k = print("""[1] Exit Script
[0] Back """)
            print("=" * 40)
            time.sleep(.25)
            l = int(input("Enter Your Choise : "))
            time.sleep(.25)
            print("=" * 40)
            if l == 1:
                print("=" * 40)
                time.sleep(.25)
                print(" Bye ".center(40, "="))
                time.sleep(.25)
                print("=" * 40)
                time.sleep(.25)
                sys.exit()
            elif l == 0:
                lol()
            else:
                print(" Error Choise ".center(40, "="))
                time.sleep(.25)
                print("=" * 40)
                time.sleep(.25)
                lol()

        elif x == 5:
            x = input("Enter First  Number : ")
            z = input("Enter Second Number : ")
            a = input("Enter Third  Number : ")
            b = input("Enter Fourth Number : ")
            n = input("Enter Fifth  Number : ")
            list = [x, z, a, b, n]
            time.sleep(.25)
            print("=" * 40)
            print("The Minimum Number Is : ", min(list))
            print("=" * 40)
            k = print("""[1] Exit Script
[0] Back """)
            print("=" * 40)
            time.sleep(.25)
            l = int(input("Enter Your Choise : "))
            time.sleep(.25)
            print("=" * 40)
            if l == 1:
                print("=" * 40)
                time.sleep(.25)
                print(" Bye ".center(40, "="))
                time.sleep(.25)
                print("=" * 40)
                time.sleep(.25)
                sys.exit()

            elif l == 0:
                lol()
            else:
                print(" Error Choise ".center(40, "="))
                time.sleep(.25)
                print("=" * 40)
                time.sleep(.25)
                lol()

        elif x == 6:
            x = input("Enter First  Number : ")
            z = input("Enter Second Number : ")
            a = input("Enter Third  Number : ")
            s = input("Enter Fourth Number : ")
            d = input("Enter Fifth  Number : ")
            w = input("Enter Sixth  Number : ")
            list = [x, z, a, s, d, w]
            time.sleep(.25)
            print("=" * 40)
            print("The Minimum Number Is : ", min(list))
            print("=" * 40)
            k = print("""[1] Exit Script
[0] Back """)
            print("=" * 40)
            l = int(input("Enter Your Choise : "))
            if l == 1:
                print("=" * 40)
                time.sleep(.25)
                print(" Bye ".center(40, "="))
                time.sleep(.25)
                print("=" * 40)
                time.sleep(.25)
                sys.exit()
            elif l == 0:
                lol()
            else:
                print(" Error Choise ".center(40, "="))
                time.sleep(.25)
                print("=" * 40)
                time.sleep(.25)
                lol()

        else:
            print("Error Choise ".center(40, "="))
            time.sleep(.25)
            print("=" * 40)
            time.sleep(.25)
            lol()
    elif inp == 2:
        x = int(input("Enter How Many Number Do You Want To Enter From 2 To 6 : "))
        time.sleep(.25)
        print("=" * 40)

        if x == 2:
            x = input("Enter First  Number : ")
            z = input("Enter Second Number : ")
            list = [x, z]
            time.sleep(.25)
            print("=" * 40)
            print("The Maximum Number Is : ", max(list))
            print("=" * 40)
            k = print("""[1] Exit Script
[0] Back """)
            print("=" * 40)
            time.sleep(.25)
            l = int(input("Enter Your Choise : "))
            time.sleep(.25)
            print("=" * 40)
            if l == 1:
                print("=" * 40)
                time.sleep(.25)
                print(" Bye ".center(40, "="))
                time.sleep(.25)
                print("=" * 40)
                time.sleep(.25)
                sys.exit()
            elif l == 0:
                lol()
            else:
                print(" Error Choise ".center(40, "="))
                time.sleep(.25)
                print("=" * 40)
                time.sleep(.25)
                lol()

        elif x == 3:
            x = input("Enter First   Number  : ")
            z = input("Enter Second  Number  : ")
            a = input("Enter Third   Number  : ")
            list = [x, z, a]
            time.sleep(.25)
            print("=" * 40)
            print("The Maximum Number Is : ", max(list))
            print("=" * 40)
            k = print("""[1] Exit Script
[0] Back """)
            print("=" * 40)
            time.sleep(.25)
            l = int(input("Enter Your Choise : "))
            time.sleep(.25)
            print("=" * 40)
            if l == 1:
                print("=" * 40)
                time.sleep(.25)
                print(" Bye ".center(40, "="))
                time.sleep(.25)
                print("=" * 40)
                time.sleep(.25)
                sys.exit()
            elif l == 0:
                lol()
            else:
                print(" Error Choise ".center(40, "="))
                time.sleep(.25)
                print("=" * 40)
                time.sleep(.25)
                lol()

        elif x == 4:
            x = input("Enter First  Number : ")
            z = input("Enter Second Number : ")
            a = input("Enter Third  Number : ")
            b = input("Enter Fourth Number : ")
            list = [x, z, a, b]
            time.sleep(.25)
            print("=" * 40)
            print("The Maximum Number Is : ", max(list))
            print("=" * 40)
            k = print("""[1] Exit Script
[0] Back """)
            print("=" * 40)
            time.sleep(.25)
            l = int(input("Enter Your Choise : "))
            time.sleep(.25)
            print("=" * 40)
            if l == 1:
                print("=" * 40)
                time.sleep(.25)
                print(" Bye ".center(40, "="))
                time.sleep(.25)
                print("=" * 40)
                time.sleep(.25)
                sys.exit()
            elif l == 0:
                lol()
            else:
                print(" Error Choise ".center(40, "="))
                time.sleep(.25)
                print("=" * 40)
                time.sleep(.25)
                lol()

        elif x == 5:
            x = input("Enter First  Number : ")
            z = input("Enter Second Number : ")
            a = input("Enter Third  Number : ")
            b = input("Enter Fourth Number : ")
            n = input("Enter Fifth  Number : ")
            list = [x, z, a, b, n]
            time.sleep(.25)
            print("=" * 40)
            print("The Maximum Number Is : ", max(list))
            print("=" * 40)
            k = print("""[1] Exit Script
[0] Back """)
            print("=" * 40)
            time.sleep(.25)
            l = int(input("Enter Your Choise : "))
            time.sleep(.25)
            print("=" * 40)
            if l == 1:
                print("=" * 40)
                time.sleep(.25)
                print(" Bye ".center(40, "="))
                time.sleep(.25)
                print("=" * 40)
                time.sleep(.25)
                sys.exit()

            elif l == 0:
                lol()
            else:
                print(" Error Choise ".center(40, "="))
                time.sleep(.25)
                print("=" * 40)
                time.sleep(.25)
                lol()

        elif x == 6:
            x = input("Enter First  Number : ")
            z = input("Enter Second Number : ")
            a = input("Enter Third  Number : ")
            s = input("Enter Fourth Number : ")
            d = input("Enter Fifth  Number : ")
            w = input("Enter Sixth  Number : ")
            list = [x, z, a, s, d, w]
            time.sleep(.25)
            print("=" * 40)
            print("The Maximum Number Is : ", max(list))
            print("=" * 40)
            k = print("""[1] Exit Script
[0] Back """)
            print("=" * 40)
            l = int(input("Enter Your Choise : "))
            if l == 1:
                print("=" * 40)
                time.sleep(.25)
                print(" Bye ".center(40, "="))
                time.sleep(.25)
                print("=" * 40)
                time.sleep(.25)
                sys.exit()
            elif l == 0:
                lol()
            else:
                print(" Error Choise ".center(40, "="))
                time.sleep(.25)
                print("=" * 40)
                time.sleep(.25)
                lol()

        else:
            print(" Error Choise ".center(40, "="))
            time.sleep(.25)
            print("=" * 40)
            time.sleep(.25)
            lol()
    elif inp == 3:
        from MainWithoutColor import nj

    else:
            print(" Error Choise ".center(40, "="))
            time.sleep(.25)
            print("=" * 40)
            time.sleep(.25)
            lol()
lol()