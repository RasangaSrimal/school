from django.db import models


class News(models.Model):
    title = models.CharField(max_length=500, null=True)
    body = models.TextField()
    image = models.ImageField(null=True, blank=True, default='default.jpeg', upload_to='news/')

    def __str__(self):
        return self.title

class Principal(models.Model):
    name = models.CharField(max_length=500, null=True) 
    start_date = models.DateField()
    end_date = models.DateField()

    def __str__(self):
        return self.name

class VicePrincipal(models.Model):
    name = models.CharField(max_length=500, null=True) 
    image = models.ImageField(null=True, blank=True, default='default.jpeg', upload_to='admin/')

    def __str__(self):
        return self.name
