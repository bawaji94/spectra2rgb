def wavelength_to_rgb(wavelength, gamma=0.8):
    wavelength = float(wavelength)
    if 380 <= wavelength <= 440:
        attenuation = 0.3 + 0.7 * (wavelength - 380) / (440 - 380)
        red = ((-(wavelength - 440) / (440 - 380)) * attenuation) ** gamma
        green = 0.0
        blue = (1.0 * attenuation) ** gamma
    elif 440 <= wavelength <= 490:
        red = 0.0
        green = ((wavelength - 440) / (490 - 440)) ** gamma
        blue = 1.0
    elif 490 <= wavelength <= 510:
        red = 0.0
        green = 1.0
        blue = (-(wavelength - 510) / (510 - 490)) ** gamma
    elif 510 <= wavelength <= 580:
        red = ((wavelength - 510) / (580 - 510)) ** gamma
        green = 1.0
        blue = 0.0
    elif 580 <= wavelength <= 645:
        red = 1.0
        green = (-(wavelength - 645) / (645 - 580)) ** gamma
        blue = 0.0
    elif 645 <= wavelength <= 750:
        attenuation = 0.3 + 0.7 * (750 - wavelength) / (750 - 645)
        red = (1.0 * attenuation) ** gamma
        green = 0.0
        blue = 0.0
    else:
        red = 0.0
        green = 0.0
        blue = 0.0
    return int(red), int(green), int(blue)


def __spectra_bands_to_RGB(no_of_bands):
    min_visible_wavelength = 380
    max_visible_wavelength = 750
    visible_bands = []
    if no_of_bands <= 0:
        raise Exception("No of spectral bands should be > 0")
    elif no_of_bands == 1:
        visible_bands = [max_visible_wavelength]
    else:
        delta_lambda = (max_visible_wavelength - min_visible_wavelength) / (no_of_bands - 1)
        bands = list(map(lambda x: min_visible_wavelength + (x * delta_lambda), range(no_of_bands - 1)))
        visible_bands = bands + [max_visible_wavelength]
    return list(map(wavelength_to_rgb, visible_bands))


def to_RGB(array, axis):
    no_of_bands = array.shape[axis]
    output_array_shape = array.shape[:axis] + (3,) + array.shape[axis + 1:]
    slice_before = [slice(None)] * len(array.shape[:axis])
    slice_after = [slice(None)] * array.shape[axis + 1:]
    return None
