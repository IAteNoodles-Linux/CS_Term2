# Check is a character is an alphabet or digit.

def check(char):
    if char.isalpha():
        return 1
    elif char.isdigit():
        return 2
    else:
        return 0

if __name__ == '__main__':
    char = input("Enter a character: ")
    result = check(char)
    print("The character is {}".format("an alphabet" if result == 1 else "a digit" if result == 2 else "not an alphabet or digit"))
