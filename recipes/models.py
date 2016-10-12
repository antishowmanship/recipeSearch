from django.db import models

class Recipe(models.Model):
    owner = models.ForeignKey(User)
    ingredients = models.ManyToManyField(Ingredient)


class Ingredient(models.Model):
    name = models.CharField(max_length=250, unique=True)


class IngredientCategory(models.Model):
    name = models.CharField(max_length=200, unique=True)


class GroceryList(models.Model):
    name = models.CharField(max_length=200)
    createdOn = models.DateTimeField(auto_now_add=True)
    updatedOn = models.DateTimeField(auto_now_add=True, auto_now=True)


class GroceryListEntry(models.Model):
    ingredientAmount = models.ForeignKey(IngredientAmount)
    groceryList = models.ForeignKey(GroceryList, on_delete=models.CASCADE)


class IngredientUnit(models.Model):
    name = models.CharField(max_length=200)


class IngredientAmount(models.Model):
    unit = models.ForeignKey(IngredientUnit, on_delete=models.CASCADE)
    volume = models.FloatField()


class IngredientConversion(models.Model):
    start_unit = models.ForeignKey(IngredientUnit)
    result_unit = models.ForeignKey(IngredientUnit)
    multiplier = models.FloatField()


class User(models.Model):
    username = models.CharField(max_length=200, unique=True)
