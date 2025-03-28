from django import forms
from django.contrib.auth.forms import UserCreationForm
from . import models


DEGREE_CHOICES = (
        ("bachelor", "Бакалавр"),
        ("master", "Магистр"),
        ("docent", "Доцент"),
        ("none", "Без диплома"),
    )

class CustomRegisterForm(UserCreationForm):
    degree = forms.ChoiceField(choices=DEGREE_CHOICES, required=True, label="Ваш диплом")
    experience = forms.IntegerField(required=True, label="Опыт работы")
    skills = forms.CharField(widget=forms.Textarea, required=False, label="Навыки")
    languages = forms.CharField(required=False, label="Знание языков")
    certifications = forms.CharField(widget=forms.Textarea, required=False, label="Сертификаты")
    address = forms.CharField(required=True, label="Адрес")
    city = forms.CharField(required=True, label="Город")
    birth_date = forms.DateField(widget=forms.DateInput(attrs={'type': 'date'}), required=True, label="Дата рождения")

    class Meta:
        model = models.CustomUser
        fields = (
            'username',
            'password1',
            'password2',
            'first_name',
            'last_name',
            'degree',
            'experience',
            'skills',
            'languages',
            'certifications',
            'address',
            'city',
            'birth_date'
        )

    def save(self, commit=True):
        user = super().save(commit=False)
        user.degree = self.cleaned_data['degree']
        user.experience = self.cleaned_data['experience']
        user.skills = self.cleaned_data['skills']
        user.languages = self.cleaned_data['languages']
        user.birth_date = self.cleaned_data['birth_date']
        user.certifications = self.cleaned_data['certifications']
        user.address = self.cleaned_data['address']
        user.city = self.cleaned_data['city']

        if commit:
            user.save()
        return user