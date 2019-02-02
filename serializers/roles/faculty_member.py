import swapper
from rest_framework import serializers

from kernel.serializers.roles.faculty_member import (
    FacultyMemberSerializer as BaseFacultyMemberSerializer
)


class FacultyMemberSerializer(BaseFacultyMemberSerializer):
    """
    Serializer for FacultyMember objects
    """

    designation = serializers.CharField(
        source='get_designation_display',
        read_only=True,
    )

    class Meta:
        """
        Meta class for FacultyMemberSerializer
        """

        model = swapper.load_model('kernel', 'FacultyMember')

        fields = [
            'id',
            'person',
            'department',
            'designation',
        ]
