import unittest
import spectra2rgb
import numpy as np


class TesSpectra2RGB(unittest.TestCase):
    def test_to_RGB_should_convert_multi_spectra_to_rgb(self):
        array = np.arange(27).reshape(3, 3, 3)

        expected = [[[135, 150, 165],
                     [180, 195, 210],
                     [225, 240, 255]],

                    [[97, 108, 119],
                     [130, 141, 152],
                     [162, 173, 184]],

                    [[0, 3, 6],
                     [10, 13, 16],
                     [19, 23, 26]]]

        rgb = spectra2rgb.to_RGB(array, 0)
        np.testing.assert_array_equal(expected, rgb)

    def test_to_RGB_should_convert_multi_spectra_inversed_to_rgb(self):
        array = np.arange(27).reshape(3, 3, 3)

        expected = [[[135, 150, 165],
                     [180, 195, 210],
                     [225, 240, 255]],

                    [[97, 108, 119],
                     [130, 141, 152],
                     [162, 173, 184]],

                    [[58, 62, 65],
                     [68, 71, 75],
                     [78, 81, 84]]]

        rgb = spectra2rgb.to_RGB(array, 0, inverse=True)
        np.testing.assert_array_equal(expected, rgb)

    def test_to_RGB_should_convert_single_spectra_to_red(self):
        array = np.arange(9).reshape(3, 3, 1)

        expected = [[[0, 0, 0],
                     [32, 0, 0],
                     [64, 0, 0]],

                    [[96, 0, 0],
                     [128, 0, 0],
                     [159, 0, 0]],

                    [[191, 0, 0],
                     [223, 0, 0],
                     [255, 0, 0]]]

        rgb = spectra2rgb.to_RGB(array, 2, inverse=True)
        np.testing.assert_array_equal(expected, rgb)


if __name__ == '__main__':
    unittest.main()
