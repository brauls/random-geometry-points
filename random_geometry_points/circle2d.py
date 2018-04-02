"""Random points on a 2D circle.

This module provides methods to generate an arbitrary number of points lying on a 2D circle.

Examples:
    For examples of the usage of this class see:
    https://github.com/brauls/random-geometry-points/blob/master/test/circle2d_test.py
"""

import math
import random
from random_geometry_points.geometry import Geometry
from random_geometry_points.validation import check_geometry_parameter, check_radius

class Circle2D(Geometry):
    """Class to generate random points lying on a 2D circle.

    The 2D circle is represented by the following equation:

        radius = sqrt( (center_x - x)**2 + (center_y - y)**2 )

    In the above equation "radius", "center_x" and "center_y" are the parameters of the 2D circle.

    In the above equation "x" and "y" represent the coordinates
    of an arbitrary point on the 2D circle.
    """

    def __init__(self, center_x, center_y, radius):
        """Circle2D constructor

        Args:
            center_x (float): The x coordinate of the circle center point
            center_y (float): The y coordinate of the circle center point
            radius (float): The radius of the circle
        """
        self.center_x = check_geometry_parameter(center_x)
        self.center_y = check_geometry_parameter(center_y)
        self.radius = check_radius(radius)

    def create_random_points(self, num_points):
        """Create a list of num_points random points that lie on the 2D circle.

        Args:
            num_points (int): The number of random points to be created.

        Returns:
            list (tuple (float, float)): A list of randomly generated points.

            The returned list contains num_points tuples.

            Each tuple represents a point lying on the 2D circle.
            The first tuple-value is the x coordinate.
            The second tuple-value is the y coordinate.
        """
        super().create_random_points(num_points)
        angles = [random.uniform(0.0, 2.0 * math.pi) for n in range(0, num_points)]
        return [self._create_circle_point(angle) for angle in angles]

    def create_random_point_generator(self, num_points):
        """Create a generator to generate num_points random points that lie on the 2D circle.

        Args:
            num_points (int): The number of random points to be created. Maximum value is 99999.

        Yields:
            tuple (float, float): The next random point.

            Each tuple represents a point lying on the 2D circle.
            The first tuple-value is the x coordinate.
            The second tuple-value is the y coordinate.
        """
        _ = [_ for _ in super().create_random_point_generator(num_points)]
        angles = [random.uniform(0.0, 2.0 * math.pi) for n in range(0, num_points)]
        return (self._create_circle_point(angle) for angle in angles)

    def _create_circle_point(self, angle):
        """Create a 2D cartesian point using the circle parameters and the given angle.

        Args:
            angle (float): The angle (radiant) for which the cartesian coordinates
              shall be calculated

        Returns:
            tuple (float, float): The cartesian coordinates corresponding to the input angle
        """
        x_from_angle = lambda angle: self.radius * math.cos(angle) + self.center_x
        y_from_angle = lambda angle: self.radius * math.sin(angle) + self.center_y
        return (x_from_angle(angle), y_from_angle(angle))
