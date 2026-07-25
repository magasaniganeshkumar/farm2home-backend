from .models import Location


class LocationService:

    @staticmethod
    def create_location(user, validated_data):
        """
        Create a customer location.
        """

        if validated_data.get("is_default"):

            Location.objects.filter(
                user=user,
                is_default=True,
            ).update(is_default=False)

        return Location.objects.create(
            user=user,
            **validated_data,
        )

    @staticmethod
    def update_location(location, validated_data):

        if validated_data.get("is_default"):

            Location.objects.filter(
                user=location.user,
                is_default=True,
            ).exclude(
                id=location.id
            ).update(
                is_default=False
            )

        for field, value in validated_data.items():
            setattr(location, field, value)

        location.save()

        return location