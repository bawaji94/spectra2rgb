class RGB:
    def __init__(self, red, green, blue):
        self.__blue = blue
        self.__green = green
        self.__red = red

    def red_intensity(self, intensity):
        return self.__red * intensity

    def green_intensity(self, intensity):
        return self.__green * intensity

    def blue_intensity(self, intensity):
        return self.__blue * intensity
