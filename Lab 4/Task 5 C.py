import re
from collections import Counter

def analyze_word_frequency():
    """
    Function to process text and analyze word frequency.
    Takes input paragraph, converts to lowercase, removes punctuation,
    and returns the most frequently used word.
    """
    
    # Get input paragraph from user
    print("Enter a paragraph to analyze:")
    paragraph = input()
    
    if not paragraph.strip():
        print("No text provided!")
        return
    
    # Convert to lowercase
    text_lower = paragraph.lower()
    
    # Remove punctuation using regex
    # This removes all punctuation marks and special characters
    text_clean = re.sub(r'[^\w\s]', '', text_lower)
    
    # Split into words and remove empty strings
    words = [word for word in text_clean.split() if word]
    
    if not words:
        print("No valid words found in the text!")
        return
    
    # Count word frequency using Counter
    word_count = Counter(words)
    
    # Find the most frequent word
    most_frequent_word = word_count.most_common(1)[0]
    
    # Display results
    print("\nText Analysis Results:")
    print("=" * 30)
    print(f"Original text: {paragraph}")
    print(f"Cleaned text (lowercase, no punctuation): {text_clean}")
    print(f"Total words: {len(words)}")
    print(f"Unique words: {len(word_count)}")
    print(f"Most frequent word: '{most_frequent_word[0]}' (appears {most_frequent_word[1]} times)")
    
    # Display all word frequencies
    print(f"\nAll word frequencies:")
    for word, count in word_count.most_common():
        print(f"'{word}': {count} times")
    
    return most_frequent_word[0]

# Alternative function that returns just the most frequent word
def get_most_frequent_word(text):
    """
    Function that takes text as parameter and returns the most frequent word.
    
    Args:
        text (str): Input text to analyze
        
    Returns:
        str: Most frequently used word
    """
    
    # Convert to lowercase
    text_lower = text.lower()
    
    # Remove punctuation
    text_clean = re.sub(r'[^\w\s]', '', text_lower)
    
    # Split into words
    words = [word for word in text_clean.split() if word]
    
    if not words:
        return None
    
    # Count frequency and return most frequent
    word_count = Counter(words)
    return word_count.most_common(1)[0][0]

# Run the function
if __name__ == "__main__":
    print("Word Frequency Analyzer")
    print("=" * 25)
    analyze_word_frequency()
    
    # Example usage of the alternative function
    print("\n" + "=" * 50)
    print("Example with pre-defined text:")
    print("-" * 30)
    
    sample_text = "Hello world! This is a test. Hello again, world. The world is beautiful."
    result = get_most_frequent_word(sample_text)
    print(f"Sample text: {sample_text}")
    print(f"Most frequent word: '{result}'")
