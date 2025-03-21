from django.db import models

# Create your models here.

class StatusModel(models.Model):
    name = models.CharField(max_length = 100)
    description = models.TextField()
    create_on = models.DateTimeField(auto_now_add = True)
    last_modified = models.DateTimeField(auto_now = True)

    def __str__(self):
        return self.name
