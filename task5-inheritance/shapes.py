import math

class Shape:
    """Base class for all shapes which has common attributes aand methods.

    Attributes:
    name of the shape  which is string: name(str)

    Methods:
    area(): Returns the area of the shape. and will be overrridden by child classes.
    perimeter(): Returns the perimeter of the shape. and will be overrridden by child classes.
    _str__(): Returns a string representation of the shape which is readable well by human.
    """
    def __init__(self, name):
        """
        Initializes the shape with a name.

        Args:
            name (str): The name of the shape.
        """
        if not isinstance(name, str):
            raise TypeError("Name of shape must be a string.")
        self.name = name

    def area(self):
        """
        Returns the area of the shape. This method should be overridden by subclasses.
        """
        raise NotImplementedError("Subclasses must implement this method, area().")
    
    def perimeter(self):
        """
        Returns the perimeter of the shape. This method should be overridden by subclasses.
        """
        raise NotImplementedError("Subclasses must implement this method, perimeter().")
    def __str__(self):
        """
        Returns a string representation of the shape.
        """
        return f"{self.name} with area {self.area()} and perimeter {self.perimeter()}."
    
class Circle(Shape):
    """Circle class which inherits from Shape class.

    Attributes:
    radius of the circle which is float: radius(float)

    Methods:
    area(): Returns the area of the circle.
    perimeter(): Returns the perimeter of the circle.
    _str__(): Returns a string representation of the circle which is readable well by human.
    fromDiameter(): Creates a Circle object from the diameter.

    """

    def __init__(self, radius):
        """
        Initializes the circle with a radius.

        Args:
            radius (float): The radius of the circle.

        Raises:
            ValueError: If radius is negative.
            TypeError: If radius is not a number.
        """
        
        if not isinstance(radius, (int, float)) or radius <= 0:
            raise ValueError("Radius must be greater than zero.")
        super().__init__("Circle")
        self.radius = radius

    def area(self):
        """
        Returns the area of the circle.
        """
        return math.pi * (self.radius ** 2)
    def perimeter(self):
        """
        Returns the perimeter of the circle.
        """
        return 2 * math.pi * self.radius
    def __str__(self):
        """
        Returns a string representation of the circle.
        """
        return f"{self.name} with radius {self.radius} has area {self.area():.2f} and perimeter {self.perimeter():.2f}."
    
    @classmethod
    def fromDiameter(cls, diameter):
        """
        Creates a Circle object from the diameter.

        Args:
            diameter (float): The diameter of the circle.

        Raises:
            ValueError: If diameter is negative.
            TypeError: If diameter is not a number.
        """
        if not isinstance(diameter, (int, float)) or diameter <= 0:
            raise ValueError("Diameter must be greater than zero.")
        radius = diameter / 2
        return cls(radius)
    
class Rectangle(Shape):
    """Rectangle class which inherits from Shape class.

    Attributes:
    length of the rectangle which is float: length(float)
    width of the rectangle which is float: width(float)

    Methods:
    area(): Returns the area of the rectangle.
    perimeter(): Returns the perimeter of the rectangle.
    _str__(): Returns a string representation of the rectangle which is readable well by human.
    """
    def __init__(self, length, width):
        """
        Initializes the rectangle with a length and width.

        Args:
            length (float): The length of the rectangle.
            width (float): The width of the rectangle.

        Raises:
            ValueError: If length or width is negative.
            TypeError: If length or width is not a number.
        """
        if not isinstance(length, (int, float)) or length <= 0:
            raise ValueError("Length must be greater than zero.")
        if not isinstance(width, (int, float)) or width <= 0:
            raise ValueError("Width must be greater than zero.")
        super().__init__("Rectangle")
        self.length = length
        self.width = width

    def area(self):
        """ returns the area of the rectangle."""
        return self.length * self.width
    def perimeter(self):
        """ returns the perimeter of the rectangle."""
        return 2 * (self.length + self.width)
    def __str__(self):
        """returns a string representation of the rectangle."""
        return f"{self.name} with length {self.length} and width {self.width} has area {self.area():.2f} and perimeter {self.perimeter():.2f}."
    
class Triangle(Shape):
    """Triangle class which inherits from Shape class.

    Attributes:
    base of the triangle which is float: base(float)
    height of the triangle which is float: height(float)

    Methods:
    area(): Returns the area of the triangle.
    perimeter(): Returns the perimeter of the triangle.
    _str__(): Returns a string representation of the triangle which is readable well by human.
    """
    def __init__(self, base, height):
        """
        Initializes the triangle with a base , height and hypotenuse .

        Args:
            base (float): The base of the triangle.
            height (float): The height of the triangle.
            hypotenuse (float): The hypotenuse of the triangle.

        Raises:
            ValueError: If base or height  is negative.
            TypeError: If base or height  is not a number.
        """
        if not isinstance(base, (int, float)) or base <= 0:
            raise ValueError("Base must be greater than zero.")
        if not isinstance(height, (int, float)) or height <= 0:
            raise ValueError("Height must be greater than zero.")
        super().__init__("Triangle")
        self.base = base
        self.height = height
         
    def area(self):
        """ returns the area of the triangle."""
        return 0.5 * self.base * self.height   
    def perimeter(self):
        """ returns the perimeter of the triangle."""
        return self.base + self.height + math.sqrt(self.base**2 + self.height**2)
    def __str__(self):
        """returns a string representation of the triangle."""
        return f"{self.name} with base {self.base} and height {self.height} has area {self.area(): .2f} and perimeter {self.perimeter():.2f}."
    



    

