import unittest
import numpy as np

from spectra2rgb import Slice, RGB


class TesSpectra2RGB(unittest.TestCase):
    def test_to_calculate_intensities_when_color_is_white(self):
        array = np.ones((3, 3, 3))
        _slice = Slice(array.shape, 2)
        expected = np.ones((3, 3, 3))

        actual = RGB(1.0, 1.0, 1.0).intensities(array[:, :, 1], _slice)
        np.testing.assert_array_equal(expected, actual)

    def test_to_calculate_intensities_when_color_is_red(self):
        array = np.ones((3, 3, 3))
        _slice = Slice(array.shape, 2)
        expected = np.zeros((3, 3, 3))
        expected[:, :, 0] = 1

        actual = RGB(1.0, 0, 0).intensities(array[:, :, 1], _slice)
        np.testing.assert_array_equal(expected, actual)

    def test_to_calculate_intensities_when_color_is_green(self):
        array = np.ones((3, 3, 3))
        _slice = Slice(array.shape, 2)
        expected = np.zeros((3, 3, 3))
        expected[:, :, 1] = 1

        actual = RGB(0, 1, 0).intensities(array[:, :, 1], _slice)
        np.testing.assert_array_equal(expected, actual)

    def test_to_calculate_intensities_when_color_is_blue(self):
        array = np.ones((3, 3, 3))
        _slice = Slice(array.shape, 2)
        expected = np.zeros((3, 3, 3))
        expected[:, :, 2] = 1

        actual = RGB(0, 0, 1).intensities(array[:, :, 1], _slice)
        np.testing.assert_array_equal(expected, actual)


if __name__ == '__main__':
    unittest.main()
