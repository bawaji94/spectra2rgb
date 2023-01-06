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

    def test_RGB_is_not_equal_to_1(self):
        self.assertNotEqual(RGB(0, 0, 0), 1)

    def test_RGB_serialization(self):
        self.assertEqual('RGB(R=0.5, G=1.0, B=2.5)', str(RGB(0.5, 1.0, 2.5)))


if __name__ == '__main__':
    unittest.main()
