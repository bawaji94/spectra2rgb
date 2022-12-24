import unittest
import spectra2rgb
import numpy as np


class TesSpectra2RGB(unittest.TestCase):
    def test_to_RGB_should_convert_multi_spectra_to_rgb(self):
        array = np.arange(27).reshape(3, 3, 3)

        expected = [[[135, 150, 165],
                     [180, 195, 210],
                     [225, 240, 255]],

                    [[85, 94, 104],
                     [113, 123, 132],
                     [142, 151, 161]],

                    [[0, 4, 7],
                     [11, 14, 18],
                     [22, 25, 29]]]

        rgb = spectra2rgb.to_RGB(array, 0)
        np.testing.assert_array_equal(expected, rgb)

    def test_to_RGB_should_convert_multi_spectra_inversed_to_rgb(self):
        array = np.arange(27).reshape(3, 3, 3)

        expected = [[[135, 150, 165],
                     [180, 195, 210],
                     [225, 240, 255]],

                    [[85, 94, 104],
                     [113, 123, 132],
                     [142, 151, 161]],

                    [[65, 69, 72],
                     [76, 79, 83],
                     [87, 90, 94]]]

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
