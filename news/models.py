from django.db import models

from webhooks.models import Webhook


class Reporter(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    email = models.EmailField()

    def __str__(self):
        return "%s %s" % (self.first_name, self.last_name)


class Article(models.Model):
    headline = models.CharField(max_length=100)
    pub_date = models.DateField()
    reporter = models.ForeignKey(Reporter, on_delete=models.CASCADE)
    webhook = models.ForeignKey(Webhook, on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return self.headline

    class Meta:
        ordering = ['headline']
