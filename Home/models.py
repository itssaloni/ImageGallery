from django.db import models

class Category(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name
    
class Tag(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name
    
class Image(models.Model):
    file = models.ImageField("uploads/")
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name="images")
    tags = models.ManyToManyField(Tag, related_name="images")

    def __str__(self):
        return self.file.name
    
class Place(models.Model):
    title = models.CharField(max_length=50)
    country = models.CharField(max_length=50)
    state = models.CharField(max_length=50)
    PinCode = models.IntegerField(default=None,blank=True,null=True)
    city = models.CharField(max_length=50,default=None, null=True)
    priority = models.IntegerField(default=None,blank=True,null=True)
    district = models.IntegerField(default=None,blank=True,null=True)
    fgxffdg = models.CharField(max_length=50,default="abc")