from Colors import Colors


def to_rgb(array, axis, inverse=False):
    no_of_bands = array.shape[axis]
    output_array_shape = array.shape[:axis] + (3,) + array.shape[axis + 1:]
    slice_before = (slice(None),) * len(array.shape[:axis])
    slice_after = (slice(None),) * len(array.shape[axis + 1:])
    colors = Colors(no_of_bands, inverse)
    return colors.convert_data(array, output_array_shape, slice_before, slice_after)
