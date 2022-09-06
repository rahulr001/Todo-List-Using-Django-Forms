# Generated by Django 4.1 on 2022-09-05 15:56

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('Todo', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='todolist',
            name='unique_user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]