"""Solution for calculating the degrees of vertices in an undirected graph."""


class Solution:
    """Provides methods for analyzing an adjacency matrix."""

    def findDegrees(self, matrix):  # pylint: disable=invalid-name
        """
        Calculate the degree of every vertex.

        Args:
            matrix: Square adjacency matrix representing an undirected graph.

        Returns:
            A list where each element represents the degree of a vertex.
        """
        return [sum(row) for row in matrix]
