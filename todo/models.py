from django.db import models

# Create your models here.


class Todo(models.Model):
    title = models.CharField(max_length=120)
    description = models.TextField()
    processing = models.FloatField(default=0.0)
    completed = models.BooleanField(default=False)
    staff = models.TextField(default='')

    def _str_(self):
        return self.title
