# Reads a text file line by line and prints it to the screen, each word seperated by a #

if __name__ == '__main__':
    with open('/home/nuub/Study/CS/Project/Files/GNU-LINUX.txt', 'r') as f:
        for line in f:
            print(line.replace(' ', '#'), end='')
            print()

    
