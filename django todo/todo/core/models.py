from django.db import models

class Todo(models.Model):
    text = models.CharField(max_length=255)
    done = models.BooleanField()
    def __unicode__(self):
        return self.text