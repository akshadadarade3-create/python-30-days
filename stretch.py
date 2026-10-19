word = ["neha","racecar", " banana", "madam", "computer", "civic", "elephant", "radar", "coffee", "a man a plan a canal, Panama", "hello world", "kayak", "sunshine", "rotor", "keyboard", "step on no pets"]
condition = lambda x: ''.join(c.lower() for c in x if c.isalnum()) == \
                      ''.join(c.lower() for c in x if c.isalnum())[::-1]

result = filter(condition, word)
palindrome = list(result)

not_palindrome = list(filter(lambda x: not condition(x), word))

print(f"Palindrome words:\n{palindrome}")

print(f"\nNot palindrome words:\n{not_palindrome}")
     