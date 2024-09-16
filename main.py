with open('./books/frankenstein.txt') as frankenstein:
    contents = frankenstein.read()


words = contents.split()
print(len(words))

character_count = {}
for word in words:
    lowered_word = word.lower()
    for letters in word:
        print(letters)