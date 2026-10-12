"""HW5 Question 3: Modifying a 2D list

Please write a function append_to_each_row() that appends a given value to the end of 
every row in a 2D list.

append_to_each_row() should take two arguments:
1. The 2D list of ints to be modified in place
2. The int value to append to the end of each row of the 2D list

It should modify the 2D list in place, rather than returning a new list.

Example usage:
grid = [
    [1, 2],
    [3, 4, 5, 6],
    [7, 8, 9]
]
append_to_each_row(grid, 0)
print(grid)  # [[1, 2, 0], [3, 4, 5, 6, 0], [7, 8, 9, 0]]
"""
def append_to_each_row(grid: list[list[int]], value: int) -> None:
    for row in grid:
        row.append(value)

if __name__ == "__main__":
    # Example usage
    grid = [
        [1, 2],
        [3, 4, 5, 6],
        [7, 8, 9]
    ]
    append_to_each_row(grid, 0)
    print(grid)  # Output: [[1, 2, 0], [3, 4, 5, 6, 0], [7, 8, 9, 0]]