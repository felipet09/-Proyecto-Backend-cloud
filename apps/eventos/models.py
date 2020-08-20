from django.db import models

# Create your models here.
class Categoria (models.Model):
    id = models.AutoField(primary_key = True)
    descripcion_cat = models.CharField(max_length=40, null=False, blank=False)

    class Meta:
        verbose_name = 'Categoria'
        verbose_name_plural = 'Categorias'
        ordering = ['id']
    
    def __str__(self):
        return '{} - {}'.format(self.id, self.descripcion_cat)

class Tipo (models.Model):
    id = models.AutoField(primary_key = True)
    descripcion_tipo = models.CharField(max_length=40, null=False, blank=False)

    class Meta:
        verbose_name = 'Tipo evento'
        verbose_name_plural = 'Tipos de eventos'
        ordering = ['id']
    
    def __str__(self):
        return '{} - {}'.format(self.id, self.descripcion_tipo)

class Evento(models.Model):
    id = models.AutoField(primary_key = True)
    nombre = models.CharField(max_length = 200, blank=False, null=False)
    lugar = models.CharField(max_length = 200, blank=False, null=False)
    direccion = models.CharField(max_length = 200, blank=False, null=False)
    fecha_inicio = models.DateField(null=True, blank=True)
    fecha_final = models.DateField(null=True, blank=True)
    id_categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE)
#    id_evento = models.ForeignKey(Tipo, on_delete=models.CASCADE)

    class Meta:
        verbose_name = 'Evento'
        verbose_name_plural = 'Eventos'
        ordering = ['id']
    
    def __str__(self):
        return '{} - {}'.format(self.id, self.nombre)