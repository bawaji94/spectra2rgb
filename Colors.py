from Color import Color
import numpy as np


class Colors(list):
    def __init__(self, no_of_bands, inverse):
        self.__no_of_bands = no_of_bands
        self.__inverse = inverse
        super().__init__(self.__spectra_bands())

    def __spectra_bands(self):
        min_visible_wavelength = 380
        max_visible_wavelength = 750
        red = Color(max_visible_wavelength)
        if self.__no_of_bands == 0:
            raise Exception("No of spectral bands should be > 0")
        elif self.__no_of_bands == 1:
            colors = [red]
        else:
            delta_lambda = (max_visible_wavelength - min_visible_wavelength) / (self.__no_of_bands - 1)
            colors = list(map(
                lambda x: Color(min_visible_wavelength + (x * delta_lambda)),
                range(self.__no_of_bands - 1)
            ))
            colors = colors + [red]
        return colors

    def convert_data(self, spectral_data, output_array_shape, slice_before, slice_after):
        output_array = np.zeros(output_array_shape)
        bands = reversed(range(self.__no_of_bands)) if self.__inverse else range(self.__no_of_bands)
        red_band = slice_before + (0,) + slice_after
        green_band = slice_before + (1,) + slice_after
        blue_band = slice_before + (2,) + slice_after
        for color, band_no in zip(self, bands):
            rgb = color.rgb()
            data_at_spectra = spectral_data[slice_before + (band_no,) + slice_after]
            output_array[red_band] = output_array[red_band] + rgb.red_intensity(data_at_spectra)
            output_array[green_band] = output_array[green_band] + rgb.green_intensity(data_at_spectra)
            output_array[blue_band] = output_array[blue_band] + rgb.blue_intensity(data_at_spectra)
        scaled_to_rgb = (output_array / output_array.max()) * 255
        return (scaled_to_rgb + 0.5).astype(int)
