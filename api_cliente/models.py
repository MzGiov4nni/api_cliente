from django.db import models

# Create your models here.

from django.db import models

class Registro_cliente(models.Model):
    Nombre_Completo=models.CharField(max_length=100)
    Edad=models.PositiveBigIntegerField()
    numero_telefonico=models.PositiveBigIntegerField()
    correo_electronico=models.CharField(max_length=100)

    class Meta:
        db_table = 'Registro_cliente'

    def __str__(self) -> str:
        return self.Nombre_Completo


