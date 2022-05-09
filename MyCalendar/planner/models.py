from django.db import models

# Create your models here.
from user.models import MyUser


class Planner(models.Model):
    planner_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255)
    owner = models.ForeignKey(MyUser, on_delete=models.CASCADE)
    visible_for = models.ManyToManyField(MyUser, related_name="visible_for")
    editable_by = models.ManyToManyField(MyUser, related_name="editable_by")

    def __str__(self):
        return self.name


class Plan(models.Model):

    plan_id = models.AutoField(primary_key=True)
    planner = models.ForeignKey(Planner, on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    start_date = models.DateTimeField()
    end_date = models.DateTimeField(null=True, blank=True)

    def __str__(self):
        return self.name