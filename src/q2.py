"""HW5 Question 2: Slicing a list

Please see sample code below that uses a Building class you need to define.

Sample Building class usage:
b = Building("A", 3)
print(b.name)    # A
print(b.floors)  # 3

Two Buildings should be considered equal if they have the same name and number of floors.

After writing the Building class, please write a function takes a list of Building instances 
and returns the sum of the number of floors in the last n Buildings in the list, where n is 
specified as an argument to the function. If n is longer than the list of buildings, consider 
all buildings in the list. If n is zero, the function should return 0.

Example usage:
sum_last_n_floors([Building("A", 3), Building("B", 5), Building("C", 2)], 2) -> 7
sum_last_n_floors([Building("A", 3), Building("B", 5), Building("C", 2)], 1) -> 2
sum_last_n_floors([Building("A", 3), Building("B", 5), Building("C", 2)], 3) -> 10
sum_last_n_floors([Building("A", 3), Building("B", 5), Building("C", 2)], 0) -> 0
"""

class Building:

    def  __init__(self, name: str, floors: int):
        self.name = name
        self.floors = floors

    def __eq__(self, other: object) -> bool:
        if not isinstance(other, Building):
            return NotImplemented
        return self.name == other.name and self.floors == other.floors

def sum_last_n_floors(buildings: list[Building], n: int) -> int:
    if n <= 0:
        return 0
    return sum(building.floors for building in buildings[-n:])

if __name__ == "__main__":
    BUILDINGS = [Building("A", 3), Building("B", 5), Building("C", 2)]
    print(sum_last_n_floors(BUILDINGS, 2))  # Output: 7
    print(sum_last_n_floors(BUILDINGS, 1))  # Output: 2
    print(sum_last_n_floors(BUILDINGS, 3))  # Output: 10
    print(sum_last_n_floors(BUILDINGS, 0))  # Output: 0
    print(Building("A", 3) == Building("A", 3))  # Output: True