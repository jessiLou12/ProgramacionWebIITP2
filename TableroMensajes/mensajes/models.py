from django.db import models
from django.utils import timezone

# Create your models here.
class Mensaje (models.Model):
    remitente= models.CharField(max_length = 500)
    destinatario = models.CharField(max_length = 500)
    texto= models.TextField()
    fecha_hora= models.DateTimeField(auto_now = True)

    ## especifica claramente quien envia y quien recibe
    def __str__(self):
        return f"{self.remitente} a {self.destinatario}:{self.texto}"