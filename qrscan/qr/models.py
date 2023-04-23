from django.db import models
import qrcode
from django_resized import ResizedImageField


class Qr(models.Model):
    data = ResizedImageField(size=[200, 200])
    titulo = models.CharField(max_length=100, null=True)