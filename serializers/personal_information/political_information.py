import swapper

from kernel.serializers.personal_information.political_information import (
    PoliticalInformationSerializer as BasePoliticalInformationSerializer
)

PoliticalInformation = swapper.load_model('kernel', 'PoliticalInformation')


class PoliticalInformationSerializer(BasePoliticalInformationSerializer):
    """
    Serializer for PoliticalInformation objects
    """

    # See superclass
    editable_fields = [
        'religion',
        'passport_number',
        'driving_license_number',
        'aadhaar_card_number',
    ]

    class Meta:
        """
        Meta class for PoliticalInformationSerializer
        """

        model = PoliticalInformation
        exclude = [
            'person',
            'id',
            'datetime_created',
            'datetime_modified',
        ]

    def to_representation(self, instance):
        """
        Add reservation category to the representation
        :param instance: the instance being represented
        :return: the dictionary representation of the instance
        """

        representation = super().to_representation(instance)

        reservation_category = instance.get_reservation_category_display()
        representation['reservation_category'] = reservation_category

        return representation
