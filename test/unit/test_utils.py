import unittest
import string
import random
import numpy as np
import os
import sys
mainpath = os.path.join(os.path.dirname(__file__), '../../')
sys.path.append(mainpath)
from data_processor import get_random_matrix as grm
from data_processor import get_file_dimensions as gfd
from data_processor import write_matrix_to_file as wmtf


def bet_0_1(num):
    ret_bool = num >= 0. and num <= 1.
    return ret_bool


class TestUtils(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.ub_matrix_dim = 10
        cls.test_data_fname = '../../iris.data'
        cls.test_data_dim = tuple([149, 5])
        cls.letters = string.ascii_letters + string.punctuation + string.digits
        cls.letters_len = len(cls.letters)
        cls.lb_str_len = 5
        cls.ub_str_len = 10

    def test_get_random_matrix(self):
        expected_shape = tuple([
            random.randint(1, self.ub_matrix_dim),
            random.randint(1, self.ub_matrix_dim)
        ])
        output_matrix = grm(
            expected_shape[0],
            expected_shape[1]
        )
        self.assertEqual(expected_shape, np.shape(output_matrix))
        for i in range(expected_shape[0]):
            for j in range(expected_shape[1]):
                self.assertTrue(bet_0_1(output_matrix[i][j]))

        self.assertRaises(TypeError,
                          grm,
                          np.random.rand() * 10,
                          np.random.rand() * 10)
        self.assertRaises(ValueError,
                          grm,
                          np.random.randint(-10, -1),
                          np.random.randint(-10, -1))

    def test_get_file_dimensions(self):
        badfname = ''
        for i in range(np.random.randint(self.lb_str_len, self.ub_str_len)):
            badfname += self.letters[np.random.randint(0, self.letters_len)]
        self.assertEqual(self.test_data_dim,
                         gfd(self.test_data_fname))
        self.assertEqual(tuple,
                         type(gfd(self.test_data_fname)))
        self.assertRaises(FileNotFoundError,
                          gfd,
                          badfname)

    def test_write_matrix_to_file(self):
        nparray = grm(5, 5)
        self.assertRaises(ValueError, wmtf, 5, 5, 5)


if __name__ == '__main__':
    unittest.main()
