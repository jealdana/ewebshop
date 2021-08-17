from django.db import models

class Product(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    photo_url = models.CharField(max_length=100)
    name = models.CharField(max_length=100)
    code = models.CharField(max_length=100,null=True)
    price = models.DecimalField( max_digits=5, decimal_places=2 )
    description = models.TextField()

    def __str__(self):
        return str(self.id) + " - " + self.name + " - " + str(self.code)

    class Meta:
        ordering = ['-id','-name','-code']
        verbose_name = "product"

class Tag(models.Model):
    name = models.CharField(max_length=255)

        