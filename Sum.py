# Find the sum off all the odd number from a list of numbers

def AddOdd(VALUES):
    sum = 0
    for number in VALUES:
        if number%2==0:
            continue
        sum+=number
    return sum

if __name__ == '__main__':
    numbers = []
    print("Enter numbers.\t\t\tTo exit, press enter...")
    while(True):
        number = input("Enter a number: ")
        if number == '':
            break
        numbers.append(int(number))
    print("The sum of all the odd numbers in the list {} is {}".format(numbers,AddOdd(numbers)))
