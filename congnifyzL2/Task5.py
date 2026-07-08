from collections import Counter
import string
filename = r"E:\coding\python.pyprograming\congnifyzL2\sample.txt" 
word_count = Counter()

try:
    with open(filename, "r", encoding="utf-8") as file:
        text = file.read().lower()
        text = text.translate(str.maketrans("", "", string.punctuation))
        words = text.split()
        word_count.update(words)

    print("\nWord Occurrences (Alphabetical Order):")
    print("-" * 35)
    print(f"{'Word':<20}{'Count'}")
    print("-" * 35)

    for word in sorted(word_count):
        print(f"{word:<20}{word_count[word]}")

except FileNotFoundError:
    print(f"Error: The file '{filename}' was not found.")