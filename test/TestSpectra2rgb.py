import unittest
import spectra2rgb
import numpy as np


class TestCustomer(unittest.TestCase):
    def test_run(self):
        array = np.arange(27).reshape(3, 3, 3)
        spectra2rgb.to_RGB(array)


if __name__ == '__main__':
    unittest.main()
