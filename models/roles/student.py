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
        Override save method of Student class to automatically run validators of a model.
        """

        if kwargs.get('run_validations', False):
            self.full_clean()
        return super().save(*args, **kwargs)
