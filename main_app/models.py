from django.db import models
from django.urls import reverse
from datetime import date
from django.contrib.auth.models import User 

MEALS = (
    ('B', 'Breakfast'),
    ('L', 'Launch'),
    ('D', 'Dinner'),
)

class Toy(models.Model):
    name = models.CharField(max_length=50)
    color = models.CharField(max_length=20)

    def __str__(this):
        return this.name

    def get_absolute_url(this):
        return reverse("toys_detail", kwargs={"pk":this.id})

# Create your models here.
class Cat(models.Model):
    name = models.CharField(max_length=100) # input text box 
    breed = models.CharField(max_length=100) # input text box 
    description = models.TextField(max_length=250) # input Text area 
    age = models.IntegerField() # input number
    image = models.ImageField(upload_to='main_app/static/uploads/', default="")
    toys = models.ManyToManyField(Toy)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(this):
        return this.name 

    def get_absolute_url(this):
        return reverse("detail",kwargs={"cat_id": this.id})

    def is_fed(this):
        return this.feeding_set.filter(date=date.today()).count() >= len(MEALS)

class Feeding(models.Model):
    date = models.DateField()
    meal = models.CharField(max_length=1, choices=MEALS, default=MEALS[0][0])
    cat = models.ForeignKey(Cat, on_delete=models.CASCADE)

    def __str__(this): 
        return f"{this.cat.name} {this.get_meal_display()} on {this.date}"