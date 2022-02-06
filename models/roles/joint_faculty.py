from django.core.validators import RegexValidator
from django.db import models

from kernel.models import AbstractJointFaculty, AbstractJointFacultyMembership
from shell.constants import faculty_designations


class JointFacultyMembership(AbstractJointFacultyMembership):
    """
    Make changes to JointFacultyMembership to suit IIT Roorkee
    """

    designation = models.CharField(
        max_length=3,
        choices=faculty_designations.FACULTY_DESIGNATIONS,
    )

    def __str__(self):
        """
        Return the string representation of the model
        :return: the string representation of the model
        """

        designation = self.get_designation_display()
        department = self.department
        return f'{designation}, {department}'


class JointFaculty(AbstractJointFaculty):
    """
    Make changes to JointFaculty to suit IIT Roorkee
    """

    employee_id = models.CharField(
        max_length=6,
        validators=[
            RegexValidator(r'\d{6}'),
        ],
        unique=True,
    )
