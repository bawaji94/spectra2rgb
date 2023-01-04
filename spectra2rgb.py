import numpy as np
from Color import Color


def __spectra_bands(no_of_bands):
    min_visible_wavelength = 380
    max_visible_wavelength = 750
    red = Color(max_visible_wavelength)
    if no_of_bands == 0:
        raise Exception("No of spectral bands should be > 0")
    elif no_of_bands == 1:
        visible_bands = [red]
    else:
        delta_lambda = (max_visible_wavelength - min_visible_wavelength) / (no_of_bands - 1)
        bands = list(map(lambda x: Color(min_visible_wavelength + (x * delta_lambda)), range(no_of_bands - 1)))
        visible_bands = bands + [red]
    return visible_bands


def to_rgb(array, axis, inverse=False):
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
        wavelength = no_of_bands - band_no - 1 if inverse else band_no
        rgb = wavelengths[wavelength].rgb()
        data_at_spectra = array[slice_before + (band_no,) + slice_after]
        output_array[red_band] = output_array[red_band] + rgb.red_intensity(data_at_spectra)
        output_array[green_band] = output_array[green_band] + rgb.green_intensity(data_at_spectra)
        output_array[blue_band] = output_array[blue_band] + rgb.blue_intensity(data_at_spectra)
    scaled_to_rgb = (output_array / output_array.max()) * 255
    return (scaled_to_rgb + 0.5).astype(int)
