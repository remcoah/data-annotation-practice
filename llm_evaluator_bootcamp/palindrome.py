# is_palindrome.py

def is_palindrome(s):
    """ 
    Check if a given string is a palindrome.
    Does not consider spaces or punctuation.
    Args:
        s (str): The string to check.
    Returns:
        bool: True if the string is a palindrome, False otherwise.
    """
    s = s.lower()
    return s == s[::-1]


# Example usage
if __name__ == "__main__":
    test_word = "Hannah"
    result = is_palindrome(test_word)
    print(f"Is {test_word} a palindrome?: {result}")  # Output: true
