# Generated by Django 3.0.6 on 2020-05-22 01:00

from django.db import migrations
import mdeditor.fields


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0004_auto_20200521_1857'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='content',
            field=mdeditor.fields.MDTextField(help_text='正文', verbose_name='正文'),
        ),
    ]
