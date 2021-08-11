1mport sys

ALPHABET = 'abcdefghijklmnopqrstuvwxyz'

args = sys.argv[1:]

for arg in args:

    print(arg)

text = 'spam '.join(args)

print(text)

lowercase_letter = text[0].lower()

print(lowercase_letter)

lowercase_text = [letter.lower()for letter in text]
lowercase_text = text.lower()
print(lowercase_text)

lowercase_text = [letter if letter in ALPHABET else '' for letter in lowercase_text]

print(lowercase_letter)
lowercase_text = ''.join(lowercase_text)

frequencies = {}
for letter in ALPHABET:
    frequencies[letter] = 0
for letter in lowercase_text:

    if letter not in frequencies:

        frequencies[letter] = 1
    
    else:

        frequencies[letter] += 1

print(frequencies)

for letter in ALPHABET:

    count = frequencies[letter]

    print(letter, end=' ')

    for c in range(count):

        print('|', end='')

    print()
