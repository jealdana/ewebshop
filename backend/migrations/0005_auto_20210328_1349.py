# Generated by Django 3.1.7 on 2021-03-28 13:49

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('backend', '0004_auto_20210328_1010'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='product',
            options={'ordering': ['-id', '-name', '-code'], 'verbose_name': 'product'},
        ),
    ]
