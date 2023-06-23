# Generated by Django 4.2.2 on 2023-06-21 21:52

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Task',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nameTranslit', models.CharField(max_length=255)),
                ('price', models.IntegerField(null=True)),
                ('name', models.CharField(max_length=255)),
                ('cashback', models.CharField(max_length=255)),
                ('screen', models.CharField(max_length=255)),
                ('brand', models.CharField(max_length=255)),
                ('proc', models.CharField(max_length=255)),
                ('rom', models.CharField(max_length=255)),
                ('camera', models.CharField(max_length=255)),
                ('cur_price', models.CharField(max_length=255)),
                ('previous_price', models.IntegerField(null=True)),
                ('slug', models.SlugField(default='')),
            ],
        ),
    ]