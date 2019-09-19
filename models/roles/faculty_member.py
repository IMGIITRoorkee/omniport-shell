from django.core.validators import RegexValidator
from django.db import models

from kernel.models import AbstractFacultyMember
from shell.constants import faculty_designations


class FacultyMember(AbstractFacultyMember):
    """
    Make changes to AbstractFacultyMember to suit IIT Roorkee
    """

    designation = models.CharField(
        max_length=3,
        choices=faculty_designations.FACULTY_DESIGNATIONS,
    )
    employee_id = models.CharField(
        max_length=6,
        validators=[
            RegexValidator(r'\d{6}'),
        ],
        unique=True,
    )

    def __str__(self):
        """
        Return the string representation of the model
        :return: the string representation of the model
        """

        person = self.person
        designation = self.get_designation_display()
        department = self.department
        return f'{person} - {designation}, {department}'
