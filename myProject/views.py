from django.shortcuts import render
from django.http import HttpResponse

def homepage(request):
    # return HttpResponse("Hello World!, I'm here.")
    return render(request, 'home.html')
    


def createMyMeal(request):
    # return render(request, 'createMeal.html')
    return HttpResponse("Create My Meal")

def myMeals(request):
    # return HttpResponse("My Meals(History)")
    return render(request, 'myMeals.html')
    

def myShopping(request):
    # return render(request, 'myShopping.html')
    return HttpResponse("My Shopping list")

