# Count the number of vowels and consonants in a text file.

if __name__ == '__main__':
    with open('/home/nuub/Study/CS/Project/Files/GNU-LINUX.txt', 'r') as f:
        text = f.read()
        vowels = 0
        consonants = 0
        for char in text:
            if char in 'aeiouAEIOU':
                vowels += 1
            elif char in 'bcdfghjklmnpqrstvwxyzBCDFGHJKLMNPQRSTVWXYZ':
                consonants += 1
        print('Vowels:', vowels)
        print('Consonants:', consonants)
