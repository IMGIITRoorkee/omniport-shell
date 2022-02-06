import swapper
from rest_framework import serializers

from omniport.utils import switcher
from kernel.serializers.roles.joint_faculty import (
    JointFacultyMembershipSerializer as BaseJointFacultyMembershipSerializer,
    JointFacultySerializer as BaseJointFacultySerializer
)


class JointFacultyMembershipSerializer(BaseJointFacultyMembershipSerializer):
    """
    Serializer for JointFacultyMembership objects
    """

    designation = serializers.CharField(
        source='get_designation_display',
        read_only=True,
    )

    class Meta:
        """
        Meta class for JointFacultyMembershipSerializer
        """

        model = swapper.load_model('kernel', 'JointFacultyMembership')

        fields = [
            'department',
            'designation',
        ]

class JointFacultySerializer(BaseJointFacultySerializer):
    """
    Serializer for JointFaculty objects
    """

    memberships = switcher.load_serializer('kernel', 'JointFacultyMembership')(many=True)

    class Meta:
        """
        Meta class for JointFacultySerializer
        """

        model = swapper.load_model('kernel', 'JointFaculty')

        fields = [
            'id',
            'person',
            'memberships',
            'employee_id',
        ]
