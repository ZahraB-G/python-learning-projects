# Find the three most common words in the Text.
from collections import Counter
text = "apple orange apple banana orange apple pear"
counter = Counter(text.split())
print(f'The three most common words are {counter.most_common(3)}')

# Count frequency of each letter, ignoring spaces and case.
sentence = "Mississippi River"
sentence = sentence.lower().replace(' ',"")
counter = Counter(sentence)
print(counter)