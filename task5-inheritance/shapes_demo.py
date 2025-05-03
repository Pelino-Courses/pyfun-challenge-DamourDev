from math import sqrt
from shapes import Circle, Rectangle, Triangle

def main():
    """Main function to demonstrate the use of Circle, Rectangle, and Triangle classes."""
    
    object1 = Circle(5)
    object2 = Rectangle(5,7)
    object3 = Triangle(3, 5)

    # Print the area and perimeter of each shape by calling the methods of each object
    print(object1)  
    print(object2)
    print(object3)
    
    object4 = Circle.fromDiameter(12)
    print(object4)  # Print the circle created from diameter

    

main()