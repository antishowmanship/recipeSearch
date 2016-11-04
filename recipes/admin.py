from django.contrib import admin

from .models import *

# Register your models here.
admin.site.register(IngredientCategory)
admin.site.register(Ingredient)
admin.site.register(Recipe)
admin.site.register(RecipeEntry)
admin.site.register(Menu)
admin.site.register(GroceryList)
admin.site.register(GroceryListEntry)
