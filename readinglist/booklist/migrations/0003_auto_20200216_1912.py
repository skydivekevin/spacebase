# Generated by Django 3.0.3 on 2020-02-16 19:12

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('booklist', '0002_review'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='book',
            name='booklists',
        ),
        migrations.DeleteModel(
            name='Booklist',
        ),
    ]
