from rest_framework import serializers


class TextSerializer(serializers.Serializer):
    text = serializers.CharField()

class ChannelUser(serializers.Serializer):
    username = serializers.CharField()