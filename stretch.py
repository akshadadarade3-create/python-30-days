sentence = input("Enter a sentence: ")

word_lengths = {word: len(word) for word in sentence.split()}

print(word_lengths)