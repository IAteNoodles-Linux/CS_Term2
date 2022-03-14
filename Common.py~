# Take a sample of ten phishing emails (or any text files) and find the most common words in them.

# Using Shakespeare's Hamlet as a sample, find the most common words in the sample.

text=""
for i in range(10):
    with open("./Files/Hamlet/"+str(i)) as f:
        text += f.read()

count = {}
for word in text.split():
    if word in count:
        count[word] += 1
    else:
        count[word] = 1

for word in sorted(count, key=count.get):
    print(word, count[word])
