from django.db import models

# Create your models here.


class Curso(models.Model):
    nombre = models.CharField(max_length=128)
    inscriptos = models.IntegerField()
    TURNOS = (
    ("Mañana", "Mañana"),
    ("Tarde", "Tarde"),
    ("Tarde", "Noche")
    )
    turno = models.TextChoices("Turno:",choices=TURNOS, default="Noche")
