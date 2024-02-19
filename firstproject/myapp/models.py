from django.db import models

# Create your models here.
class Name(models.Model):
    name=models.CharField(max_length=30)
    number=models.IntegerField()
    # def __str__(self):
    #     return self.name


class Customer_Detail(models.Model):
    cname=models.CharField(max_length=20)
    clname=models.CharField(max_length=10)
    cadd=models.TextField(max_length=100)
    phone=models.IntegerField()
    salary=models.IntegerField()
    def __str__(self):
        return self.cname
    

class Blog(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    image = models.ImageField(upload_to='blog_images/', null=True, blank=True)



# fname
# lname
# Address
# pincode
# phone
