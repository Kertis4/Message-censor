import re

bad_words = [
    "badword1", "nastyword", "forbidden", "curse", "uglyword",
    "evil", "trash", "vulgar", "unwanted", "offensive"
]



bad_pattern = re.compile(r'\b('+'|'.join(bad_words) + r')\b', re.IGNORECASE)


message = input(" write a message - ")

words = message.split()
for i, word in enumerate(words):
    if bad_pattern.search(word):
        words[i] = "*" * len(word)

censored_message = " ".join(words)

print(censored_message)

