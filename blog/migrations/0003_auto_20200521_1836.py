# Generated by Django 3.0.6 on 2020-05-21 18:36

from django.db import migrations
import markdownx.models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_auto_20200520_1759'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='content',
            field=markdownx.models.MarkdownxField(help_text='正文', verbose_name='正文'),
        ),
    ]
