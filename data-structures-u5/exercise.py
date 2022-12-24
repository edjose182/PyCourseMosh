### Find the most repitly character in a text
from pprint import pprint # This gives the printed information a new format

sentence = "This is a common interview question"

repeat_letters = {}

for character in sentence:
    if character in repeat_letters.keys():
        repeat_letters[character] += 1
    else:
        repeat_letters[character] = 1

print(sorted(repeat_letters.items(),key=lambda kv:kv[1],reverse=True))
