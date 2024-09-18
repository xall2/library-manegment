from django.db import models



class Category(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self): 
        return self.name





class bookState(models.TextChoices):
    AVAILABLE = 'Available'
    RENTAL = 'Rental'
    SOLD = 'Sold'
    

class Book(models.Model):
    title = models.CharField(max_length=250)
    author = models.CharField(max_length=250,null=True , blank=True)
    photo_book = models.ImageField(upload_to='photos',null=True , blank=True)
    photo_author = models.ImageField(upload_to='photos',null=True , blank=True)
    pages = models.IntegerField(null=True , blank=True)
    pricee = models.DecimalField(max_digits=6 , decimal_places=2,null=True , blank=True)
    rental_price_day = models.DecimalField(max_digits=6 , decimal_places=2,null=True , blank=True)  #ايجار الكتاب في اليوم
    rental_period = models.IntegerField(null=True , blank=True) #عدد ايام الايجار
    total_rental = models.DecimalField(max_digits=6 , decimal_places=2,null=True , blank=True) 
    active = models.BooleanField(default=True) #هل الكتاب متاح او لا
    state  = models.CharField(max_length=50,choices=bookState.choices,null=True , blank=True) #هل الكتاب متاح ولا تم بيعه ولا  تم استأجاره
    Category = models.ForeignKey(Category,on_delete=models.SET_NULL,null=True , blank=True)

    def __str__(self): 
        return self.title
