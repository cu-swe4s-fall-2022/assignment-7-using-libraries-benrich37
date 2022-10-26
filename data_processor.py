import numpy as np
import sys

def get_random_matrix(num_rows, num_columns):
    try: 
        matrix = np.random.rand(num_rows, num_columns)
    except TypeError:
        raise TypeError('Arguments must be ints')
    except ValueError:
        raise ValueError('Arguments must be ints >= 1')
    except Exception as e:
        raise e('unexpected error')
    return matrix

def get_file_dimensions(file_name):
	return (0,0)

def write_matrix_to_file(num_rows, num_columns, file_name):
	return None
