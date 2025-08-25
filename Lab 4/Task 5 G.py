import string
from collections import Counter

def most_frequent_word(paragraph: str) -> str:
    """
    Processes the input paragraph, converts text to lowercase,
    removes punctuation, and returns the most frequently used word.
    """
    # Convert to lowercase
    text = paragraph.lower()
    # Remove punctuation
    text = text.translate(str.maketrans('', '', string.punctuation))
    # Split into words
    words = text.split()
    # Count word frequency
    freq = Counter(words)
    # Find the most common word
    most_common = freq.most_common(1)
    return most_common[0][0] if most_common else None

# Example usage:
paragraph = input("Enter a paragraph: ")
result = most_frequent_word(paragraph)
if result:
    print(f"The most frequently used word is: '{result}'")
else:
    print("No words found in the input.")