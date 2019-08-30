from django.conf.urls import url

from to_do import views

urlpatterns = [
    url(r'dashboards/', views.DashboardCreateAPIView.as_view(),),
    url(r'dashboard/(?P<pk>\d+)/$', views.DashboardByIDAPIView.as_view(),),
    url(r'goals/', views.GoalCreateAPIView.as_view(),),
    url(r'goal/(?P<pk>\d+)/$', views.GoalUpdateAPIView.as_view(),),
    url(r'users/', views.UserCreateAPIView.as_view(),),
]
