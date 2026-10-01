word = input("Enter the Words:").lower()
vowel = {"a","e","i","o","u"}
found = set()
for letter in word:
    if letter in vowel:
       found.add(letter)
missing = vowel-found
print("vowels present:",sorted(found))
print("vowels missing:",sorted(missing))