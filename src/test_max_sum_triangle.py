# -*- coding: utf-8 -*-
import unittest
from .hell_triangle import *


class TestDataContext(unittest.TestCase):
    def __test_max_sum_triangle__(self, input_data) -> int:
        hell_triangle = HellTriangle()
        return hell_triangle.max_sum_triangle(input_data)

    """
    Test case scenario (1)
    Parameters: [[6], [3, 5], [9, 7, 1]]
    Result should be 26
    """

    def test_max_sum_triangle_case_1(self):
        result = self.__test_max_sum_triangle__(
            [[6], [3, 5], [9, 7, 1], [4, 6, 8, 4]])

        self.assertTrue(result == 26)

    """
    Test case scenario (2)
    Parameters: [[1], [5, 2], [6, 3, 4], [8, 5, 6, 7], [9, 8, 10, 11, 12]]
    Result should be 29
    """

    def test_max_sum_triangle_case_2(self):
        result = self.__test_max_sum_triangle__(
            [[1], [5, 2], [6, 3, 4], [8, 5, 6, 7], [9, 8, 10, 11, 12]])

        self.assertTrue(result == 29)

    """
    Test case scenario (3)
    Parameters: [[55], [94, 48], [95, 30, 96], [77, 71, 26, 67]]
    Result should be 321
    """

    def test_max_sum_triangle_case_3(self):
        result = self.__test_max_sum_triangle__(
            [[55], [94, 48], [95, 30, 96], [77, 71, 26, 67]])

        self.assertTrue(result == 321)

    """
    Test case scenario (4)
    Parameters: [[5], [1, 3], [4, 7, 10], [0, 3, 2, 1], [10, 13, 11, 5, 15]]
    Result should be 34
    """

    def test_max_sum_triangle_case_4(self):
        result = self.__test_max_sum_triangle__(
            [[5], [1, 3], [4, 7, 10], [0, 3, 2, 1], [10, 13, 11, 5, 15]])

        self.assertTrue(result == 34)


if __name__ == '__main__':
    unittest.main()
