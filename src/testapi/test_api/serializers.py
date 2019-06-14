from rest_framework import serializers


class HelloSerializer(serializers.Serializer):
    def create(self, validated_data):
        pass

    def update(self, instance, validated_data):
        pass

    name = serializers.CharField(max_length=10)
