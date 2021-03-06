# Generated by Django 2.0.6 on 2018-07-23 18:12

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Articles',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=120)),
                ('imgLink', models.TextField()),
                ('bookURL', models.URLField(default='http://avidreaders.ru/author/zhan-kristof-granzhe/')),
                ('post', models.TextField()),
                ('date', models.DateTimeField()),
                ('like', models.IntegerField(default=0)),
                ('authot', models.CharField(max_length=120)),
                ('authorURL', models.URLField(default='https://ru.wikipedia.org/wiki/')),
                ('authorData', models.TextField()),
                ('authotImgLink', models.TextField()),
            ],
        ),
    ]
