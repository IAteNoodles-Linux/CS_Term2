# Display ASCII code for a character and vice versa.

if __name__ == '__main__':
    char = input("Please enter your input: ")
    try:
        print("The ASCII code for {} is {}".format(char, ord(char)))
    except TypeError:
        print("The character representation of {} is {}".format(char,chr(int(char))))
