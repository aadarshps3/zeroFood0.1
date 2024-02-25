import email
from email.headerregistry import Address
from django.db import models
from django.contrib.auth.models import User
# Create your models here.


class NGOExtra(models.Model):
    user=models.OneToOneField(User,on_delete=models.CASCADE)
    address = models.TextField(null=False)
    joindate=models.DateField(auto_now_add=True)
    mobile = models.CharField(max_length=40)
    # claimed=models.BooleanField(default=False)
    def __str__(self):
        return self.user.first_name
    @property
    def get_id(self):
        return self.user.id
    @property
    def get_name(self):
        return self.user.first_name




# classes=[('one','one'),('two','two'),('three','three'),
# ('four','four'),('five','five'),('six','six'),('seven','seven'),('eight','eight'),('nine','nine'),('ten','ten')]
class DonarExtra(models.Model):
    user=models.OneToOneField(User,on_delete=models.CASCADE)
    company_name = models.CharField(max_length=191)
    address=models.TextField(null=False)
    mobile = models.CharField(max_length=40,null=True)
    email= models.CharField(max_length=40)
    fssi_certificate=models.ImageField(upload_to='cerificate')
    # status=models.BooleanField(default=False)
    @property
    def get_name(self):
        return self.user.first_name+" "+self.user.last_name
    @property
    def get_id(self):
        return self.user.id
    def __str__(self):
        return self.user.first_name


food=(
    ('Veg','Veg'),
    ('Non Veg','Non Veg'),
    ('Both','Both')
)
class Donation(models.Model):
    username = models.CharField(max_length=191)
    companyName = models.CharField(max_length=191)
    number = models.CharField(max_length=50)
    address = models.CharField(max_length=500)
    foodName = models.CharField(max_length=191)
    foodImage = models.ImageField(upload_to='static/pics', null=True, blank=True)
    food_type = models.CharField(max_length=50,choices=food)
    quantity = models.CharField(max_length=50)
    hours = models.CharField(max_length=50)
    description = models.CharField(max_length=500, null=True)
    status = models.BooleanField(default = False)
    donationdate=models.DateField(auto_now_add=True)



class Notice(models.Model):
    date=models.DateField(auto_now=True)
    by=models.CharField(max_length=20,null=True,default='food')
    message=models.CharField(max_length=500)

class Claim(models.Model):
    ngoname = models.CharField(max_length=191)
    foodName = models.CharField(max_length=191)
    mobile = models.CharField(max_length=40)
    address = models.TextField(null=False, default="")

class fertilizer(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    Name=models.CharField(max_length=100)
    Location=models.CharField(max_length=100)
    owner_name=models.CharField(max_length=100)
    Phone_no=models.CharField(max_length=10)
    Reg_Id=models.CharField(max_length=4)
    Email_id=models.EmailField()

    def __str__(self):
        return self.user.first_name
    @property
    def get_id(self):
        return self.user.id
    @property
    def get_name(self):
        return self.user.first_name


class ferti_Claim(models.Model):
    fertiname = models.CharField(max_length=191)
    foodName = models.CharField(max_length=191)
    mobile = models.CharField(max_length=40)
    address = models.TextField(null=False, default="")