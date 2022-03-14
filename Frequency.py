# Find the frequecy of all numbers in a list.

def get_frequency(numbers):
    frequency = {}
    for number in numbers:
        if number in frequency:
            frequency[number] += 1
        else:
            frequency[number] = 1
    return frequency

if __name__ == '__main__':
    numbers = []
    print("Enter numbers to find their frequency:\t\tTo exit, press enter...")
    while(True):
        number = input('Enter a number: ')
        if number == '':
            break
        numbers.append(int(number))
    frequency = get_frequency(numbers)
    for number in frequency:
        print('{} occurs {} times'.format(number, frequency[number]))
