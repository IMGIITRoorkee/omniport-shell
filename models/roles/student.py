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
        semester_count = self.branch.semester_count
        year_count = self.branch.year_count

        # In case branch semester_count or year_count is None, set semester_per_year to default value i.e. 2
        try:
            semester_per_year = int(semester_count/year_count)
        except TypeError:
            semester_per_year = int(2)

        current_semester = self.current_semester
        self.current_year = int((current_semester + semester_per_year - 1)/semester_per_year)

        super(Student, self).save(*args, **kwargs)

