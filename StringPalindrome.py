# Find all the palindrome words in a string and print them.

if __name__ == '__main__':
    from Palindrome import isPalindrome
    text=input("Enter a string: ")
    for word in text.split():
        if isPalindrome(word):
            print(word)
