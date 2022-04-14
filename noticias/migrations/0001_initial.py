# Generated by Django 4.0.3 on 2022-04-08 14:33

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Noticia',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titulo', models.CharField(max_length=200, unique=True)),
                ('data_noticia', models.DateField()),
                ('fonte', models.CharField(max_length=50)),
                ('conteudo', models.TextField()),
                ('url', models.URLField()),
                ('slug', models.SlugField(max_length=255)),
            ],
            options={
                'ordering': ['-data_noticia'],
            },
        ),
    ]
