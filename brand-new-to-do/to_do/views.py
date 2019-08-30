from rest_framework import generics
from rest_framework.views import APIView
from rest_framework.response import Response
from django.shortcuts import get_object_or_404, render

from rest_framework import status


from .utils import match_state


from .models import Dashboard, Goal, User
from .view_serializers import GoalValidatorSerializer, GoalUpdateValidatorSerializer
from .model_serializers import DashboardSerializer, GoalSerializer, UserSerializer


def home(request):
    return render(request, 'home.html')


class DashboardCreateAPIView(generics.ListCreateAPIView):
    """ Dashboard API"""
    queryset = Dashboard.objects.all()
    serializer_class = DashboardSerializer

    def get_queryset(self):
        """
         This view should return a list of all dashboards
        for the currently authenticated user.
        """
        user = self.request.user.dashboard_set.all()
        return user


class DashboardByIDAPIView(APIView):
    """  This view should return dashboard by id"""
    serializer_class = DashboardSerializer

    def get(self, request, pk):
        dashboard = get_object_or_404(Dashboard.objects.all(), pk=pk)
        serializer = DashboardSerializer(dashboard)
        return Response(serializer.data)


class GoalCreateAPIView(APIView):
    """ Goal Create API with custom method post. Function validate input data,
        transforms is_urgent and is_important fields via match_state function to state value
        and post changed data"""
    view_request_serializer = GoalValidatorSerializer

    def post(self, request):
        serializer = self.view_request_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        request_data = serializer.data
        request_data.update(user=request.user.pk)
        pre_validated_data = match_state(request_data)
        model_serializer = GoalSerializer(data=pre_validated_data)
        model_serializer.is_valid(raise_exception=True)
        created_goal = model_serializer.save()
        return Response(GoalSerializer(instance=created_goal).data, status=status.HTTP_201_CREATED)

    def get(self, request):
        goals = Goal.objects.all()
        serializer = GoalSerializer(goals, many=True)
        return Response(serializer.data)


class GoalUpdateAPIView(APIView):
    """ Goal Update API with partial update"""
    view_request_serializer = GoalUpdateValidatorSerializer

    def put(self, request, pk):
        serializer = self.view_request_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        goal = get_object_or_404(Goal.objects.all(), pk=pk)
        request_data = serializer.data
        serializer = GoalSerializer(instance=goal, data=request_data, partial=True)
        serializer.is_valid(raise_exception=True)
        updated_goal = serializer.save()
        return Response(GoalSerializer(instance=updated_goal).data)


class UserCreateAPIView(generics.ListCreateAPIView):
    """ User API"""
    queryset = User.objects.all()
    serializer_class = UserSerializer
