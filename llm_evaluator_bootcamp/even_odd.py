# even_odd.py

def check_even_odd(num: int) -> str:
    """
    Returns 'Even' if the number is even, 'Odd' otherwise.
    """
    return "Even" if num % 2 == 0 else "Odd"

# Example usage:
if __name__ == "__main__":
    print(check_even_odd(4))  # Output: Even
    print(check_even_odd(7))  # Output: Odd
