import unittest
import spectra2rgb
import numpy as np


class TestCustomer(unittest.TestCase):
    def test_run(self):
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


if __name__ == '__main__':
    unittest.main()
