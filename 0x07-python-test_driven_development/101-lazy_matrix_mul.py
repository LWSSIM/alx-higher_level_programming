#!/usr/bin/python3
'''Matrix multiplication using numpy module
'''

import numpy as np

def lazy_matrix_mul(m_a, m_b):
    '''Multiply operand matrices

        Note:
            uses numpy module

        Args:
            m_a: 1st matrix
            m_b: 2nd matrix

        Return:
            new product matrix
    '''
    return np.matmul(m_a, m_b)
