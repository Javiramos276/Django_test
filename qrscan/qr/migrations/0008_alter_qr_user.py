# Generated by Django 4.1.7 on 2023-04-25 20:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('qr', '0007_alter_qr_user'),
    ]

    operations = [
        migrations.AlterField(
            model_name='qr',
            name='user',
            field=models.IntegerField(),
        ),
    ]
