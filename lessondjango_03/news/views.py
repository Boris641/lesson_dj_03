from django.shortcuts import render, redirect
from . models import News_post
from . forms import News_postForms

# Create your views here.
def home(request):
    news = News_post.objects.all()
    return render(request,'news/home.html',{'news':news})

def new(request):
    news = News_post.objects.all()
    return render(request,'news/new.html', {'news':news})

def contacts(request):
    return render(request,'news/contacts.html')

def user(request):
    error = ""
    if request.method == 'POST':
        form = News_postForms(request.POST)
        if form.is_valid():
            form.save()
            return redirect(new)

        else:
            error = 'Данные заполнены не корректно'
    form = News_postForms()
    return render(request, 'news/user.html', {'form': form, 'error': error })
