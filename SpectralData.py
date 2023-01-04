from Colors import Colors


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
        return self.__colors.convert_data(self.__array, output_array_shape, slice_before, slice_after)
