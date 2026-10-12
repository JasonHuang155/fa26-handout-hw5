"""HW5 Question 4: Slicing strings

Please write a function remove_middle() that returns a version of the passed string with the 
characters between two given indices removed.

remove_middle() should take three arguments: the string, the start index, and the end index.
It should return a version of the string with the characters between the start (inclusive) and 
end (exclusive) indices removed.

If the start index is 0 or negative, the removal should start from the beginning of the string.
If the end index is greater than the length of the string, the removal should go up to the end 
of the string.
If the start index is greater than the length of the string, no characters should be removed.
If the start index is greater than the end index, no characters should be removed.

Example usage:
remove_middle("elephant", 2, 5)  # "elant"
remove_middle("elephant", 2, 6)  # "elnt"
remove_middle("elephant", 0, 100)  # ""
"""

def remove_middle(text: str, start: int, end: int) -> str:
    start = max(start, 0)

    if start > end:
        return text
    return text[:start] + text[end:]

if __name__ == "__main__":
    print(remove_middle("elephant", 2, 5))    # elant
    print(remove_middle("elephant", 2, 6))    # elnt
    print(remove_middle("elephant", 0, 100))  # (empty string)
    print(remove_middle("elephant", -3, 2))   # ephant
    print(remove_middle("elephant", 20, 30))  # elephant
    print(remove_middle("elephant", 5, 2))    # elephant