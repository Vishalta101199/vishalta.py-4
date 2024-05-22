class Circle:
  """Represents a circle with a center and radius."""

  def __init__(self, center_x, center_y, radius):
    """Initializes a Circle object.

    Args:
        center_x: X-coordinate of the circle's center.
        center_y: Y-coordinate of the circle's center.
        radius: The radius of the circle.
    """
    self.__center_x = center_x  # Private member variable
    self.__center_y = center_y  # Private member variable
    self.radius = radius        # Public member variable (accessible outside the class)

  def calculate_area(self):
    """Calculates the area of the circle.

    Returns:
        The area of the circle (pi * radius^2).
    """
    # Accessing private member variables within a method
    return 3.141 * (self.radius ** 2)  # Using a constant value (not ideal)

  def calculate_area_using_pi(self):
    """Calculates the area of the circle using a private member variable for pi.

    Returns:
        The area of the circle (pi * radius^2).
    """
    PI = 3.141  # Private constant within the class (using a single underscore)
    return PI * (self.radius ** 2)

class Rectangle:
  """Represents a rectangle with width and height."""

  def __init__(self, width, height):
    """Initializes a Rectangle object.

    Args:
        width: The width of the rectangle.
        height: The height of the rectangle.
    """
    self.width = width
    self.height = height

  def calculate_area(self):
    """Calculates the area of the rectangle (width * height).

    Returns:
        The area of the rectangle.
    """
    return self.width * self.height

  def calculate_perimeter(self):
    """Calculates the perimeter of the rectangle (2 * width + 2 * height).

    Returns:
        The perimeter of the rectangle.
    """
    return 2 * (self.width + self.height)

# Example usage
rectangle = Rectangle(5, 3)
area = rectangle.calculate_area()
perimeter = rectangle.calculate_perimeter()

print("Area:", area)  # Output: Area: 15
print("Perimeter:", perimeter)  # Output: Perimeter: 16

class TV:
    """Represents a television with attributes and methods for controlling it."""

    def __init__(self, brand, size):
        """Initializes a TV object.

        Args:
            brand: The brand of the TV.
            size: The size of the TV screen (in inches).
        """
        self.brand = brand
        self.size = size
        self.isOn = False
        self.channel = 1
        self.volume = 0

    def turn_on(self):
        """Turns the TV on."""
        self.isOn = True
        print(f"{self.brand} TV is now on (Channel: {self.channel}, Volume: {self.volume})")

    def turn_off(self):
        """Turns the TV off."""
        self.isOn = False
        print(f"{self.brand} TV is now off")

    def set_channel(self, channel):
        """Sets the TV channel to a specific value.

        Args:
            channel: The desired channel number.
        """
        if self.isOn:
            self.channel = channel
            print(f"{self.brand} TV is now on channel {self.channel}")
        else:
            print(f"{self.brand} TV is off. Please turn it on to change channels.")

    def change_channel(self, up=True):
        """Changes the TV channel up or down.

        Args:
            up (bool, optional): If True, increases the channel (default). If False, decreases the channel.
        """
        if self.isOn:
            if up:
                self.channel += 1
            else:
                self.channel -= 1

            # Handle channel wrapping (e.g., going below channel 1)
            if self.channel < 1:
                self.channel = 100  # Adjust for your maximum channel number
            elif self.channel > 100:  # Adjust for your maximum channel number
                self.channel = 1
            print(f"{self.brand} TV is now on channel {self.channel}")
        else:
            print(f"{self.brand} TV is off. Please turn it on to change channels.")

    def adjust_volume(self, amount):
        """Adjusts the TV volume by a certain amount.

        Args:
            amount: The amount to increase or decrease the volume (positive for up, negative for down).
        """
        if self.isOn:
            self.volume += amount
            # Handle volume limits (e.g., not going below 0 or exceeding maximum)
            self.volume = max(0, min(self.volume, 100))  # Adjust for your maximum volume
            print(f"{self.brand} TV volume is now at {self.volume}")
        else:
            print(f"{self.brand} TV is off. Please turn it on to adjust volume.")
