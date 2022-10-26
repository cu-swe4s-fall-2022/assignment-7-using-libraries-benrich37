import numpy as np
import pandas as pd
import sys
import os


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
    try:
        data = pd.read_csv(file_name)
    except TypeError:
        raise TypeError('File name argument must be a string')
    except FileNotFoundError:
        raise FileNotFoundError('File ' + file_name +
                                ' not found in working directory '
                                + str(os.path.dirname(__file__)))
    return np.shape(data)


def write_matrix_to_file(num_rows, num_columns, file_name):
    # Expecting get_random_matrix to handle the bad argument stuff
    matrix = get_random_matrix(num_rows, num_columns)
    matrix = pd.DataFrame(matrix)
    try:
        matrix.to_csv(file_name)
    except ValueError:
        raise ValueError('File name must be a string')
