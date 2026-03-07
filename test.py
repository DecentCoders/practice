class Circle:
    PI = 3.1416  # Class constant (shared by all Circle instances)
    
    def __init__(self, radius):
        self.radius = radius

    # Calculate area (πr²)
    def area(self):
        return self.PI * (self.radius **2)

    # Calculate circumference (2πr)
    def circumference(self):
        return 2 * self.PI * self.radius

# Test
circle1 = Circle(5)
print(f"Circle Radius: {circle1.radius}")
print(f"Area: {circle1.area():.2f}")  # Output: 78.54
print(f"Circumference: {circle1.circumference():.2f}")  # Output: 31.42