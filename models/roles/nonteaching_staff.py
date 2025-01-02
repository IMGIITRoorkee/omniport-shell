import swapper

from kernel.models import AbstractNonTeachingStaff

class NonTeachingStaff(AbstractNonTeachingStaff):
    """
    This class implements NonTeachingStaff Role
    """

    class Meta:
        """
        Meta class for NonTeachingStaff
        """

        swappable = swapper.swappable_setting('kernel', 'NonTeachingStaff')
