# Generated by Django 3.0.3 on 2020-02-16 21:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('booklist', '0006_userfavorite'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='book',
            name='user',
        ),
        migrations.AddField(
            model_name='Userfavorite',
            name='rating',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.DeleteModel(
            name='Review',
        ),
    ]
