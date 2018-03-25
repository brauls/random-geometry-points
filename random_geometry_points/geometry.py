"""Random points on geometry surfaces.
"""

import math
from abc import ABCMeta, abstractmethod

class Geometry(metaclass=ABCMeta):
    """Serves as a base class for all geometry types.
    """

    @abstractmethod
    def create_random_points(self, num_points):
        """Creates a list of num_points random points that lie on the geometry surface.
        """
        pass

    @abstractmethod
    def create_random_point_generator(self, num_points):
        """Creates a generator to generate num_points random points that lie on the geometry surface
        """
        pass

    @staticmethod
    def _check_number_of_points_to_create(num_points):
        """Check the number of points to create for a geometry.
        The number of points must be of type int and its value must be
        greater than zero and less than 100000.
        """
        if not isinstance(num_points, int):
            raise TypeError("Inproper type for number of points. Expected int.")
        elif num_points <= 0:
            raise ValueError("""Inproper value for number of points.
            Expected a value greater than zero""")
        elif num_points >= 100000:
            raise ValueError("""Inproper value for number of points.
            Expected a value less than 100000""")

    @staticmethod
    def _check_geometry_parameter(param):
        """Check the type of one geometry parameter to be float or int.
        """
        if isinstance(param, float):
            checked_param = param
        elif isinstance(param, int):
            checked_param = float(param)
        else:
            raise TypeError("Inproper parameter type. Expected float or int.")
        if math.isinf(checked_param) or math.isnan(checked_param):
            raise ValueError("Inproper parameter value. No inf or nan.")
        return checked_param
