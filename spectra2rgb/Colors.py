from spectra2rgb import Color
import numpy as np


class Colors(list):
    def __init__(self, no_of_bands, inverse):
        self.__no_of_bands = no_of_bands
        self.__inverse = inverse
        super().__init__(self.__spectra_bands())

    def __spectra_bands(self):
        red = Color(Color.RED)
        if self.__no_of_bands == 0:
            raise Exception("No of spectral bands should be > 0")
        elif self.__no_of_bands == 1:
            colors = [red]
        else:
            delta_lambda = (Color.RED - Color.VIOLET) / (self.__no_of_bands - 1)
            colors = list(map(
                lambda x: Color(Color.VIOLET + (x * delta_lambda)),
                range(self.__no_of_bands - 1)
            ))
            colors = colors + [red]
        return colors

    def __iterate(self):
        bands_range = range(self.__no_of_bands)
        bands = reversed(bands_range) if self.__inverse else bands_range
        return zip(self, bands)

    def rgb_intensities(self, data, _slice):
        output_array = np.zeros(_slice.rgb_shape)
        for color, band_no in self.__iterate():
            data_at_spectra = data[_slice.at(band_no)]
            output_array = output_array + color.rgb.intensities(data_at_spectra, _slice)
        scaled_to_rgb = (output_array / output_array.max()) * 255
        return (scaled_to_rgb + 0.5).astype(int)
