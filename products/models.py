from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator
from django.contrib.auth.models import User

from profiles.models import UserProfile


class Category(models.Model):

    class Meta:
        verbose_name_plural = 'Categories'

    name = models.CharField(max_length=254)
    friendly_name = models.CharField(max_length=254, null=True, blank=True)

    def __str__(self):
        return self.name

    def get_friendly_name(self):
        return self.friendly_name


class Product(models.Model):
    category = models.ForeignKey('Category', null=True, blank=True, on_delete=models.SET_NULL)
    sku = models.CharField(max_length=254, null=True, blank=True)
    name = models.CharField(max_length=254)
    colour = models.CharField(max_length=254, null=True, blank=True)
    stock_level = models.IntegerField(null=True, blank=True)
    description = models.TextField()
    price = models.DecimalField(max_digits=6, decimal_places=2)
    rating = models.DecimalField(max_digits=6, decimal_places=2, null=True, blank=True)
    image_url = models.URLField(max_length=1024, null=True, blank=True)
    image = models.ImageField(null=True, blank=True)
    # chain_width = models.CharField(max_length=254, null=True, blank=True)
    # chain_length = models.CharField(max_length=254, null=True, blank=True)


    def __str__(self):
        return self.name

    def is_featured(self):
        return self.featured

    def get_rating(self):
        total = (sum(int(review['star_rating']) for review
                 in self.reviews.values()))

class Review(models.Model):
    """
    The review model class, with fields for
    user and products using a foreign key (unique value)
    A prod_description and review_time
    """

    user = models.ForeignKey(UserProfile, related_name='reviews',
                             on_delete=models.CASCADE)
    product = models.ForeignKey(Product, related_name='reviews',
                                on_delete=models.CASCADE)
    description = models.TextField(max_length=450, null=False,
                                   blank=False)
    star_rating = models.IntegerField(validators=[
            MaxValueValidator(5),
            MinValueValidator(1)
        ])
    review_time = models.DateTimeField(auto_now_add=True)