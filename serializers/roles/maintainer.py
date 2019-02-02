import swapper
from rest_framework import serializers

from kernel.serializers.roles.maintainer import (
    MaintainerSerializer as BaseMaintainerSerializer
)


class MaintainerSerializer(BaseMaintainerSerializer):
    """
    Serializer for Maintainer objects
    """

    role = serializers.CharField(
        source='get_role_display',
        read_only=True,
    )
    designation = serializers.CharField(
        source='get_designation_display',
        read_only=True,
    )

    class Meta:
        """
        Meta class for MaintainerSerializer
        """

        model = swapper.load_model('kernel', 'Maintainer')

        fields = [
            'id',
            'person',
            'role',
            'designation',
            'post',
        ]
