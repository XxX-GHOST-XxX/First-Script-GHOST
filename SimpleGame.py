import random, sys ,time , termcolor , pyfiglet
from random import randint

print("=" * 40)
time.sleep(.2)
print(termcolor.colored(pyfiglet.figlet_format("OSAMA"),color="red"))
time.sleep(.2)
print("=" * 40)
time.sleep(.2)

def maina() :
    print("""[1] START GAME 
[0] BACK""")
    print("=" * 40)
    time.sleep(.25)
    kl = int(input("Enter Your Choise : "))
    time.sleep(.25)
    print("=" * 40)
    if kl == 1:
        ce = randint(1, 5)
        i = int(input("Enter Random Number From (1 To 5) : "))
        if 0 < i < 5 :
            time.sleep(.2)
            if i == ce :
                print("=" * 40)
                time.sleep(.2)
                c= print("Good You Are Win 🥳")
                time.sleep(.2)
                print("=" * 40)
                time.sleep(.2)
                y=print("""[0] Exit Script
[1] Play Again""")
                time.sleep(.2)
                print("=" * 40)
                x = int(input("Enter Your Choice : "))
                if x ==0 :
                    print("=" * 40)
                    time.sleep(.2)
                    print("Bye")
                    time.sleep(.2)
                    print("=" * 40)
                    sys.exit()
                elif x==1 :
                    maina()

            else:
                time.sleep(.2)
                print("=" * 40)
                time.sleep(.2)
                print("Try Again 😉")
                time.sleep(.2)
                print("=" * 40)
                time.sleep(.2)
                print("Write Number Is : ",ce)
                print("=" * 40)
                time.sleep(.2)
                maina()
        else:
            print("=" * 40)
            time.sleep(.2)
            print ("Your Number Is Not For Range (1-5)")
            print("=" * 40)
            time.sleep(.2)
            maina()
    elif kl == 0 :
        from MainWithoutColor import nj
    else:
        print(" Error Choise ".center(40, "="))
        print("=" * 40)
        time.sleep(.25)
        maina()
maina()
