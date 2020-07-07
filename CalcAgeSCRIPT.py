import sys ,time , termcolor , pyfiglet
print("----WELCOME TO GHOST CALC AGE SCRIPT----")
time.sleep(.2)
print(termcolor.colored(pyfiglet.figlet_format("OSAMA")))
time.sleep(.2)
print("=" * 40)
def agae() :
    print("""[1] CALC AGE
[0] BACK""")
    print("=" * 40)
    time.sleep(.25)
    kl = int(input("Enter Your Choise : "))
    time.sleep(.25)
    print("=" * 40)
    if kl == 1:
        age = int(input("Enter Your Age : "))
        if age < 1:
            print("=" * 40)
            time.sleep(.25)
            print("Your Are Not Born Yet 🤣😋")
            print("=" * 40)
            time.sleep(.25)
            agae()


        if age <= 80:
            print("=" * 40)
            years = age * 1
            month = years * 12
            week = month * 4
            day = week * 7
            hour = day * 24
            min = hour * 60
            sec = min * 60
            print(f"In Years : {years} Year.")
            time.sleep(.25)
            print(f"In month : {month} Month.")
            time.sleep(.25)
            print(f"In week  : {week:,} Week.")
            time.sleep(.25)
            print(f"In day   : {day:,} Day.")
            time.sleep(.25)
            print(f"In hour  : {hour:,} Hour.")
            time.sleep(.25)
            print(f"In min   : {min:,} Min.")
            time.sleep(.25)
            print(f"In sec   : {sec:,} Sec.")
            print("=" * 40)
            print("""[1] Exit Script
[0] Back """)
            print("=" * 40)
            time.sleep(.25)
            inp = int(input("Enter Your Choise : "))
            time.sleep(.25)
            print("=" * 40)
            if inp == 0:
                agae()
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
                agae()


        else:
            if age > 80:
                print("=" * 40)
                time.sleep(.25)
                print("Your Are Already Dead ☠💀 ")
                print("=" * 40)
                time.sleep(.25)
                print("""[1] Exit Script
[0] Back """)
                print("=" * 40)
                time.sleep(.25)
                inp = int(input("Enter Your Choise : "))
                time.sleep(.25)
                print("=" * 40)
                if inp == 0:
                    agae()
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
                    agae()
    elif kl == 0 :
        from MainWithoutColor import nj
    else:
        print(" Error Choise ".center(40, "="))
        print("=" * 40)
        time.sleep(.25)
        agae()
agae()