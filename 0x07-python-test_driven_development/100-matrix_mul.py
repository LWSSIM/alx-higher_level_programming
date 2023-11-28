#!/usr/bin/python3
'''safe 2 matrix multiplication
'''


def matrix_mul(m_a, m_b):
    '''Multiply 2 matrices

        Args:
            m_a: 1st
            m_b: 2nd

        Return:
            Resulting matix ->(list of integer/float lists)

        Raises:
            on bad inputs, type, or form of operands
    '''
    for i, operand in zip([m_a, m_b], ['m_a', 'm_b']):
        if not isinstance(i, list):
            raise TypeError('{} must be a list'.format(operand))
        for row in i:
            if not isinstance(row, list):
                raise TypeError("{} must be a list of lists".format(operand))
            if not i or not row or i is None or row is None:
                raise ValueError("{} can't be empty".format(operand))
            for el in row:
                if not isinstance(el, (int, float)):
                    raise TypeError("{} should contain only integers or floats"
                                    .format(operand))
            if len(i[0]) != len(row):
                raise TypeError("each row of {} must be of the same size"
                                .format(operand))

    if len(m_a[0]) != len(m_b):
        raise ValueError("m_a and m_b can't be multiplied")

    row_a, col_a = len(m_a), len(m_a[0])
    row_b, col_b = len(m_b), len(m_b[0])

    m_c = [[0] * col_b for _ in range(row_a)]

    for i in range(row_a):
        for j in range(col_b):
            for k in range(col_a):
                m_c[i][j] += m_a[i][k] * m_b[k][j]
    return m_c
