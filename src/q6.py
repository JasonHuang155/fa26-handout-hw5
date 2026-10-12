"""HW5 Question 6: Using list comprehension, but not to build a list

Please write a function sum_2d() that takes a 2D list of ints and returns the sum of 
all the ints in the list.

sum_2d() should take only one argument, which is the 2D list of ints.

Example usage:
sum_2d([[1, 2, 3], [4, 5, 6]])    # 21
sum_2d([[1, 2], [3, 4], [5, 6]])  # 21
sum_2d([[10]])                    # 10
sum_2d([[]])                      # 0
"""

def sum_2d(two_d_list: list[list[int]]) -> int:
    return sum(value for row in two_d_list for value in row)

if __name__ == "__main__":
    print(sum_2d([[1, 2, 3], [4, 5, 6]]))    # 21
    print(sum_2d([[1, 2], [3, 4], [5, 6]]))  # 21
    print(sum_2d([[10]]))                    # 10
    print(sum_2d([[]]))                      # 0