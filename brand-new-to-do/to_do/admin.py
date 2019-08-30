from django.contrib import admin

from .models import Dashboard
from .models import Goal


class DashboardAdmin(admin.ModelAdmin):
    list_display = ('name', 'user')
    search_fields = ('name', 'user')

    class Meta:
        verbose_name_plural = 'Dashboards'
        verbose_name = 'Dashboard'
        ordering = '-name'


class GoalAdmin(admin.ModelAdmin):
    list_display = ('user', 'dashboard', 'title', 'state', 'status', 'publish_date')
    search_fields = ('user', 'dashboard', 'title', 'status')

    class Meta:
        verbose_name_plural = 'Goals'
        verbose_name = 'Goal'
        ordering = 'user'


admin.site.register(Dashboard, DashboardAdmin)
admin.site.register(Goal, GoalAdmin)
