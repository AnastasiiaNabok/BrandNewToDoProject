from rest_framework import serializers


class GoalValidatorSerializer(serializers.Serializer):
    """ View Serializer for Goal create"""

    dashboard = serializers.IntegerField()
    status = serializers.BooleanField(default=False)
    title = serializers.CharField()
    is_urgent = serializers.BooleanField(default=False)
    is_important = serializers.BooleanField(default=False)


class GoalUpdateValidatorSerializer(serializers.Serializer):
    """ View Serializer for Goal update"""

    dashboard = serializers.IntegerField(required=False)
    status = serializers.BooleanField(required=False)
    title = serializers.CharField(required=False)
    is_urgent = serializers.BooleanField(required=False)
    is_important = serializers.BooleanField(required=False)
