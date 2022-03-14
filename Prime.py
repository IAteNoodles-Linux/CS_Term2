# A python program to check if a number is prime or not.
# We check if a number is prime or not by sqrt n approach.

def check_prime(num):
    if num == 1:
        return False
    counter = 2
    while(counter**2 <= num):
        if num % counter == 0:
            return False
        counter += 1
    return True

if __name__ == '__main__':
    num = int(input("Enter a number: "))
    if check_prime(num):
        print("{} is a prime number.".format(num))
    else:
        print("{} is not a prime number.".format(num))















