"""Random points on a sphere.

This module provides methods to generate an arbitrary number of points lying on a sphere.

Examples:
    For examples of the usage of this class see:
    https://github.com/brauls/random-geometry-points/blob/master/test/sphere_test.py
"""

import math
import random
from random_geometry_points.geometry import Geometry
from random_geometry_points.validation import check_geometry_parameter, check_radius

class Sphere(Geometry):
    """Class to generate random points lying on a sphere.

    The sphere is represented by the following equation:

        radius = sqrt( (center_x - x)**2 + (center_y - y)**2 + (center_z - z)**2 )

    In the above equation "radius", "center_x", "center_y" and "center_z"
    are the parameters of the sphere.

    In the above equation "x", "y" and "z" represent the coordinates
    of an arbitrary point on the sphere.
    """

    def __init__(self, center_x, center_y, center_z, radius):
        """Sphere constructor

        Args:
            center_x (float): The x coordinate of the sphere center point
            center_y (float): The y coordinate of the sphere center point
            center_z (float): The z coordinate of the sphere center point
            radius (float): The radius of the sphere
        """
        self.center_x = check_geometry_parameter(center_x)
        self.center_y = check_geometry_parameter(center_y)
        self.center_z = check_geometry_parameter(center_z)
        self.radius = check_radius(radius)

    def create_random_points(self, num_points):
        """Create a list of num_points random points that lie on the sphere.

        Args:
            num_points (int): The number of random points to be created. Maximum value is 99999.

        Returns:
            list (tuple (float, float, float)): A list of randomly generated points.

            The returned list contains num_points tuples.

            Each tuple represents a point lying on the sphere.
            The first tuple-value is the x coordinate.
            The second tuple-value is the y coordinate.
            The third tuple-value is the z coordinate.
        """
        super().create_random_points(num_points)
        polar_coords = [_create_random_azimuth_zenith() for n in range(0, num_points)]
        return [self._create_sphere_point(az_ze[0], az_ze[1]) for az_ze in polar_coords]

    def create_random_point_generator(self, num_points):
        """Create a generator to generate num_points random points that lie on the sphere.

        Args:
            num_points (int): The number of random points to be created.

        Yields:
            tuple (float, float, float): The next random point.

            Each tuple represents a point lying on the sphere.
            The first tuple-value is the x coordinate.
            The second tuple-value is the y coordinate.
            The third tuple-value is the z coordinate.
        """
        _ = [_ for _ in super().create_random_point_generator(num_points)]
        polar_coords = [_create_random_azimuth_zenith() for n in range(0, num_points)]
        return (self._create_sphere_point(az_ze[0], az_ze[1]) for az_ze in polar_coords)

    def _create_sphere_point(self, azimuth, zenith):
        """Create a 3D cartesian point using the sphere parameters and the given angles.

        Args:
            azimuth (float): The azimuth angle (radiant) for which
              the cartesian coordinates shall be calculated
            zenith (float): The zenith angle (radiant) for which
              the cartesian coordinates shall be calculated

        Returns:
            tuple (float, float, float): The cartesian coordinates corresponding to the input angle
        """
        x_from_angle = lambda az, ze: self.radius * math.sin(ze) * math.cos(az) + self.center_x
        y_from_angle = lambda az, ze: self.radius * math.sin(ze) * math.sin(az) + self.center_y
        z_from_angle = lambda az, ze: self.radius * math.cos(ze) + self.center_z
        return (x_from_angle(azimuth, zenith), y_from_angle(azimuth, zenith),
                z_from_angle(azimuth, zenith))

def _create_random_azimuth_zenith():
    """Create random values for azimuth and zenith in radiant.

    Returns:
        tuple (float, float): Random values (radiant) for azimuth and zenith
    """
    azimuth = random.uniform(0.0, 2.0 * math.pi)
    zenith = random.uniform(0.0, math.pi)
    return (azimuth, zenith)
