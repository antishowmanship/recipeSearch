from django.db import models

class Recipe(models.Model):
    owner = models.ForeignKey(User)
    ingredients = models.ManyToManyField(Ingredient)


class Ingredient(models.Model):
    name = models.CharField(max_length=250, unique=True)
    category = models.ForeignKey(IngredientCategory)


class IngredientCategory(models.Model):
    name = models.CharField(max_length=200, unique=True)


class GroceryList(models.Model):
    name = models.CharField(max_length=200)
    expired = models.BooleanField(default=False)
    createdOn = models.DateTimeField(auto_now_add=True)
    updatedOn = models.DateTimeField(auto_now_add=True, auto_now=True)


class GroceryListEntry(models.Model):
    groceryList = models.ForeignKey(GroceryList, on_delete=models.CASCADE)
    amount = models.FloatField()
    ingredientUnit = models.ForeignKey(IngredientUnit)
    checked = models.BooleanField(default=False)
    amount_selected = models.FloatField(default=0)


class IngredientUnit(models.Model):
    name = models.CharField(max_length=200)


class IngredientConversion(models.Model):
    start_unit = models.ForeignKey(IngredientUnit)
    result_unit = models.ForeignKey(IngredientUnit)
    multiplier = models.FloatField()


class User(models.Model):
    username = models.CharField(max_length=200, unique=True)
