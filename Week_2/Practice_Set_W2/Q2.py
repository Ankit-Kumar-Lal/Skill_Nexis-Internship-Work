# Write a dictionary program to count word frequency

sentence = input("Enter a sentence: ")

words = sentence.split()
freq = {}

for word in words:
    if word in freq:
        freq[word] += 1
    else:
        freq[word] = 1

print("Word frequency:")
for word in freq:
    print(word, ":", freq[word])
