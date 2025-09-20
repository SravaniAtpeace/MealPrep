from django.urls import path
from . import views

app_name = 'mealPrep'

urlpatterns = [
    path('Meal/',views.Meal_view, name = "Meal"),
    path('createMealPlan/',views.createMealPlan_view, name = "createMealPlan"),
]