def average(num):
    sum_num = 0
    for data in num:
        sum_num = sum_num + data          
    average = sum_num / len(num)
    return average

def main():
    try:
        num = int(input('\nEnter integer number : '))
        list_num.append(num)
        again = input("\nAgain [y/n] ? : ")
        if again == 'y':
            main()
        elif again.lower() == 'n':
            print("\nThe average from", list_num, "is", average(list_num))
            exit()
        else:
            print("\nInput unknown\nPlease enter the correct choice!\n")
            main()
    except ValueError:
        print('\nNumbers not an integer')
        main()

list_num = []
main()
