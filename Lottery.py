# Generate a random number between 1 to 6 and check if the user guessed it.

if __name__ == '__main__':
    from random import randint
    num = randint(1, 6)
    if int(input('Guess a number between 1 and 6: ')) == num:
        print('You guessed it!')
    else:
        print('You guessed wrong. The number was {}.'.format(num))
