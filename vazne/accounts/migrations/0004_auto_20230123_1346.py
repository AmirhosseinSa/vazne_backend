# Generated by Django 3.2.16 on 2023-01-23 10:16

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('accounts', '0003_auto_20230122_2311'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='credit',
            name='user',
        ),
        migrations.AddField(
            model_name='credit',
            name='owner',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='auth.user'),
            preserve_default=False,
        ),
    ]
