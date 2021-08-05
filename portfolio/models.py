from django.db import models

# Create your models here.


class Project(models.Model):
    title = models.CharField(max_length=100)  # max pocet znaku
    description = models.CharField(max_length=250)
    image = models.ImageField(upload_to='portfolio/images/')  # kde jsou obrazky ulozene
    url = models.URLField(blank=True)  # neni povinna

    def __str__(self):
        return self.title
