from django.db import models


class Books(models.Model):
    GENRE = (
        ('Проза', 'Проза'),
        ('Приключения', 'Приключения'),
        ('Роман', 'Роман'),
        ('Детектив', 'Детектив'),
    )
    image = models.ImageField(upload_to='books/', verbose_name='загрузите фото', null=True)
    title = models.CharField(max_length=100, verbose_name='введите название', null=True)
    description = models.TextField(verbose_name='введите описание', null=True, blank=True)
    price = models.DecimalField(max_digits=10, decimal_places=2, verbose_name='введите цену', null=True)
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='введите дату выхода', null=True)
    genre = models.CharField(max_length=30, choices=GENRE, verbose_name='введите жанр', null=True)
    time = models.TimeField(verbose_name='введите время', null=True)
    author = models.CharField(max_length=100, verbose_name='введите автора', null=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'книга'
        verbose_name_plural = 'книги'

class Reviews(models.Model):
    GRADE = (
        ('1', '1'),
        ('2', '2'),
        ('3', '3'),
        ('4', '4'),
        ('5', '5'),

    )

    choice_book = models.ForeignKey(Books, on_delete=models.CASCADE,
                                    related_name='reviews', verbose_name='выберите книгу', null=True)
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='введите дату выхода', null=True)
    description = models.TextField(null=True,blank=True, verbose_name='введите описание')
    grade = models.CharField(max_length=10, choices=GRADE, default='1', verbose_name='введите оценку', null=True)

    def __str__(self):
        return f'{self.choice_book.title} - {self.grade}'

    class Meta:
        verbose_name = 'отзыв'
        verbose_name_plural = 'отзывы'