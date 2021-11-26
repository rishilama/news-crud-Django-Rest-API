from django.db import models

# Create your models here.
class News(models.Model):
    headlines = models.CharField(max_length=255)
    reportedBy = models.CharField(max_length=50)
    addedDate = models.DateTimeField(auto_now_add=True)
    description = models.TextField(null =True)

    def __str__(self):
        return str(self.headlines)