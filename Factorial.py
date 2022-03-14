# Calculate factorial of a number.

def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)

if __name__ == '__main__':
    print("Factorial: {}".format(factorial(int(input("Enter a number: ")))))

