# Generated by Django 4.1.2 on 2022-10-16 15:07

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0011_notes'),
    ]

    operations = [
        migrations.AlterField(
            model_name='notes',
            name='blog_writer',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
