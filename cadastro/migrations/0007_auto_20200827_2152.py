# Generated by Django 3.1 on 2020-08-28 00:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cadastro', '0006_auto_20200827_2135'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pessoas',
            name='email',
            field=models.CharField(max_length=70),
        ),
    ]
