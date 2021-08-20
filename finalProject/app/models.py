from django.db import models

# Create your models here.


class Data(models.Model):
    objects = None
    Row_ID = models.IntegerField(default=False)
    Symboling = models.IntegerField(default=False)
    Normalized_Losses = models.IntegerField(default=False)
    Make = models.CharField(max_length=200)
    Num_of_Doors = models.CharField(max_length=200)
    Body_Style = models.CharField(max_length=200)
    Drive_Wheels = models.CharField(max_length=200)
    Engine_Location = models.CharField(max_length=200)
    Wheel_Base = models.FloatField(default=False)
    Length = models.FloatField(default=False)
    Width = models.FloatField(default=False)
    Height = models.FloatField(default=False)
    Curb_Weight = models.IntegerField(default=False)
    Engine_Type = models.CharField(max_length=200)
    Num_of_Cylinders = models.CharField(max_length=200)
    Engine_Size = models.IntegerField(default=False)
    Fuel_System = models.CharField(max_length=200)
    Bore = models.FloatField(default=False)
    Stroke = models.FloatField(default=False)
    Compression_Ratio = models.FloatField(default=False)
    Horsepower = models.IntegerField(default=False)
    Peak_rpm = models.IntegerField(default=False)
    City_mpg = models.IntegerField(default=False)
    Highway_mpg = models.IntegerField(default=False)
    Price = models.IntegerField(default=False)
    Horsepower_Binned = models.CharField(max_length=200)
    Diesel = models.IntegerField(default=False)
    Gas = models.IntegerField(default=False)
    Normal = models.IntegerField(default=False)
    Turbo = models.IntegerField(default=False)
