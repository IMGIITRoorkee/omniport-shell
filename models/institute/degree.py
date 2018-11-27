from django.db import models

from kernel.constants import graduations
from kernel.models import AbstractDegree
from shell.constants import degrees


class Degree(AbstractDegree):
    """
    Make changes to AbstractDegree to suit IIT Roorkee
    """

    code = models.CharField(
        max_length=7,
        unique=True,
        choices=degrees.DEGREES,
    )

    @property
    def name(self):
        """
        Return the name of the degree
        :return: the name of the degree
        """

        return self.get_code_display()

    @property
    def graduation(self):
        """
        Return the graduation level of the degree
        :return: the graduation level of the degree
        """

        degree_tuple = (self.code, self.name,)
        graduation_degrees_map = {
            graduations.GRADUATIONS[3]: degrees.GRADUATE_DEGREES,
            graduations.GRADUATIONS[4]: degrees.POSTGRADUATE_DEGREES,
            graduations.GRADUATIONS[5]: degrees.DOCTORATE_DEGREES,
            graduations.GRADUATIONS[6]: degrees.POSTDOCTORATE_DEGREES,
        }

        for (grad, deg) in graduation_degrees_map:
            if degree_tuple in deg:
                return grad
