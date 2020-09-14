from django.core.validators import RegexValidator
from django.db import models

from kernel.models import AbstractStudent


class Student(AbstractStudent):
    """
    Make changes to AbstractStudent to suit IIT Roorkee
    """

    enrolment_number = models.CharField(
        max_length=8,
        validators=[
            RegexValidator(r'\d{8}'),
        ],
        unique=True,
    )

    def save(self, *args, **kwargs):
        """
        Override .save call to update the year of the student whenever
        the semester is updated
        """
        curent_semester = self.current_semester
        self.current_year = int((curent_semester+1)/2)
        super(Student, self).save(*args, **kwargs)

