# Generated by Django 4.1.3 on 2022-11-20 10:16

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0002_alter_author_name_author'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='author',
            options={'verbose_name': 'Автор', 'verbose_name_plural': 'Авторы'},
        ),
        migrations.AlterModelOptions(
            name='book',
            options={'verbose_name': 'Книги', 'verbose_name_plural': 'Книги'},
        ),
        migrations.AlterModelOptions(
            name='city',
            options={'verbose_name': 'Город', 'verbose_name_plural': 'Города'},
        ),
        migrations.AlterModelOptions(
            name='client',
            options={'verbose_name': 'Клиент', 'verbose_name_plural': 'Клиенты'},
        ),
        migrations.AlterModelOptions(
            name='genre',
            options={'verbose_name': 'Жанр', 'verbose_name_plural': 'Жанры'},
        ),
        migrations.AlterField(
            model_name='book',
            name='amount',
            field=models.IntegerField(blank=True, verbose_name='Колличество'),
        ),
        migrations.AlterField(
            model_name='book',
            name='author_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='news.author', verbose_name='Автор'),
        ),
        migrations.AlterField(
            model_name='book',
            name='genres',
            field=models.ManyToManyField(to='news.genre', verbose_name='Жанр'),
        ),
        migrations.AlterField(
            model_name='book',
            name='price',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=9, verbose_name='Стоймость'),
        ),
        migrations.AlterField(
            model_name='book',
            name='title',
            field=models.CharField(db_index=True, max_length=150, verbose_name='Наименование книги'),
        ),
        migrations.AlterField(
            model_name='city',
            name='days_delivery',
            field=models.IntegerField(blank=True, verbose_name='Количество дней доставки'),
        ),
        migrations.AlterField(
            model_name='city',
            name='name_city',
            field=models.CharField(db_index=True, max_length=150, verbose_name='Город'),
        ),
        migrations.AlterField(
            model_name='genre',
            name='name_genre',
            field=models.CharField(max_length=150, verbose_name='Жанр'),
        ),
    ]
