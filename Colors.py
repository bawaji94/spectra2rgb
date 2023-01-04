from Color import Color


class Colors(list):
    def __init__(self, no_of_bands):
        self.__no_of_bands = no_of_bands
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
