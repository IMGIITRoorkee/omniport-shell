from django.db import models

from kernel.models.roles import AbstractMaintainer
from shell.constants import maintainer


class Maintainer(AbstractMaintainer):
    """
    Make changes to AbstractMaintainer to suit IIT Roorkee
    """

    role = models.CharField(
        max_length=3,
        choices=maintainer.MAINTAINER_ROLES,
    )
    designation = models.CharField(
        max_length=3,
        choices=maintainer.MAINTAINER_DESIGNATIONS,
    )

    def update_designation(self):
        """
        Update the designation according to the year of the student
        """

        person = self.person
        student = person.student
        year = student.current_year
        self.designation = maintainer.MAINTAINER_DESIGNATIONS[year - 1][0]
        self.save()

    def __str__(self):
        """
        Return the string representation of the model
        :return: the string representation of the model
        """

        person = self.person
        role = self.get_role_display()
        designation = self.get_designation_display()
        post = self.post
        return f'{person} - {role}, {designation} ({post})'
