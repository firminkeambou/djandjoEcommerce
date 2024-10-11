from django.db import models

# Create your models here.
class Products(models.Model):
    # by  default, when you query this model, it will returns an "object", if you want a different behavior, for example the name of the movie, Do as follows:
    def __str__(self):
        return self.title
    title = models.CharField(max_length=200)
    price = models.FloatField()
    discount_price = models.FloatField()
    category = models.CharField(max_length=200)
    description = models.TextField()
    # we are having a link for the image field because most of the ecommerce website have their images in a different server
    image = models.CharField(max_length=500)
    