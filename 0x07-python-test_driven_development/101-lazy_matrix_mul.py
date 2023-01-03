#!/usr/bin/python3.5
"""Module composed by a function that multiplies 2 matrices"""


import numpy as np


def lazy_matrix_mul(m_a, m_b):
    """ Multiply 2 matrices

    Description:
        This function multiplies two matrices using numpy

    Args:
        m_a (matrix) b: the first args
        m_b (matrix a): the second args

    Returns:
        result of the multiplication

    """

    return (np.matmul(m_a, m_b))
