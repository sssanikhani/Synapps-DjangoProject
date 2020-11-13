from rest_framework.exceptions import NotAcceptable


class BaseSerializer:
    @classmethod
    def get_valid_data(cls, serializer, data):
        serializer = serializer(data=data)
        valid = serializer.is_valid()
        if not valid:
            raise NotAcceptable(serializer.errors)
        validated_data = serializer.validated_data
        return validated_data
