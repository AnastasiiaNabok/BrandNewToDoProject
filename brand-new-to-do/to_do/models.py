from django.db import models
from django.contrib.auth.models import User
from .constant import UI, UNI, NUI, NUNI


class Dashboard(models.Model):
    name = models.CharField(max_length=200, unique=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return '{}  {}'.format(self.name, self.user)


class Goal(models.Model):
    CHOICES = (
        (UI, 'Urgent and Important'),
        (UNI, 'Urgent and Not Important'),
        (NUI, 'Not Urgent and Important'),
        (NUNI, 'Not Urgent and Not Important'),
    )

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    dashboard = models.ForeignKey(Dashboard, on_delete=models.CASCADE)
    publish_date = models.DateTimeField('date published', auto_now_add=True)
    title = models.CharField(max_length=200,)
    state = models.CharField(choices=CHOICES, default=NUNI, max_length=4)
    status = models.BooleanField(default=False)

    class Meta:
        unique_together = ('title', 'dashboard')
