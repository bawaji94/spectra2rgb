from Colors import Colors
import numpy as np
from Slice import Slice


class SpectralData:
    def __init__(self, array, axis, inverse=False):
        self.__array = array
        self.__axis = axis
        no_of_bands = self.__array.shape[self.__axis]
        self.__colors = Colors(no_of_bands, inverse)

    def to_rgb(self):
        s = Slice(self.__array.shape, self.__axis)
        output_array = np.zeros(s.output_shape)
        for color, band_no in self.__colors.iterate():
            data_at_spectra = self.__array[s.at(band_no)]
            output_array[s.at(0)] = output_array[s.at(0)] + color.rgb.red_intensity(data_at_spectra)
            output_array[s.at(1)] = output_array[s.at(1)] + color.rgb.green_intensity(data_at_spectra)
            output_array[s.at(2)] = output_array[s.at(2)] + color.rgb.blue_intensity(data_at_spectra)
        scaled_to_rgb = (output_array / output_array.max()) * 255
        return (scaled_to_rgb + 0.5).astype(int)
