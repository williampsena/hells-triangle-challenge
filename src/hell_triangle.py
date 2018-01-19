"""Hell Triangle Class
"""
class HellTriangle:

    def max_sum_triangle(self, triangle) -> int:
        """
        Returns the maximum sum of a triangle

        Args:
            triangle: A set of integers

        Returns:
            The maximum sum of triangle
        """

        def __recursive_nodes__(triangle, node_index: int = 0, max_sum: int = 0) -> int:
            node = triangle[0][node_index]

            if len(triangle) == 0:
                return max_sum
            elif len(triangle) == 1:
                return max_sum + node
            else:
                filter_nodes = triangle[1:]

                return max(__recursive_nodes__(filter_nodes, node_index, max_sum + node),
                           __recursive_nodes__(filter_nodes, node_index + 1, max_sum + node))

        return __recursive_nodes__(triangle)
