from django.db import models

from kernel.models import AbstractResidence
from shell.constants import residences


class Residence(AbstractResidence):
    """
    Make changes to AbstractResidence to suit IIT Roorkee
    """

    code = models.CharField(
        max_length=3,
        unique=True,
        choices=residences.RESIDENCES,
    )

    @property
    def name(self):
        """
        Return the name of the residence
        :return: the name of the residence
        """

        return self.get_code_display()
