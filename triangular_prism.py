
import copy
import math
import numpy
import itertools

import utilities


class TriangularPrism(object):

    def __init__(self, color='b', long_side=1, axis_length_factor=1.5):
        self.color = color
        self.axis_length_factor = axis_length_factor
        self._setup_3D_object_data()
        self.long_side = long_side

    @property
    def data(self):
        return(copy.deepcopy(self.object_data))

    @data.setter
    def data(self, value):
        self.object_data = value

    @property
    def color(self):
        return(self.object_color)

    @color.setter
    def color(self, value):
        self.object_color = value

    @property
    def axis_length(self):
        return(self.axis_length_factor * self.long_side)

    def _setup_3D_object_data(self):
        # This is are R^3 coordinates of
        # each corner in the 3D object
        self.object_data = [
            [[-1, -1, -1], [1, -1, -1]],
            [[-1, -1, -1], [0,  1, -1]],
            [[-1, -1, -1], [0,  0,  1]],
            [[ 1, -1, -1], [0,  1, -1]],
            [[ 1, -1, -1], [0,  0,  1]],
            [[ 0,  1, -1], [0,  0,  1]]
        ]
