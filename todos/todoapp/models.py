from django.db import models

class MytodoModel(models.Model):
    task = models.CharField(max_length=50)

    def __str__(self):
        return self.task