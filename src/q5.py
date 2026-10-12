"""HW5 Question 5: Using list comprehension to build a list

Please write a function flatten() that takes a 2D list of ints and returns a single 1D
list containing all the values.

flatten() should take only one argument: a 2D list of ints.
It should return a new list containing all the values from the 2D list, in order.
It should not modify the original 2D list.

Example usage:
flatten([[1, 2, 3], [4, 5, 6]])  # [1, 2, 3, 4, 5, 6]
flatten([[1, 2], [], [], [3]])       # [1, 2, 3]
"""
def flatten(two_d_list: list[list[int]]) -> list[int]:
    return [value for row in two_d_list for value in row]

if __name__ == "__main__":
    print(flatten([[1, 2, 3], [4, 5, 6]]))  # Output: [1, 2, 3, 4, 5, 6]
    print(flatten([[1, 2], [], [], [3]]))       # Output: [1, 2, 3]

    grid = [[1, 2], [3, 4]]
    FLAT = flatten(grid)
    print(FLAT)  # Output: [1, 2, 3, 4]
    print(grid)  # Output: [[1, 2], [3, 4]] (unchanged)