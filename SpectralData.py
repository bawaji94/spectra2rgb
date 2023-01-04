from Colors import Colors
import numpy as np


class SpectralData:
    def __init__(self, array, axis, inverse=False):
        self.__array = array
        self.__axis = axis
        no_of_bands = self.__array.shape[self.__axis]
        self.__colors = Colors(no_of_bands, inverse)

    def to_rgb(self):
        output_array_shape = self.__array.shape[:self.__axis] + (3,) + self.__array.shape[self.__axis + 1:]
        slice_before = (slice(None),) * len(self.__array.shape[:self.__axis])
        slice_after = (slice(None),) * len(self.__array.shape[self.__axis + 1:])
        output_array = np.zeros(output_array_shape)
        red_band = slice_before + (0,) + slice_after
        green_band = slice_before + (1,) + slice_after
        blue_band = slice_before + (2,) + slice_after
        for color, band_no in self.__colors.iterate():
            rgb = color.rgb()
            data_at_spectra = self.__array[slice_before + (band_no,) + slice_after]
            output_array[red_band] = output_array[red_band] + rgb.red_intensity(data_at_spectra)
            output_array[green_band] = output_array[green_band] + rgb.green_intensity(data_at_spectra)
            output_array[blue_band] = output_array[blue_band] + rgb.blue_intensity(data_at_spectra)
        scaled_to_rgb = (output_array / output_array.max()) * 255
        return (scaled_to_rgb + 0.5).astype(int)
