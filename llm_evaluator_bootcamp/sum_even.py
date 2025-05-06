# sum_even.py

def sum_even_numbers(nums: list[int]) -> int:
    """
    Returns the sum of all even numbers in the given list.
    
    Args:
        nums (list[int]): A list of integers.
    
    Returns:
        int: Sum of all even numbers.
    """
    return sum(n for n in nums if n % 2 == 0)


# Example usage
if __name__ == "__main__":
    test_list = [1, 2, 3, 4, 5, 6]
    result = sum_even_numbers(test_list)
    print(f"Sum of even numbers: {result}")  # Output: 12
