from rest_framework import serializers


class SnippetUpdateSerializer(serializers.Serializer):
    pattern_id = serializers.IntegerField()
    bar = serializers.CharField()
