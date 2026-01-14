from django.db import models

class Master(models.Model):
    master_id = models.CharField(max_length=100)
    name = models.CharField( max_length=50)
    brach = models.CharField(max_length=20)

    def __str__(self):
        return self.name
    