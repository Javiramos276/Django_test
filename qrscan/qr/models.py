from django.db import models
import qrcode
from django_resized import ResizedImageField
from django.contrib.auth.models import User


class Qr(models.Model):
    data = ResizedImageField(size=[200, 200])
    titulo = models.CharField(max_length=100, null=True)
    usuario = models.ForeignKey(User, on_delete=models.CASCADE)
