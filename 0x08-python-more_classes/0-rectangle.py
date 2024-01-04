#!/usr/bin/python3

class Rectangle:

    def __init__(self, height, width):
        self.height = height
        self.width = width

    def area(self):
        return self.height * self.width
        
    def perimeter(self):
        return (self.height + self.width) * 2

    def is_sqaure(self):
       return self.height == self.width

