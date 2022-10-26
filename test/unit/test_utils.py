import unittest
import string
import random
import numpy as np
import os
import sys

mainpath = os.path.join(os.path.dirname(__file__), '../../')
sys.path.append(mainpath)
import data_processor

def bet_0_1(num):
    ret_bool = num >= 0. and num <= 1.
    return ret_bool

class TestUtils(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        ub_matrix_dim = 10
        
    @classmethod
    def setUp(cls):
        # TODO
        
    @classmethod
    def tearDown(cls):
        # TODO
        
    def test_get_random_matrix(self):
        expected_shape = tuple([
            random.randint(0, cls.ub_matrix_dim),
            random.randint(0, cls.ub_matrix_dim)
        ])
        output_matrix = data_processor.get_random_matrix(
            expected_shape[0],
            expected_shape[1]
        )
        self.assertEqual(expected_shape,
                        np.shape(output_matrix)
                        )
        for i in range(expected_shape[0]):
            for j in range(expected_shape[1]):
                self.assertTrue(bet_0_1(output_matrix[i][j]))
        
    def test_get_file_dimensions(self):
        # TODO
        
    def test_write_matrix_to_file(self):
        # TODO
        
if __name__ == '__main__':
    unittest.main()
