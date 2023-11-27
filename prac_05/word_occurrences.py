"""
Word Occurrences
Estimate: 20 minutes 00 seconds
Actual:   20 minutes 24 seconds
"""

TEST_STRING = 'this is a collection of words of nice words this is a fun thing it is'

# input_text = input("text: ")
input_text = TEST_STRING
words = input_text.split()
words.sort()

word_to_count = {}
for word in words:
    try:
        word_to_count[word] += 1
    except KeyError:
        word_to_count[word] = 1

longest_word_length = -1
for word in words:
    if len(word) > longest_word_length:
        longest_word_length = len(word)

for word, value in word_to_count.items():
    print(f"{word:{longest_word_length}} : {value}")
