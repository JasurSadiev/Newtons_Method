from rest_framework import serializers

class NewtonSerializer(serializers.Serializer):
    equation = serializers.CharField(max_length=500)
    first = serializers.IntegerField()
    second = serializers.IntegerField()