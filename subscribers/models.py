from tabnanny import verbose
from django.db import models

class Subscribers(models.Model):

    email = models.EmailField(blank=False, null=False, help_text="Correo Electronico")
    full_name = models.CharField(max_length=40, blank=False, null=False, help_text="Nombre y Apellido")

    def __str__(self):
        return self.full_name

    class Meta:
        verbose_name = "Subscriptor"
        verbose_name_plural = "Subscriptores"