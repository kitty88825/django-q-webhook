from django.db import models


class Webhook(models.Model):
    name = models.CharField(max_length=255)
    endpoint = models.TextField()

    def __str__(self):
        return self.name
