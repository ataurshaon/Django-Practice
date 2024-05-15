from django.shortcuts import render
from django.http import HttpResponse
from first_app.models import Musician, Album
from first_app import forms

# Create your views here.

# def contact(request):
#     return HttpResponse("<h1>I am from contact path</h1>")

# def home(request):
#     return HttpResponse("<h1>This is home page</h1> <a href='contact/'>Contact</a> <a href='about/'>About Us</a>")

# def contact(request):
#     return HttpResponse("<h1>This is contact page</h1> <a href='/'>Home Page</a> <a href='/about/'>About</a>")

# def about(request):
#     return HttpResponse("<h1>This is about us page</h1> <a href='/'>Home Page</a> <a href='/contact/'>Contact</a>")
    

# def index(request):
    # musicial_list = Musician.objects.order_by('first_name')
    # dic = {'text': 'This is a list of Musicians', 'musician': musicial_list}

    # dic = {'sample_text': Album.objects.get(pk=1)} #by primary key value get release date for filter

    # dic = {'sample_text': "sample text",}
    # return render(request, 'first_app/index.html', context=dic)
    #return HttpResponse("<h1>I am from first app</h1>")

# def form(request):
#     new_form = forms.user_form()
#     diction = {'test_form': new_form, 'heading_1': "This form is using by Django library"}

#     if request.method == 'POST':
#         new_form = forms.user_form(request.POST)

#         diction.update({'test_form':new_form}) #for showing error we need to overwrite previous empty form

#         if new_form.is_valid():
#             # user_name = new_form.cleaned_data['user_name']
#             # user_dob = new_form.cleaned_data['user_dob']
#             # user_email = new_form.cleaned_data['user_email']
#             # boolean_field = new_form.cleaned_data['boolean_field']

#             #field = new_form.cleaned_data['field']

#             #field = new_form.cleaned_data['number_field'] #for integar value custom validation
            


#             # diction.update({'user_name':user_name})
#             # diction.update({'user_dob':user_dob})
#             # diction.update({'user_email':user_email})
#             # diction.update({'form_submitted':"YES"})
#             # diction.update({'boolean_field':boolean_field})

#             #diction.update({'field': field})
#             diction.update({'field': 'Fields Match!!!'})
#             diction.update({'form_submitted': "Yes"})

#             #diction.update({'name': name})


#     return render(request, 'first_app/form.html', context = diction)

# def form(request):
#     new_form = forms.MusicianForm()

#     if request.method == 'POST':
#         new_form = forms.MusicianForm(request.POST)

#         if new_form.is_valid():
#             new_form.save(commit=True)
#             return index(request)
    
#     diction = {'test_form': new_form, 'heading_1': 'Add New Musicians'}

#     return render(request, 'first_app/form.html', context = diction)


# After connecting with mySql views are below

def index(request):
    musician_list = Musician.objects.order_by('first_name')
    diction = { 'title': "Home Page", 'musician_list':musician_list }
    return render(request,'first_app/index.html', context=diction)

def album_list(request):
    diction = { 'title': "List of Albums" }
    return render(request,'first_app/album_list.html', context=diction)

def musician_form(request):
    form = forms.MusicianForm()

    if request.method == 'POST':
        form = forms.MusicianForm(request.POST)

        if form.is_valid():
            form.save(commit=True)
            return index(request)

    diction = { 'title': "Add Musician", 'musician_form':form }
    return render(request,'first_app/musician_form.html', context=diction)

def album_form(request):
    form = forms.AlbumForm()

    if request.method == 'POST':
        form = forms.AlbumForm(request.POST)

        if form.is_valid():
            form.save(commit=True)
            return index(request)

    diction = { 'title': "Add Album", 'album_form': form }
    return render(request,'first_app/album_form.html', context=diction)