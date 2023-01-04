import numpy as np
from Colors import Colors


def to_rgb(array, axis, inverse=False):
    no_of_bands = array.shape[axis]
    output_array_shape = array.shape[:axis] + (3,) + array.shape[axis + 1:]
    output_array = np.zeros(output_array_shape)
    slice_before = (slice(None),) * len(array.shape[:axis])
    slice_after = (slice(None),) * len(array.shape[axis + 1:])
    red_band = slice_before + (0,) + slice_after
    green_band = slice_before + (1,) + slice_after
    blue_band = slice_before + (2,) + slice_after
    colors = Colors(no_of_bands)
    bands = reversed(range(no_of_bands)) if inverse else range(no_of_bands)
    for color, band_no in zip(colors, bands):
        rgb = color.rgb()
        data_at_spectra = array[slice_before + (band_no,) + slice_after]
        output_array[red_band] = output_array[red_band] + rgb.red_intensity(data_at_spectra)
        output_array[green_band] = output_array[green_band] + rgb.green_intensity(data_at_spectra)
        output_array[blue_band] = output_array[blue_band] + rgb.blue_intensity(data_at_spectra)
    scaled_to_rgb = (output_array / output_array.max()) * 255
    return (scaled_to_rgb + 0.5).astype(int)
