from django.db import models

class Ingredient(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Meal(models.Model):
    MEAL_TYPES = (
        ('BF', 'Breakfast'),
        ('LN', 'Lunch'),
        ('DN', 'Dinner'),
        ('SN', 'Snack'),
    )
    type = models.CharField(max_length=2, choices=MEAL_TYPES)
    name = models.CharField(max_length=100)
    ingredients = models.ManyToManyField(Ingredient)
    cook_time = models.DurationField()

    def __str__(self):
        return self.name

class Day(models.Model):
    date = models.DateField()
    meals = models.ManyToManyField(Meal)

    def __str__(self):
        return str(self.date)

class MealPlan(models.Model):
    name = models.CharField(max_length=100)
    calories = models.IntegerField()
    protein = models.FloatField()
    carbohydrates = models.FloatField()
    days = models.ManyToManyField(Day)
    favorite_meal = models.ForeignKey(Meal, related_name='favorite_for', on_delete=models.SET_NULL, null=True, blank=True)
    is_vegetarian = models.BooleanField(default=False)
    preferred_ingredients = models.ManyToManyField(Ingredient, related_name='preferred_in_mealplans')
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

class ShoppingList(models.Model):
    mealplan = models.ForeignKey(MealPlan, on_delete=models.CASCADE)
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"Shopping List for {self.mealplan.name}"