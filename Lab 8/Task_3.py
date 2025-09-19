import re

def is_sentence_palindrome(sentence):
    # Remove non-alphanumeric characters and convert to lowercase
    cleaned = re.sub(r'[^a-zA-Z0-9]', '', sentence).lower()
    return cleaned == cleaned[::-1]


if __name__ == "__main__":
    # Test case 1
    print(f"Test case 1 \n Sentence: 'A man a plan a canal Panama' ->", is_sentence_palindrome("A man a plan a canal Panama"))
    # returns: True

    # Test case 2
    print(f"Test case 2 \n Sentence: 'Hello World' ->", is_sentence_palindrome("Hello World"))
    # returns: False

    # Test case 3
    print(f"Test case 3 \n Sentence: 'No lemon, no melon' ->", is_sentence_palindrome("No lemon, no melon"))
    # returns: True
