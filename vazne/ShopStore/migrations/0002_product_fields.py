# Generated by Django 3.2.16 on 2022-12-29 19:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ShopStore', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='fields',
            field=models.CharField(choices=[('football', 'football'), ('basketball', 'basketball'), ('swim', 'swim')], default=1, max_length=100),
            preserve_default=False,
        ),
    ]
