from collections import Counter
import string
def get_most_frequent_words(filename, top_n = 5):
    try:
        with open(filename, 'r') as file:
            text = file.read()
        text = text.lower()
        text = text.translate(str.maketrans('', '', string.punctuation))
        words = text.split()
        word_counts = Counter(words)
        most_common = word_counts.most_common(top_n)
        print(f"\nTop {top_n} most frequent words in '{filename}':")
        for word, count in most_common:
            print(f"{word}: {count} times")
    except FileNotFoundError:
        print(f"Error: The file '{filename}' was not found.")

filename = input("Enter the filename(e.g., 'sample.txt'): ")
get_most_frequent_words(filename, top_n = 5)