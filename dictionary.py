dictionary = {
    "friend" : "मित्र",
    "water" : "पाणी",
    "food" : "अन्न",
    "college":"महाविद्यालय",
    "intelligence":"बुद्धिमत्ता",
    "machine":"यंत्र",
    "hello":"नमस्कार",
    "needs":"गरजा",
    "our":"आपल्या",

}
sentence = input("Enter an English sentence or word: ").lower()

words = sentence.split()

for word in words:
    if word in dictionary:
        print(dictionary[word], end=" ")
    else:
        print("[not found]", end=" ")