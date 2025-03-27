from django import forms
from . import models, parser_mybook, parser_rezka

class ParserForm(forms.Form):
    MEDIA_CHOICES = (
        ('mybook.ru', 'mybook.ru'),
        ('Rezka.ag', 'Rezka.ag'),
    )
    media_type = forms.ChoiceField(choices=MEDIA_CHOICES)

    class Meta:
        fields = [
            'media_type',
        ]
    def parser_data(self):
        if self.data['media_type'] == 'mybook.ru':
            my_books = parser_mybook.parsing_mybook()
            for i in my_books:
                models.MybookModel.objects.create(**i)
        elif self.data['media_type'] == 'Rezka.ag':
            rezka_films = parser_rezka.parsing_rezka()
            for i in rezka_films:
                models.RezkaFilmsModel.objects.create(**i)