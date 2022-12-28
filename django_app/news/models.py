from django.db import models
from django.urls import reverse


class Author(models.Model):
    name_author = models.CharField(max_length=150, db_index=True, verbose_name='Автор')

    def __str__(self):
        return self.name_author

    class Meta:
        verbose_name = "Автор"
        verbose_name_plural = "Авторы"


class Book(models.Model):
    title = models.CharField(max_length=150, db_index=True, verbose_name='Наименование книги')
    price = models.DecimalField(max_digits=9, decimal_places=2, blank=True, verbose_name='Стоймость')
    amount = models.IntegerField(blank=True, verbose_name='Колличество')
    image_path = models.ImageField(upload_to='photo', blank=True)
    author_id = models.ForeignKey('Author', on_delete=models.PROTECT, verbose_name='Автор')
    genres = models.ManyToManyField('Genre', verbose_name='Жанр')

    def __str__(self):
        return self.title

    #кнопка смотреть на сайту в админ панели
    def get_absolute_url(self):
        return reverse("news", kwargs={"book_id": self.pk})

    # наименование блоков в админ панели
    class Meta:
        verbose_name = "Книги"
        verbose_name_plural = "Книги"
        # ordering = ['title']


class Genre(models.Model):
    name_genre = models.CharField(max_length=150, verbose_name="Жанр")

    def __str__(self):
        return self.name_genre

    class Meta:
        verbose_name = "Жанр"
        verbose_name_plural = "Жанры"


class City(models.Model):
    name_city = models.CharField(max_length=150, db_index=True, verbose_name="Город", unique=True)
    days_delivery = models.IntegerField(blank=True, verbose_name="Количество дней доставки")

    class Meta:
        verbose_name = "Город"
        verbose_name_plural = "Города"


class Client(models.Model):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    email = models.EmailField(max_length=254, db_index=True, unique=True)
    login = models.CharField(max_length=255)
    psw_hash = models.CharField(max_length=256)
    city_id = models.ForeignKey('City', on_delete=models.PROTECT)

    class Meta:
        verbose_name = "Клиент"
        verbose_name_plural = "Клиенты"


class Step(models.Model):
    name_step = models.CharField(max_length=255)


class Order(models.Model):
    client_id = models.ForeignKey('Client', on_delete=models.CASCADE)
    steps = models.ManyToManyField('Step')
    date = models.DateTimeField(auto_now_add=True)
    amount = models.IntegerField()
    books = models.ManyToManyField('Book')
