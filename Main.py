import num

def ask():
    while True:
        print("Please choose from the following option:\n")
        print("1. Perfume\t2. Cosmetic\t3. Medicine\t")
        try:
            s = input(': ')
            ["1",'2','3'].index(s)
        except ValueError:
            print("Not a valid option!")
        else:
            break
    num.decorate(s)


def start():
    print('Welcome to star pharma!')
    while True:
        ask()
        print("Press '1' for another ticket'\nPress '2' to exit")
        try:
            s = input(': ')
            ['1','2'].index(s)
        except ValueError:
            print("choose a valid option!")
        else:
            if s=="2":
                break


start()
