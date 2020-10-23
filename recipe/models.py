from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils.translation import gettext_lazy as _

# Create your models here.
class User(AbstractUser):

	def __str__(self):
		return self.username
 
class Ingredients(models.Model):
	ingredient = models.CharField(_("Ingredient"),max_length=1000)
	quantity = models.PositiveIntegerField(_("Quantity"))

class Tags(models.Model): # Incase we implement a search algorithm
	tag = models.CharField(_("Tag"),max_length=250)

class Recipe(models.Model):
	owner = models.ForeignKey(User, on_delete=models.CASCADE)
	food = models.CharField(_("Food"),max_length=250)
	food_desc = models.CharField(_("Description"),max_length=10000)
	ingredients = models.ManyToManyField(Ingredients)
	tags = models.ManyToManyField(Tags)
	time_to_prepare = models.CharField(max_length=250)

class Steps(models.Model):
	step = models.CharField(_("Step"),max_length=10000)
	food = models.ForeignKey(Recipe, on_delete=models.CASCADE)

class FoodImages(models.Model):
	food = models.ForeignKey(Recipe, on_delete=models.CASCADE)
	image = models.ImageField(_("Food Image"))