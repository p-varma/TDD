class Celsius:
    def __init__(self, temperature=0):
            self.temperature = temperature

    def to_fahrenheit(self):
        return (self.get_temperature() * 1.8) + 32

    # getter method
    def temperature(self):
        print("Getting Value")
        return self._temperature

    # setter method
    def set_temperature(self, value):
        print("Setting Value")
        if value < -273.15:
            raise ValueError("Temperature below -273.15 is not possible.")
        self._temperature = value

    temperature = property(get_temperature,set_temperature)


# Create a new object, set_temperature() internally called by __init__
human = Celsius(37)

# Get the temperature attribute via a getter
print(human.get_temperature())


human.temperature = -300


print(human.get_temperature())