# Generated by Django 4.1.7 on 2023-04-26 22:56

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('qr', '0010_rename_user_qr_usuario'),
    ]

    operations = [
        migrations.AlterField(
            model_name='qr',
            name='usuario',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]