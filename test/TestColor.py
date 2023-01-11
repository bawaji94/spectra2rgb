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

    def test_should_convert_orange_wavelength_to_orange(self):
        blue_wavelength = 580
        color = Color(blue_wavelength)

        self.assertEqual(RGB(1, 1, 0), color.rgb)

    def test_red_and_violet_are_not_same_color(self):
        self.assertNotEqual(Color(Color.RED), Color(Color.VIOLET))

    def test_red_color_is_not_equal_to_1(self):
        self.assertNotEqual(Color(Color.RED), 1)

    def test_render_Color_with_wavelength(self):
        self.assertEqual(str(Color(Color.RED)), 'Color(λ = 750nm)')

    def test_should_convert_red_wavelength_to_red_hexcode(self):
        red_wavelength = 645
        color = Color(red_wavelength)

        self.assertEqual('#FF0000', color.hexcode)


if __name__ == '__main__':
    unittest.main()
