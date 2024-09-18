from django.shortcuts import get_object_or_404, render,redirect
from .models import *
from .forms import BookForm, CategoryForm






def index(request):
    #اضيف كتاب في الداتابيس من الموقع
    if request.method == 'POST':
        add_book = BookForm(request.POST, request.FILES) #راح ياخذ الداتا والصور اللي ادخلها اليوزر ويحفظها في الداتابيس
        if add_book.is_valid():
           add_book.save()


    #اضيف تصنيف في الداتابيس من الموقع
    if request.method == 'POST':
        add_category = CategoryForm(request.POST)
        if add_category.is_valid():
           add_category.save()


    context = {
        'books': Book.objects.all(),
        'category' : Category.objects.all(),
        'form':BookForm(),
        'categoryForm' : CategoryForm(),
        'number_books' :Book.objects.filter(active=True).count(), #يرجع عدد الكتب الاكتيف
        'sold_books' :Book.objects.filter(state='Sold').count(),
        'rental_books' :Book.objects.filter(state='Rental').count(),
        'available_books' :Book.objects.filter(state='Available').count(),

    }
    return render(request, 'pages/index.html', context)




def books(request):
    search = Book.objects.all() #هذا عشان يرجع كل الكتب اذا دخل الراوت بدون ما سوى بحث,اذا ماسوى بحث راح تكون هذي قيمته,اما اذا سوى بحث راح تتغير قيمته تحت  شوفي

    #search
    title = None
    if 'search_name' in request.GET:   #سيرش نيم هذه موجودة في تاق الانبوت اللي لما اليوزر يدخل شيء راح تنحفظ في هذا المتغير
        title = request.GET['search_name'] #يرجع الانبوت اللي دخله اليوزر
        if title:
            search = search.filter(title__icontains=title)  #افلتر البحث من خلال  العنوان حق الكتاب واقدر ابحث بأشياء ثانية زي التصنيف مثلا


    context = {
        'books': search,
        'category' : Category.objects.all(),
        'categoryForm' : CategoryForm(),
    }
    return render(request, 'pages/books.html',context)




def update(request,id):
   
    book_id = Book.objects.get(id=id) #راح يرجع لي الايدي حق الكتاب, يعني كأني قلتله جيب الايدي  من الايدي اللي في البراميتر اللي راح يجيني مع الريكويست
    
    #هذا حق لما اروح لصفحة التعديل واعدل البيانات واضغط سيف
    if request.method == 'POST':
        book_save = BookForm(request.POST, request.FILES, instance=book_id) #ابغى الفورم ترجع ببيانات الكتاب الخاص بالايدي
        if book_save.is_valid():
           book_save.save()
           return redirect('/') #راح يرجع لصفحة الانديكس لان الباث حقها كذا

    else:  #هذا حق لما يضغط زر التعديل اللي من صفحة الانديكس عشان يوديه لصفحة التعديل
         context = {
             'form' : BookForm(instance=book_id) #ابغى يكون عندي فورم لكن بداخلها بيانات الكتاب الخاص بهذا الايدي
         }
        
    return render(request, 'pages/update.html',context)


def delete(request,id):
    book_id = get_object_or_404(Book, id=id) #راح يرجع لي الايدي حق الكتاب, يعني كأني قلتله جيب الايدي  من الايدي اللي في البراميتر اللي راح يجيني مع الريكويست
    
    #اذا راح لصفحة الحذف وضغط حذف
    if request.method == 'POST':
        book_id.delete()
        return redirect('/') #راح يرجع لصفحة الانديكس لان الباث حقها كذا
    
    
    return render(request, 'pages/delete.html')

