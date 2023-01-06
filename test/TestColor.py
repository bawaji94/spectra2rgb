import unittest

from spectra2rgb import RGB, Color


class TestColor(unittest.TestCase):
    def test_should_convert_red_wavelength_to_red(self):
        red_wavelength = 580.71
        color = Color(red_wavelength)

        self.assertEqual(RGB(1, 0, 0), color.rgb)


if __name__ == '__main__':
    unittest.main()
