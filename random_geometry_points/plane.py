"""Random points on a plane.

This module provides methods to generate an arbitrary number of points lying on a plane.

Examples:
    For examples of the usage of this class see:
    https://github.com/brauls/random-geometry-points/blob/master/test/plane_test.py
"""

import math
import random
from random_geometry_points.geometry import Geometry
from random_geometry_points.validation import check_geometry_parameter, \
  check_vector, check_direction_vector, check_radius
from random_geometry_points.vector_math import normalize_vector, \
  calc_dot_product, calc_perpendicular_vector, rotate_vector, scale_vector, sum_vectors

class Plane(Geometry):
    """Class to generate random points lying on a plane.

    The plane is represented by the following equation:

        d = n_x * x + n_y + y + n_z * z

    In the above equation "d", "n_x", "n_y" and "n_z" are the parameters of the plane.
    "n_x", "n_y" and "n_z" are the elements of the normal vector of the plane while
    "d" is the smallest distance of the plane from the origin.

    In the above equation "x", "y" and "z" represent the coordinates
    of an arbitrary point on the plane.
    """

    def __init__(self, normal_vec, d_origin, ref_point, radius):
        """Plane constructor

        Args:
            normal_vec (tuple (float, float, float)): The normal vector of the plane
            d_origin (float): The smallest distance of the plane from the origin
            ref_point (tuple (float, float, float)): The center point
              for the plane point creation radius
            radius (float): The plane point creation radius
        """
        n_vec = check_direction_vector(normal_vec)
        self.normal_vec = normalize_vector(n_vec)
        self.d_origin = check_geometry_parameter(d_origin)
        self.radius = check_radius(radius)
        self.ref_point = check_vector(ref_point)
        if not math.isclose(calc_dot_product(self.normal_vec, self.ref_point) - self.d_origin,
                            0.0, abs_tol=0.000001):
            raise ValueError("""Invalid reference point. Expected the reference point
              to lie on the plane""")

    @classmethod
    def from_normal_form(cls, normal_vec, position_vec, radius):
        """Factory method to create a plane when having the plane
        parameters in the plane's normal form.

        Args:
            normal_vec (tuple (float, float, float)): The normal vector of the plane
            position_vec (tuple (float, float, float)): An arbitrary point on the plane.
              That point is also used as the center point for the plane point creation radius
            radius (float): The plane point creation radius

        Returns:
            Plane: The plane object
        """
        n_vec = check_direction_vector(normal_vec)
        n0_vec = normalize_vector(n_vec)
        ref_point = check_vector(position_vec)
        d_origin = calc_dot_product(n0_vec, ref_point)
        return cls(normal_vec, d_origin, ref_point, radius)

    @classmethod
    def from_hessian_normal_form(cls, normal_vec, d_origin, radius):
        """Factory method to create a plane when having the plane
        parameters in the plane's hessian normal form.

        Args:
            normal_vec (tuple (float, float, float)): The normal vector of the plane
            d_origin (float): The smallest distance of the plane from the origin
            radius (float): The plane point creation radius

        Returns:
            Plane: The plane object
        """
        n_vec = check_direction_vector(normal_vec)
        n0_vec = normalize_vector(n_vec)
        ref_point = scale_vector(n0_vec, d_origin)
        return cls(normal_vec, d_origin, ref_point, radius)

    def create_random_points(self, num_points):
        """Create a list of num_points random points that lie on the plane.

        Args:
            num_points (int): The number of random points to be created. Maximum value is 99999.

        Returns:
            list (tuple (float, float, float)): A list of randomly generated points.

            The returned list contains num_points tuples.

            Each tuple represents a point lying on the plane.
            The first tuple-value is the x coordinate.
            The second tuple-value is the y coordinate.
            The third tuple-value is the z coordinate.
        """
        super().create_random_points(num_points)
        start_vec = calc_perpendicular_vector(self.normal_vec)
        return [self._create_plane_point(start_vec) for n in range(0, num_points)]

    def create_random_point_generator(self, num_points):
        """Create a generator to generate num_points random points that lie on the plane.

        Args:
            num_points (int): The number of random points to be created. Maximum value is 99999.

        Yields:
            tuple (float, float, float): The next random point.

            Each tuple represents a point lying on the plane.
            The first tuple-value is the x coordinate.
            The second tuple-value is the y coordinate.
            The third tuple-value is the z coordinate.
        """
        _ = [_ for _ in super().create_random_point_generator(num_points)]
        start_vec = calc_perpendicular_vector(self.normal_vec)
        return (self._create_plane_point(start_vec) for n in range(0, num_points))

    def _create_plane_point(self, start_vec):
        """Create a 3D cartesian point using the plane parameters.

        Args:
            start_vec (tuple (float, float, float)): A vector perpendicular to the
              plane's normal vector

        Returns:
            tuple (float, float, float): An arbitrary point on the plane
        """
        angle = random.uniform(0.0, 2.0*math.pi)
        distance = random.uniform(0.0, self.radius)
        random_direction = normalize_vector(rotate_vector(start_vec, self.normal_vec, angle))
        return sum_vectors(self.ref_point, scale_vector(random_direction, distance))
