from django.db import models


# Create your models here.

class StripImage(models.Model):
    url = models.ImageField(upload_to="strip_images")
    added_at = models.DateTimeField(auto_now_add=True, editable=False)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.id} {self.url}"
