def starFormation2(n):
    # Rounded Up
    n = (-(-n//2))
    for i in range(0, n):
        for j in range(0, i + 1):
            print('* ' , end='')
        print('')
    for i in reversed(range(0, n)):
        for j in range(1, i + 1):
            print('* ' , end='')
        print('')

n = int(input('Banyak baris yang akan dicetak : '))
starFormation2(n)
