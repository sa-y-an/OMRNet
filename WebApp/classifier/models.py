from django.db import models


class Image(models.Model):
    title = models.CharField(max_length=200)
    image = models.ImageField(upload_to='images')
    ans_class = models.CharField(max_length= 15, blank=True)
    score = models.TextField(blank=True)


    def __str__(self):
        return self.title
