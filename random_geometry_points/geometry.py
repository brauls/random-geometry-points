"""Random points on geometry surfaces.
"""

from abc import ABCMeta, abstractmethod
from random_geometry_points.validation import check_number_of_random_points

class Geometry(metaclass=ABCMeta):
    """Base class for all geometry types.
    """

    @abstractmethod
    def create_random_points(self, num_points):
        """Create a list of num_points random points that lie on the geometry surface.
        """
        check_number_of_random_points(num_points)
        return []

    @abstractmethod
    def create_random_point_generator(self, num_points):
        """Create a generator to generate num_points random points that lie on the geometry surface
        """
        check_number_of_random_points(num_points)
        yield from ()
