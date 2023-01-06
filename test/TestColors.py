import unittest
import numpy as np
from spectra2rgb import Colors, Color, Slice


class TestColors(unittest.TestCase):
    def test_list_of_colors_given_no_of_bands_is_2(self):
        self.assertEqual(Colors(2, False), [Color(Color.VIOLET), Color(Color.RED)])

    def test_list_of_colors_given_no_of_bands_is_3(self):
        expected_colors = [Color(Color.VIOLET), Color(565), Color(Color.RED)]
        self.assertEqual(Colors(3, False), expected_colors)

    def test_list_of_colors_given_no_of_bands_is_5(self):
        expected_colors = [Color(Color.VIOLET),
                           Color(472.5),
                           Color(565),
                           Color(657.5),
                           Color(Color.RED)]
        self.assertEqual(Colors(5, False), expected_colors)

    def test_list_of_colors_given_no_of_bands_is_1(self):
        self.assertEqual(Colors(1, False), [Color(Color.RED)])

    def test_list_of_colors_given_no_of_bands_is_0(self):
        with self.assertRaises(Exception) as context:
            Colors(0, False)
        self.assertEqual("No of spectral bands should be > 0", str(context.exception))

    def test_convert_multi_spectra_to_rgb_array_when_not_inversed(self):
        array = np.arange(27).reshape(3, 3, 3)
        expected = [[[135, 150, 165], [180, 195, 210], [225, 240, 255]],
                    [[97, 108, 119], [130, 141, 152], [162, 173, 184]],
                    [[0, 3, 6], [10, 13, 16], [19, 23, 26]]]

        colors = Colors(3, False)
        rgb_intensities = colors.rgb_intensities(array, Slice(array.shape, axis=0))

        np.testing.assert_array_equal(expected, rgb_intensities)
        self.assertEqual(np.int64, rgb_intensities.dtype)

    def test_convert_multi_spectra_to_rgb_array_when_inversed(self):
        array = np.arange(27).reshape(3, 3, 3)
        expected = [[[135, 150, 165], [180, 195, 210], [225, 240, 255]],
                    [[97, 108, 119], [130, 141, 152], [162, 173, 184]],
                    [[58, 62, 65], [68, 71, 75], [78, 81, 84]]]

        colors = Colors(3, True)
        rgb_intensities = colors.rgb_intensities(array, Slice(array.shape, axis=0))

        np.testing.assert_array_equal(expected, rgb_intensities)
        self.assertEqual(np.int64, rgb_intensities.dtype)
