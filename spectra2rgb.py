import numpy as np
from RGB import RGB


def __wavelength_to_rgb(wavelength, gamma=0.8):
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
    return RGB(red, green, blue)


def __spectra_bands(no_of_bands):
    min_visible_wavelength = 380
    max_visible_wavelength = 750
    if no_of_bands <= 0:
        raise Exception("No of spectral bands should be > 0")
    elif no_of_bands == 1:
        visible_bands = [max_visible_wavelength]
    else:
        delta_lambda = (max_visible_wavelength - min_visible_wavelength) / (no_of_bands - 1)
        bands = list(map(lambda x: min_visible_wavelength + (x * delta_lambda), range(no_of_bands - 1)))
        visible_bands = bands + [max_visible_wavelength]
    return visible_bands


def to_RGB(array, axis):
    no_of_bands = array.shape[axis]
    output_array_shape = array.shape[:axis] + (3,) + array.shape[axis + 1:]
    output_array = np.zeros(output_array_shape)
    slice_before = (slice(None),) * len(array.shape[:axis])
    slice_after = (slice(None),) * len(array.shape[axis + 1:])
    red_band = slice_before + (0,) + slice_after
    green_band = slice_before + (1,) + slice_after
    blue_band = slice_before + (2,) + slice_after
    wavelengths = __spectra_bands(no_of_bands)
    for band_no in range(no_of_bands):
        rgb = __wavelength_to_rgb(wavelengths[band_no])
        data_at_spectra = array[slice_before + (band_no,) + slice_after]
        output_array[red_band] = output_array[red_band] + rgb.red_intensity(data_at_spectra)
        output_array[green_band] = output_array[green_band] + rgb.green_intensity(data_at_spectra)
        output_array[blue_band] = output_array[blue_band] + rgb.blue_intensity(data_at_spectra)
    scaled_to_rgb = (output_array / output_array.max()) * 255
    return (scaled_to_rgb + 0.5).astype(int)
