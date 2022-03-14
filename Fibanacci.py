# Generate first 15 fibonacci numbers.

def fib(n):
    a, b = 0, 1
    print(0,end=' ')
    for i in range(n):
        a, b = b, a + b
        print(a, end=' ')
    print()

if __name__ == '__main__':
    fib(15)

