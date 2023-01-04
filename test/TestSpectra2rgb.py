import unittest
from SpectralData import SpectralData
import numpy as np


class TesSpectra2RGB(unittest.TestCase):
    def test_to_RGB_should_convert_multi_spectra_to_rgb(self):
        array = np.arange(27).reshape(3, 3, 3)

        expected = [[[135, 150, 165], [180, 195, 210], [225, 240, 255]],
                    [[97, 108, 119], [130, 141, 152], [162, 173, 184]],
                    [[0, 3, 6], [10, 13, 16], [19, 23, 26]]]

        rgb = SpectralData(array, 0).to_rgb()
        np.testing.assert_array_equal(expected, rgb)

    def test_to_RGB_should_convert_multi_spectra_inversed_to_rgb(self):
        array = np.arange(27).reshape(3, 3, 3)

        expected = [[[135, 150, 165], [180, 195, 210], [225, 240, 255]],
                    [[97, 108, 119], [130, 141, 152], [162, 173, 184]],
                    [[58, 62, 65], [68, 71, 75], [78, 81, 84]]]

        rgb = SpectralData(array, 0).to_rgb(inverse=True)
        np.testing.assert_array_equal(expected, rgb)

    def test_to_RGB_should_convert_single_spectra_to_red(self):
        array = np.arange(9).reshape(3, 3, 1)

        expected = [[[0, 0, 0], [32, 0, 0], [64, 0, 0]],
                    [[96, 0, 0], [128, 0, 0], [159, 0, 0]],
                    [[191, 0, 0], [223, 0, 0], [255, 0, 0]]]

        rgb = SpectralData(array, 2).to_rgb(inverse=True)
        np.testing.assert_array_equal(expected, rgb)

    def test_to_RGB_should_not_convert_zero_band_data(self):
        array = np.array([]).reshape(3, 3, 0)
        with self.assertRaises(Exception) as context:
            SpectralData(array, axis=2).to_rgb()
        self.assertEqual("No of spectral bands should be > 0", str(context.exception))

    def test_to_RGB_should_convert_multi_spectra_to_rgb_in_axis_1(self):
        array = np.arange(9 * 7).reshape(3, 7, 3)

        expected = [[[52, 57, 61], [28, 31, 34], [7, 10, 12]],
                    [[149, 154, 158], [100, 103, 107], [58, 61, 63]],
                    [[246, 250, 255], [172, 176, 179], [109, 112, 114]]]

        rgb = SpectralData(array, 1).to_rgb()
        np.testing.assert_array_equal(expected, rgb)


if __name__ == '__main__':
    unittest.main()
