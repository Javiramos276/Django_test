# Generated by Django 4.1.7 on 2023-04-07 00:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('qr', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='qr',
            name='titulo',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='qr',
            name='data',
            field=models.ImageField(upload_to='media'),
        ),
    ]
