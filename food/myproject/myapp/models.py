from django.db import models
class canteen(models.Model):
    name= models.CharField(max_length=100)
    description = models.TextField()
    price = models.DecimalField(max_digits=8, decimal_places=2)
    image = models.ImageField(upload_to='list/', blank=True, null=True)

    def __str__(self):
        return self.name

class bakerys(models.Model):
    name= models.CharField(max_length=100)
    description = models.TextField()
    price = models.DecimalField(max_digits=8, decimal_places=2)
    image = models.ImageField(upload_to='items/', blank=True, null=True)

    def __str__(self):
        return self.name

class mess(models.Model):
    name= models.CharField(max_length=100)
    description = models.TextField()
    price = models.DecimalField(max_digits=8, decimal_places=2)
    image = models.ImageField(upload_to='menu/', blank=True, null=True)

    def __str__(self):
        return self.name
