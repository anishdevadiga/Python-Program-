word_input = input("Enter a alphabet: ")
word=word_input.lower()
if word == 'a' or word == 'e' or  word == 'i' or word == 'o' or word == 'u' :
    print(f"{word} is an vowel")
elif word == 'y':
    print(f"{word} is an vowel or an consonant")
else:
    print(f"{word} is an consonant")