import unittest

from spectra2rgb import RGB, Color


class TestColor(unittest.TestCase):
    def test_should_convert_red_wavelength_to_red(self):
        red_wavelength = 645
        color = Color(red_wavelength)

        self.assertEqual(RGB(1, 0, 0), color.rgb)

    def test_should_convert_green_wavelength_to_green(self):
        green_wavelength = 510
        color = Color(green_wavelength)

        self.assertEqual(RGB(0, 1, 0), color.rgb)

    def test_should_convert_blue_wavelength_to_blue(self):
        blue_wavelength = 440
        color = Color(blue_wavelength)

        self.assertEqual(RGB(0, 0, 1), color.rgb)


if __name__ == '__main__':
    unittest.main()
