#!/usr/bin/env python3

class Shoe:
    def __init__(self, brand, size) -> None:
        self.brand = brand
        self.size = size
        self._condition = 'Old'  # Initialize condition attribute

    # Property getter and setter for size
    @property
    def size(self):
        return self._size
    
    @size.setter
    def size(self, size):
        if isinstance(size, int):
            self._size = size
        else:
            print("size must be an integer")
    
    # Method to simulate cobbling (repairing) the shoe
    def cobble(self):
        print("Your shoe is as good as new!")
        self._condition = "New"  # After cobbling, the shoe's condition is 'New'

    # Property for condition to access it
    @property
    def condition(self):
        return self._condition
    
    @condition.setter
    def condition(self, value):
        if value in ["New", "Old"]:
            self._condition = value
        else:
            print("Invalid condition!")

# Test to check the cobble method
shoe = Shoe(brand="Nike", size=42)
print(shoe.condition)  # Should print 'Old'
shoe.cobble()
print(shoe.condition)  # Should print 'New'
