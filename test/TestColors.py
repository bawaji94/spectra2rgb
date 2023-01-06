import unittest
from spectra2rgb import Colors, Color


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
