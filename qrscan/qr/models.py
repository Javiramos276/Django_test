from django.db import models
import qrcode


class Qr(models.Model):
    data = models.ImageField()
    titulo = models.CharField(max_length=100, null=True)