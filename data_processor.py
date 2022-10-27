import numpy as np
import pandas as pd
import sys
import os


def get_random_matrix(num_rows, num_columns):

    """ Returns an NxM matrix of random floats within [0, 1]

    Perameters:
    ----------
           num_rows: Number of rows (N) in return matrix
                     ASSUMPTIONS: Must be a positive integer
        num_columns: Number of columns (M) in return matrix
                     ASSUMPTIONS: Must be a positive integer
    Returns:
    --------
             matrix: NxM np.ndarray containing random floats
                       between 0 and 1
    """

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

    """ Returns the dimensions of provided csv file

    Perameters:
    ----------
          file_name: String of file name to examine
                     ASSUMPTIONS: Must be a string
                                  File must exist in working directory
                                  File must be interpretable as a csv
    Returns:
    --------
                dim: length 2 tuple with dimensions of provided file
    """

    try:
        data = pd.read_csv(file_name)
    except TypeError:
        raise TypeError('File name argument must be a string')
    except FileNotFoundError:
        raise FileNotFoundError('File ' + file_name +
                                ' not found in working directory ' +
                                str(os.path.dirname(__file__)))
    dim = np.shape(data)
    return dim


def write_matrix_to_file(num_rows, num_columns, file_name):

    """ Writes a random matrix to a csv file

    Perameters:
    ----------
             num_rows: Passed as num_rows to get_random_matrix function
          num_columns: Passed as num_columns to get_random_matrix function
            file_name: String to save matrix as
                       ASSUMPTIONS: Must be a string
                                    Must not contain a filtype suffix
    Returns:
    --------
    None

    """

    # Expecting get_random_matrix to handle the bad argument stuff
    matrix = get_random_matrix(num_rows, num_columns)
    matrix = pd.DataFrame(matrix)
    try:
        matrix.to_csv(file_name)
    except ValueError:
        raise ValueError('File name must be a string')
