from django.db import models
from django.contrib.auth.models import User


class IngredientCategory(models.Model):
    name = models.CharField(max_length=200, unique=True)

    def __str__(self):
        return self.name


class Ingredient(models.Model):
    name = models.CharField(max_length=250, unique=True)
    category = models.ForeignKey(IngredientCategory)

    def __str__(self):
        return self.name


class Recipe(models.Model):
    owner = models.ForeignKey(User)
    ingredients = models.ManyToManyField(Ingredient, through='RecipeEntry')

    def __str__(self):
        return "\n".join(self.ingredients)


class RecipeEntry(models.Model):
    ingredient = models.ForeignKey(Ingredient)
    recipe = models.ForeignKey(Recipe)
    quantity = models.FloatField()
    unit = models.CharField(max_length=100)

    def __str__(self):
        return self.ingredient + " " + str(self.quantity) + self.unit


class Menu(models.Model):
    name = models.CharField(max_length=100)
    recipes = models.ManyToManyField(Recipe)
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name


class GroceryList(models.Model):
    name = models.CharField(max_length=200)
    owner = models.ForeignKey(User)
    expired = models.BooleanField(default=False)
    createdOn = models.DateTimeField(auto_now_add=True)
    updatedOn = models.DateTimeField(auto_now=True)
    entries = models.ManyToManyField(Ingredient, through='GroceryListEntry')

    def __str__(self):
        return self.name


class GroceryListEntry(models.Model):
    groceryList = models.ForeignKey(GroceryList, on_delete=models.CASCADE)
    ingredient = models.ForeignKey(Ingredient, on_delete=models.CASCADE)
    amount = models.FloatField()
    ingredientUnit = models.CharField(max_length=50)
    checked = models.BooleanField(default=False)
    amount_selected = models.FloatField(default=0)

    def __str(self):
        return str(self.ingredient)

