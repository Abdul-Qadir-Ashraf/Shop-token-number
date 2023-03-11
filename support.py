def perfume():
    l=100
    while True:
        yield f'P-{l}'
        l= l+1

def cosmetic():
    l =100
    while True:
        yield f'C-{l}'
        l+=1

def medicine():
    l=100
    while True:
        yield f"M-{l}"
        l+=1

p = perfume()
c = cosmetic()
m = medicine()

def decorate(d):
    print('\n')
    print('*'*23)
    if d =='1':
        print(f"Your token number is: {(next(p))}")
    elif d =='2':
        print(f"Your token number is: {next(c)}")
    elif d =='3':
        print(f"Your token number is: {next(m)}")
    print("Keep waiting your turn will come soon!")
    print("*"*23)
    print('\n')
