# Generated by Django 3.1 on 2020-08-28 12:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cadastro', '0008_auto_20200827_2215'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pessoas',
            name='email',
            field=models.EmailField(max_length=70),
        ),
    ]
