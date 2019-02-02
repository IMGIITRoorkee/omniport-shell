KERNEL_FACULTYMEMBER_SERIALIZER = (
    'shell.serializers.roles.'
    'faculty_member.FacultyMemberSerializer'
)
KERNEL_MAINTAINER_SERIALIZER = (
    'shell.serializers.roles.'
    'maintainer.MaintainerSerializer'
)

KERNEL_POLITICALINFORMATION_SERIALIZER = (
    'shell.serializers.personal_information.'
    'political_information.PoliticalInformationSerializer'
)

__all__ = [
    'KERNEL_FACULTYMEMBER_SERIALIZER',
    'KERNEL_MAINTAINER_SERIALIZER',

    'KERNEL_POLITICALINFORMATION_SERIALIZER',
]
