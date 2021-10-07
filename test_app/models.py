from django.db import models

class Blog(models.Model):
    title = models.CharField(max_length=100)
    contents = models.TextField()
    author = models.CharField(max_length=20)
    created_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

class Car(models.Model):
    name = models.CharField(max_length=20)
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name






























# from django.db.models.fields import BigIntegerField, BooleanField, FloatField, IntegerField, PositiveIntegerField, TextField
# from django.db.models.fields.related import ForeignKey, ManyToManyField, OneToOneField


        # models.CharField(max_length=200)
        # models.TextField() #has no restriction to max_length
        # models.IntegerField() #start from -0 to +9 and -9 to +9
        # models.BigIntegerField() #this takes in big integer numbers
        # models.PositiveIntegerField() #incase you dont want a negative path,defining a model that does not accept a negative value then you can define a positiveintegerfield
        # models.FloatField() #takes in decimal values
        # models.BooleanField() #gives a true or false value
        # models.ManyToManyField() #defines a relationship between two models and specifying that the two models can have many models over many models
        # models.OneToOneField() #one model can have one of another model, it can be multiple
        # models.ForeignKey() - OneToManyField #one model has many other entries
        # models.DateField() #this one will only show the dates
        # models.DateTimeField() #this one will show both the dates and the time
        # models.TimeField() #this one will only show the time

# Create your models here.
# class TestModel(models.Model):
#     name = models.CharField(max_length=255) #can add unique=True, null=True, blank=True
#     #name = models.CharField(max_length=255, unique=True, null=True, error_messages={"null":"this field cannot be null"})
#     description = models.TextField()
#     phone_number = models.PositiveIntegerField()
#     is_active = models.BooleanField()
#     amount = models.FloatField()
#     extra_name = models.CharField(max_length=250,editable=False, default="null") #wont appear on admin and cant be editable
#     created_at = models.DateTimeField(auto_now_add=True) 
#     updated_at = models.DateTimeField(auto_now=True) #auto_now means change this everytime

#     def __str__(self):
#         return f"{self.name}"
#         #return f"{self.name} - {self.created_at.strftime('%H: %M: %S')}"

#     class Meta:
#         ordering = ("-created_at",)
#         verbose_name_plural = "Test Model"

#     #overriding default save process
#     def save(self, *args, **kwargs):
#         self.extra_name = f"{self.name} - {self.phone_number}"
#         super().save(*args, **kwargs)

#     # def __str__(self):
#     #     return f"{self.extra_name}"   #This will now save names from admin pannel(test models) with name - phonenumber

# #Relationships
# #ForeignKey here means that a single TestModel can have multiple ModelX
# class ModelX(models.Model): #we can also use ....ForeignKey("appname.TestModel",) this is if TestModel is not here but in another app and ...on delete is of two ways , on_delete= models.SET_NULL, null=True or on_delete=models.CASCADE means when deleting it also deletes whatever model it is referencing to.
#     test_content = models.ForeignKey(
#         TestModel, on_delete=models.CASCADE, related_name="test_content")
#     mileage = models.FloatField()
#     created_at = models.DateTimeField(auto_now_add=True) 
#     updated_at = models.DateTimeField(auto_now=True)

#     def __str__(self):
#         return f"{self.test_content.name} - {self.mileage}"

#     class Meta:
#         ordering = ("-created_at",)
#         verbose_name_plural = "ModelX"

# #OneToOneField here means we can only have a single relationship with each other
# class ModelY(models.Model): 
#     test_content = models.OneToOneField(
#         TestModel, on_delete=models.CASCADE, related_name="test_content_y")
#     mileage = models.FloatField()
#     created_at = models.DateTimeField(auto_now_add=True) 
#     updated_at = models.DateTimeField(auto_now=True)

#     def __str__(self):
#         return f"{self.test_content.name} - {self.mileage}"

#     class Meta:
#         ordering = ("-created_at",)
#         verbose_name_plural = "ModelY"


