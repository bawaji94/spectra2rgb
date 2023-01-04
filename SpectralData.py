from Colors import Colors
import numpy as np
from Slice import Slice


class SpectralData:
    def __init__(self, array, axis, inverse=False):
        self.__array = array
        self.__colors = Colors(array.shape[axis], inverse)
        self.__slice = Slice(array.shape, axis)

    def to_rgb(self):
        output_array = np.zeros(self.__slice.output_shape)
        for color, band_no in self.__colors.iterate():
            data_at_spectra = self.__array[self.__slice.at(band_no)]
            output_array = output_array + color.rgb.intensities(data_at_spectra, self.__slice)
        scaled_to_rgb = (output_array / output_array.max()) * 255
        return (scaled_to_rgb + 0.5).astype(int)
