import unittest
from unittest import mock
import numpy as np

from spectra2rgb.spectralData import SpectralData


class TesSpectra2RGB(unittest.TestCase):
    @mock.patch("spectra2rgb.spectralData.Slice")
    @mock.patch("spectra2rgb.spectralData.Colors")
    def test_creation_of_spectral_data(self, mock_colors, mock_slice):
        mock_colors.return_value = mock_colors
        mock_slice.return_value = mock_slice
        x = np.random.random((3, 3, 3))

        SpectralData(x, axis=0)

        mock_colors.assert_called_once()
        mock_colors.assert_called_with(3, False)
        mock_slice.assert_called_once()
        mock_slice.assert_called_with((3, 3, 3), 0)

    @mock.patch("spectra2rgb.spectralData.Slice")
    @mock.patch("spectra2rgb.spectralData.Colors")
    def test_conversion_to_rgb_values(self, mock_colors, mock_slice):
        mock_colors.return_value = mock_colors
        mock_slice.return_value = mock_slice
        mock_colors.rgb_intensities.return_value = 'dummy_return_value'
        x = np.random.random((3, 3, 3))

        actual = SpectralData(x, axis=0).to_rgb()

        mock_colors.rgb_intensities.assert_called_once()
        mock_colors.rgb_intensities.assert_called_with(x, mock_slice)
        self.assertEqual(actual, 'dummy_return_value')


if __name__ == '__main__':
    unittest.main()
