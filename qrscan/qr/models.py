from django.db import models
import qrcode


class Qr(models.Model):
    data = models.ImageField(upload_to='media')
    titulo = models.CharField(max_length=100, null=True)