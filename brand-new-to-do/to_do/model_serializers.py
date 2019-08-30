from rest_framework import serializers


from .models import Dashboard, Goal, User
from .utils import unmatch_state


class GoalSerializer(serializers.ModelSerializer):
    is_urgent = serializers.SerializerMethodField()
    is_important = serializers.SerializerMethodField()

    """ Method get_is_urgent unmatch state and return is_urgent value"""

    def get_is_urgent(self, obj):
        return unmatch_state(obj.state).get('is_urgent')

    """ Method get_is_important unmatch state and return is_important value"""

    def get_is_important(self, obj):
        return unmatch_state(obj.state).get('is_important')

    class Meta:
        model = Goal
        exclude = ('state',)


class DashboardSerializer(serializers.ModelSerializer):
    goals = GoalSerializer(many=True, read_only=True, source='goal_set')

    class Meta:
        model = Dashboard
        fields = '__all__'


class UserSerializer(serializers.ModelSerializer):
    dashboards = serializers.SerializerMethodField()

    """ Method return dashboard Id and Name"""

    def get_dashboards(self, user):
        return user.dashboard_set.all().values('id', 'name')

    class Meta:
        model = User
        fields = ('id', 'username', 'email', 'is_staff', 'date_joined', 'dashboards')
