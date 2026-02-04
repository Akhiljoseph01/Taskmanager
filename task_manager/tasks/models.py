from django.db import models

class task(models.Model):
    title = models.CharField(max_length=50)
    created_at = models.DateTimeField(auto_created=True)
    completed = models.BooleanField(default=False, null=True, blank=True)

    def __str__(self):
        return self.title
