from django.db import models
from django.utils.html import mark_safe
from django.contrib.auth.models import AbstractUser
from django.contrib.auth.models import User
from django.core.validators import MinValueValidator, MaxValueValidator
from django.utils import timezone
# Create your models here.


class Banner(models.Model):
    title = models.CharField(max_length=200)
    img = models.ImageField(upload_to='banner_img/')

    class Meta:
        verbose_name_plural = '1. Banner'

    def __str__(self):
        return self.title


class Nation(models.Model):
    title = models.CharField(max_length=200)
    img = models.ImageField(upload_to='nation_img/')

    class Meta:
        verbose_name_plural = '2.Nation'

    def __str__(self):
        return self.title


class State(models.Model):
    title = models.CharField(max_length=250)
    img = models.ImageField(upload_to='state_img/')

    class Meta:
        verbose_name_plural = '3. State'

    def __str__(self):
        return self.title




class District(models.Model):
    title = models.CharField(max_length=250)
    img = models.ImageField(upload_to='district_img/')
    class Meta:
        verbose_name_plural = '4. District'
    def __str__(self):
        return self.title




class Post(models.Model):
    name = models.CharField(max_length=50)
    img = models.ImageField(upload_to='post/')
    nation = models.ForeignKey(Nation, on_delete=models.CASCADE)
    district = models.ForeignKey(District, on_delete=models.CASCADE)
    state = models.ForeignKey(State, on_delete=models.CASCADE)
    phone = models.IntegerField()
    area=models.CharField(max_length=50)
    detail = models.CharField(max_length=100, default='Your default value')
    location = models.URLField()
    Time=models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)


    def image_tage(self):
        return mark_safe('<img src=%s width="50" height="50" />'%(self.img.url))

    class Meta:
       verbose_name_plural='5. Post'

    def __str__(self):
        return self.name  




class CustomUser(AbstractUser):
    image = models.ImageField(upload_to='user_images/',blank=True)
    age = models.IntegerField(blank=True, null=True)
    phone_number = models.IntegerField(blank=True, null=True)
    nation = models.CharField(max_length=20,blank=True)
    district = models.CharField(max_length=20,blank=True)
    state = models.CharField(max_length=20,blank=True)
    area = models.CharField(max_length=50,blank=True)
    rating = models.IntegerField(default=0)
    time = models.IntegerField(default=0)   # Default value set to 0
    created_at = models.DateTimeField(auto_now_add=True)
    currency = models.IntegerField(default=0)
    is_custumer=models.BooleanField(default=True)

    def __str__(self):
        return self.username
    
class Booking(models.Model):
    user=models.OneToOneField(CustomUser, on_delete=models.CASCADE)
    post=models.ManyToManyField(Post)
    created_at = models.DateTimeField(default=timezone.now) 
    def __str__(self):
        return self.user.username
    


class UserRating(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    rating = models.IntegerField(validators=[MinValueValidator(1), MaxValueValidator(5)])

    def __str__(self):
        return f"{self.user.username}: {self.rating}"

# class Watchlist(models.Model):
#     user = models.OneToOneField(User, on_delete=models.CASCADE)
#     post = models.ManyToManyField(Post)


# class CustomUser(AbstractUser):

#     image = models.ImageField(upload_to='user_images/')
#     phone_number = models.CharField(max_length=20)
#     email=models.EmailField()
#     nation = models.CharField(max_length=20)
#     district = models.CharField(max_length=20)
#     state = models.CharField(max_length=20)
#     area = models.CharField(max_length=50)
#     rating = models.IntegerField(default=0) # Default value set to 0
#     time = models.IntegerField(default=0)   # Default value set to 0
#     created_at = models.DateTimeField(auto_now_add=True)
#     currency = models.IntegerField(default=0)
#     is_custumer=models.BooleanField(default=True)

    # Additional fields and methods can be added as per your requirements

# you're encountering indicates a clash between the reverse accessors for the groups and user_permissions fields of 
# the User model in the auth app and your custom User model in the home app.
# to resolve this issue, you can specify a unique related_name for the groups and user_permissions fields in your custom User model. Here's an example:
  
    # Specify unique related_name for groups field
    # groups = models.ManyToManyField(
    #     'auth.Group',
    #     related_name='home_user_set',
    #     blank=True,
    #     help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.',
    #     verbose_name='groups',
    # )

    # # Specify unique related_name for user_permissions field
    # user_permissions = models.ManyToManyField(
    #     'auth.Permission',
    #     related_name='home_user_set',
    #     blank=True,
    #     help_text='Specific permissions for this user.',
    #     verbose_name='user permissions',
    # )