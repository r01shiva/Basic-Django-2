# Generated by Django 2.0.7 on 2018-09-07 20:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cleaning', '0002_auto_20180908_0129'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='color',
            field=models.CharField(default='', max_length=20),
        ),
        migrations.AlterField(
            model_name='product',
            name='material',
            field=models.CharField(default='', max_length=30),
        ),
        migrations.AlterField(
            model_name='product',
            name='shape',
            field=models.CharField(default='', max_length=20),
        ),
        migrations.AlterField(
            model_name='product',
            name='usage',
            field=models.CharField(default='', max_length=30),
        ),
    ]
