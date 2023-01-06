import unittest

from spectra2rgb import Slice


class TestSlice(unittest.TestCase):
    def test_slice_to_give_rgb_array_shape(self):
        original_data_shape = (2000, 40, 200, 200)
        output_data_shape = (2000, 3, 200, 200)

        _slice = Slice(original_data_shape, axis=1)

        self.assertEqual(output_data_shape, _slice.rgb_shape)

    def test_slice_to_give_index_spectra_dimension_at_2(self):
        original_data_shape = (2000, 40, 200, 200)
        actual_index = (slice(None), 2, slice(None), slice(None))

        _slice = Slice(original_data_shape, axis=1)

        self.assertEqual(actual_index, _slice.at(2))

    def test_slice_to_give_index_spectra_dimension_at_3(self):
        original_data_shape = (2000, 40, 200, 200)
        actual_index = (slice(None), 3, slice(None), slice(None))

        _slice = Slice(original_data_shape, axis=1)

        self.assertEqual(actual_index, _slice.at(3))
