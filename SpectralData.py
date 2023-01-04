from Colors import Colors
import numpy as np
from Slice import Slice


class SpectralData:
    def __init__(self, array, axis, inverse=False):
        self.__array = array
        no_of_bands = array.shape[axis]
        self.__colors = Colors(no_of_bands, inverse)
        self.__slice = Slice(array.shape, axis)

    def to_rgb(self):
        output_array = np.zeros(self.__slice.output_shape)
        for color, band_no in self.__colors.iterate():
            data_at_spectra = self.__array[self.__slice.at(band_no)]
            rgb = color.rgb
            output_array[self.__slice.at(0)] = output_array[self.__slice.at(0)] + rgb.red_intensity(data_at_spectra)
            output_array[self.__slice.at(1)] = output_array[self.__slice.at(1)] + rgb.green_intensity(data_at_spectra)
            output_array[self.__slice.at(2)] = output_array[self.__slice.at(2)] + rgb.blue_intensity(data_at_spectra)
        scaled_to_rgb = (output_array / output_array.max()) * 255
        return (scaled_to_rgb + 0.5).astype(int)
