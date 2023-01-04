import numpy as np


class RGB:
    def __init__(self, red, green, blue):
        self.__blue = blue
        self.__green = green
        self.__red = red

    def intensities(self, data, _slice):
        rgb_intensities = np.zeros(_slice.output_shape)
        rgb_intensities[_slice.at(0)] = self.__red * data
        rgb_intensities[_slice.at(1)] = self.__green * data
        rgb_intensities[_slice.at(2)] = self.__blue * data
        return rgb_intensities
