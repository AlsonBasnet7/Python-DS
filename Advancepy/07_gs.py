class Circle:
    def __init__(self, radius):
        self._radius = radius

    @property
    def radius(self):
        return self._radius

    @property
    def area(self):  # Read-only computed property
        return 3.1416 * self._radius * self._radius

c = Circle(5)
print(c.radius)  # 5
print(c.area)  # 78.54

# c.radius = 10  # Raises AttributeError: can't set attribute
# c.area = 20 # Raises AttributeError: can't set attribute