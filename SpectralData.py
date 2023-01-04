from Colors import Colors


class SpectralData:
    def __init__(self, array, axis):
        self.__array = array
        self.__axis = axis

    def to_rgb(self, inverse=False):
        no_of_bands = self.__array.shape[self.__axis]
        output_array_shape = self.__array.shape[:self.__axis] + (3,) + self.__array.shape[self.__axis + 1:]
        slice_before = (slice(None),) * len(self.__array.shape[:self.__axis])
        slice_after = (slice(None),) * len(self.__array.shape[self.__axis + 1:])
        colors = Colors(no_of_bands, inverse)
        return colors.convert_data(self.__array, output_array_shape, slice_before, slice_after)
