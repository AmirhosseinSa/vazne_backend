# Generated by Django 3.2.16 on 2022-11-15 18:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0002_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='images',
            field=models.ImageField(default='Images/None/No-img.jpg', upload_to='Images/'),
        ),
        migrations.DeleteModel(
            name='image',
        ),
    ]
