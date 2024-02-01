from django.db import models
# from django.contrib.auth.models import User
# from django.contrib.auth.models import AbstractUser


class City(models.Model):
    name = models.CharField(max_length=200, null=True)
    image = models.ImageField(upload_to='static/city_image/', null=True)

    def __str__(self):
        return self.name


class Partner(models.Model):
    first_name = models.CharField(max_length=200, null=True)
    last_name = models.CharField(max_length=200, null=True)
    email = models.CharField(max_length=200, null=True)
    city_id = models.ForeignKey(City, related_name='City', null=True, on_delete=models.CASCADE)
    # user_id = models.ForeignKey(CustomUser,on_delete=models.CASCADE)

    def __str__(self):
        return self.first_name + self.last_name


class Product(models.Model):
    partner = models.ForeignKey(Partner, related_name='partner', on_delete=models.CASCADE)
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
        return f"{self.room_type} - {self.id} -{self.partner.first_name}"

# class CustomUser(AbstractUser):
#     # Add your custom fields here
#     # partner_id = models.ForeignKey(Partner)
#     customer = models.BooleanField(default=False, null=True, blank=False)
#     publisher = models.BooleanField(default=False, null=True, blank=False)
#     profile_picture = models.ImageField(upload_to='profile_pics/', null=True, blank=True)


class Orders(models.Model):
    # customer = models.ForeignKey(Partner,on_delete=models.CASCADE)
    name = models.CharField(max_length=200,null=True)
    create_date = models.DateField(null=True, blank=True)

    def __str__(self):
        return self.name


class ProductImage(models.Model):
    partner = models.ForeignKey(Partner, related_name='images', on_delete=models.CASCADE)
    product = models.ForeignKey(Product, related_name='images', on_delete=models.CASCADE)
    image = models.ImageField(upload_to='static/product_images/')

    def __str__(self):
        return f"Image for {self.product.name} - {self.partner.first_name}"




