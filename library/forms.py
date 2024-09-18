from django import forms
from .models import Book, Category



class CategoryForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = ['name'] 

        widgets = {
            'name': forms.TextInput(attrs={'class':'form-control'}),
            }




class BookForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = '__all__'  

        widgets = {
            'title': forms.TextInput(attrs={'class':'form-control'}),
            'author': forms.TextInput(attrs={'class':'form-control'}),
            'pages': forms.NumberInput(attrs={'class':'form-control'}),
            'photo_book': forms.FileInput(attrs={'class':'form-control'}),
            'photo_author': forms.FileInput(attrs={'class':'form-control'}),
            'pricee': forms.NumberInput(attrs={'class':'form-control'}),
            'rental_price_day': forms.NumberInput(attrs={'class':'form-control' ,'id':'rentalprice'}),
            'rental_period': forms.NumberInput(attrs={'class':'form-control' ,'id':'rentaldays'}),
            'total_rental': forms.NumberInput(attrs={'class':'form-control' ,'id':'totalrental'}),
            'active': forms.NullBooleanSelect(attrs={'class':'form-control'}),
            'state': forms.Select(attrs={'class':'form-control'}),
            'Category': forms.Select(attrs={'class':'form-control'}),
            
        }
