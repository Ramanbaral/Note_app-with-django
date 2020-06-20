from django.db import models

# Create your models here.
class note(models.Model):
    title=models.CharField(max_length=400)
    body=models.TextField()
    created_date=models.DateField(auto_now_add=True)

    def __str__(self):
        return self.title


    