# Generated by Django 4.0.2 on 2022-04-22 15:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0003_service'),
    ]

    operations = [
        migrations.AlterField(
            model_name='service',
            name='image',
            field=models.ImageField(upload_to='images'),
        ),
        migrations.AlterField(
            model_name='service',
            name='service',
            field=models.CharField(max_length=50),
        ),
    ]