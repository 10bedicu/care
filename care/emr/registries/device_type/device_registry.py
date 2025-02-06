class DeviceTypeBase:
    def handle_create(self, request_data, obj):
        """
        Handle Creates, the original source request along with the base object created is passed along.
        Update the obj as needed and create any extra metadata needed. This method is called within a transaction
        """
        return obj

    def handle_update(self, request_data, obj):
        """
        Handle Updates, the original source request along with the base object updated is passed along.
        Update the obj as needed and create any extra metadata needed. This method is called within a transaction
        """
        return obj

    def handle_delete(self, obj):
        """
        Handle Deletes, the object to be deleted is passed along.
        Perform validation or any other changes required here
        """
        return obj

    def list(self, obj):
        """
        Return Extra metadata for the given obj for lists, N+1 queries is okay, caching is recommended for performance
        """
        return {}

    def retrieve(self, obj):
        """
        Return Extra metadata for the given obj during retrieves
        """
        return {}


class InternalQuestionnaireRegistry:
    _device_types = {}

    @classmethod
    def register(cls, device_type, device_class) -> None:
        if not issubclass(device_class, DeviceTypeBase):
            raise ValueError("The provided class is not a subclass of DeviceTypeBase")
        cls._device_types[device_type] = device_class
