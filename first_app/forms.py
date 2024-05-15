from django import forms
from django.core import validators
from first_app import models

#below function is for only even input for number_field
# def even_or_not(value):
#     if value%2 == 1:
#      raise forms.ValidationError("Please insert an even number")

#class user_form(forms.Form):
    # user_name = forms.CharField(label= "Full Name", widget=forms.TextInput(attrs={'placeholder':'Enter Your Full Name', 'style':'width:300px'}))
    # user_dob = forms.DateField(label="Date of Birth", widget=forms.TextInput(attrs={'type':'date'}))
    # user_email = forms.EmailField(label="User Email", widget=forms.TextInput(attrs={'placeholder' : 'Enter Your Email Address' }))
    # boolean_field = forms.BooleanField(required='false')

    # field = forms.CharField(max_length=15, min_length=5)

    #Drop down code below
    # choices = (('', '--Select Option--'), ('1', 'First'), ('2', 'Second'), ('3', 'Third'))
    # field = forms.ChoiceField(choices=choices, required=False) #required false because of for taking empty value

    #Radio button code below
    # choices = (('A', 'A'), ('B', 'B'), ('C', 'C'))
    # field = forms.ChoiceField(choices= choices, widget=forms.RadioSelect)

    #Multiple value selected drop down code below
    # choices = (('', '--Select Option--'), ('1', 'First'), ('2', 'Second'), ('3', 'Third'))
    # field = forms.MultipleChoiceField(choices=choices, required=False) #required false because of for taking empty value

    #Multiple value selected code below
    # choices = (('A', 'A'), ('B', 'B'), ('C', 'C'))
    # field = forms.MultipleChoiceField(choices= choices)

    #Multiple checkbox value selected code below
    # choices = (('A', 'A'), ('B', 'B'), ('C', 'C'))
    # field = forms.MultipleChoiceField(choices= choices, widget=forms.CheckboxSelectMultiple)

    #Validators
    #name = forms.CharField(validators=[validators.MaxLengthValidator(10), validators.MinLengthValidator(5)])
    #number_field = forms.IntegerField(validators=[validators.MaxValueValidator(15), validators.MinValueValidator(5)])

    #number_field = forms.IntegerField(validators=[even_or_not])

    #below code for email verification
    # user_email = forms.EmailField()
    # user_vmail = forms.EmailField()

    # def clean(self):
    #     all_cleaned_data = super().clean()
    #     user_email = all_cleaned_data['user_email']
    #     user_vmail = all_cleaned_data['user_vmail']

    #     if user_email != user_vmail:
    #         raise forms.ValidationError("Field Don't Match")


    #Form create from models
class MusicianForm(forms.ModelForm):
    class Meta:
        model = models.Musician
        fields = "__all__" # keep all the values of the models
        #fields = ('first_name', 'last_name')
        #exclude = ['first_name'] #for not showing this

class AlbumForm(forms.ModelForm):
    release_date = forms.DateField(widget=forms.TextInput(attrs={'type':'date' }))
    
    class Meta:
        model = models.Album
        fields = "__all__"
