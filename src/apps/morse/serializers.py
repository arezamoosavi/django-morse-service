from rest_framework import serializers

class QueueSerializer(serializers.Serializer):
    messege = serializers.CharField(required=True)
    