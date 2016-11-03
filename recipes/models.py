from django.db import models
from django.contrib.auth.models import User


class IngredientCategory(models.Model):
    name = models.CharField(max_length=200, unique=True)


class Ingredient(models.Model):
    name = models.CharField(max_length=250, unique=True)
    category = models.ForeignKey(IngredientCategory)


class Recipe(models.Model):
    owner = models.ForeignKey(User)
    ingredients = models.ManyToManyField(Ingredient, through=RecipeEntry)


class RecipeEntry(models.Model):
    ingredient = models.ForeignKey(Ingredient)
    recipe = models.ForeignKey(Recipe)
    quantity = models.FloatField()
    unit = models.CharField(max_length=100)


class Menu(models.Model):
    name = models.CharField(max_length=100)
    recipes = models.ManyToManyField(Recipe)
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)


class GroceryList(models.Model):
    name = models.CharField(max_length=200)
    expired = models.BooleanField(default=False)
    createdOn = models.DateTimeField(auto_now_add=True)
    updatedOn = models.DateTimeField(auto_now=True)
    entries = models.ManyToManyField(Ingredient, through=GroceryListEntry)


class GroceryListEntry(models.Model):
    groceryList = models.ForeignKey(GroceryList, on_delete=models.CASCADE)
    ingredient = models.ForeignKey(Ingredient, on_delete=models.CASCADE)
    amount = models.FloatField()
    ingredientUnit = models.CharField(max_length=50)
    checked = models.BooleanField(default=False)
    amount_selected = models.FloatField(default=0)

