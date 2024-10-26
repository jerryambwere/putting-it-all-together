#!/usr/bin/env python3

class Shoe:
    def __init__(self,brand,size) -> None:
        self.brand=brand
        self.size=size
      

    @property
    def size(self):
        return self._size
    
    @size.setter
    def size(self,size):
        if isinstance(size,int):
            self._size=size
        else:
            print("size must be an integer")
    
    def cobble(self):
        print("Your shoe is as good as new!")

    def condition(self):
         self.condition == "New"
        