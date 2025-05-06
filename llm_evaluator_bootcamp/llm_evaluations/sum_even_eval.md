# Sum of Even Numbers – LLM Output Evaluation

## Problem Statement
Write a Python function that takes a list of integers and returns the sum of all even numbers in the list.

---

## Output A
def sum_even_numbers(nums):
    total = 0
    for n in nums:
        if n % 2 == 0:
            total += n
    return total

**Explanation:**  
This function initializes a total at 0, then iterates through the list. For each number, it checks if it is even using `% 2 == 0` and adds it to the total.

---

## Output B
def sum_even_numbers(lst):
    total = 0
    for n in lst:
        if n // 2 == 0:
            total += n
    return total

**Explanation:**  
This function loops through the list and adds numbers where `n // 2 == 0`.

---

## Evaluation

**Chosen Output:** A  
**Reasoning:**  
Output A is accurate and precise. It correctly uses the modulo operator to check if each number is even before adding it to the total.

Output B is incorrect. It uses integer division (`//`) and checks if the result is 0. This only evaluates to `True` for `n = 0` or `n = 1`, and misses all other even numbers.

---

## Notes
- `% 2 == 0` is the correct way to test for even numbers.
- `// 2 == 0` is a faulty condition and leads to incorrect results.
- Watch for misuse of operators in LLM-generated logic.
