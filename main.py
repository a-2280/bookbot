with open('./books/frankenstein.txt') as frankenstein:
    contents = frankenstein.read()

words = contents.split()

character_count = { }
for word in words:
    lowered_word = word.lower()
    for letters in lowered_word:
        if letters in character_count:
            character_count[letters] += 1
        else:
            character_count[letters] = 1

print('--- Begin report of books/frankenstein.txt ---')
print(f'{len(words)} words found in the document')
print()
sorted_items = sorted(character_count.items())
for character, count in sorted_items:
    print(f'The {character} character was found {count} times')
print('--- End report ---')