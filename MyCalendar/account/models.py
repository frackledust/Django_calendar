from django.db import models
# Create your models here.


class Event(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    date = models.DateTimeField('date', auto_now_add=False)

    def __str__(self):
        return self.name


class Category(models.Model):
    name = models.CharField(max_length=100)
    urgency_level = models.IntegerField(default=1)

    def __str__(self):
        return self.name


class Mission(models.Model):
    event = models.ForeignKey(Event, on_delete=models.CASCADE)
    text = models.CharField(max_length=500)
    done = models.BooleanField(default=False)
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return f'{self.id} - {self.event.name} ({self.text})'
