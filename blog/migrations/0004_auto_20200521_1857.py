# Generated by Django 3.0.6 on 2020-05-21 18:57

import ckeditor.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0003_auto_20200521_1836'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='content',
            field=ckeditor.fields.RichTextField(help_text='正文', verbose_name='正文'),
        ),
    ]
