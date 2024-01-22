from django.db import models
# from django.contrib.auth.models import User
# from django.contrib.auth.models import AbstractUser


class Product(models.Model):
    name = models.CharField(max_length=200,null=True)
    price= models.FloatField()
    CHOICES = [
        ('bed_wise', 'Rate Per Bed'),
        ('room', 'Rate Per Room'),
    ]
    room_type = models.CharField(
        max_length=20,
        choices=CHOICES,
        default='bed_wise',  # Set a default value if needed
    )

    def __str__(self):
        return f"{self.room_type} - {self.id}"


class ProductImage(models.Model):
    product = models.ForeignKey(Product, related_name='images', on_delete=models.CASCADE)
    image = models.ImageField(upload_to='product_images/')

    def __str__(self):
        return f"Image for {self.product.name}"


# class CustomUser(AbstractUser):
#     # Add your custom fields here
#     # partner_id = models.ForeignKey(Partner)
#     customer = models.BooleanField(default=False, null=True, blank=False)
#     publisher = models.BooleanField(default=False, null=True, blank=False)
#     profile_picture = models.ImageField(upload_to='profile_pics/', null=True, blank=True)


class Partner(models.Model):
    first_name = models.CharField(max_length=200, null=True)
    last_name = models.CharField(max_length=200, null=True)
    email = models.CharField(max_length=200, null=True)
    # user_id = models.ForeignKey(CustomUser,on_delete=models.CASCADE)


class Orders(models.Model):
    # customer = models.ForeignKey(Partner,on_delete=models.CASCADE)
    name = models.CharField(max_length=200,null=True)
    create_date = models.DateField(null=True, blank=True)

    def __str__(self):
        return self.name




