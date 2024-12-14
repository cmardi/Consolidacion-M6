from django.db import models

class VehiculoModel(models.Model):
    marcas = [ 
    ('FIAT', 'Fiat'),
    ('CHEVROLET','Chevrolet'),
    ('FORD', 'Ford'),
    ('TOYOTA', 'Toyota'),
    ]
    
    marca = models.CharField(max_length=20, choices=marcas, default='FORD')
    modelo = models.CharField(max_length=100)
    serial_carroceria = models.CharField(max_length=50) 
    serial_motor = models.CharField(max_length=50)

    categorias = [
        ('PARTICULAR', 'Particular'),
        ('TRANSPORTE', 'Transporte'),
        ('CARGA', 'Carga')
    ]

    categoria = models.CharField(max_length = 20, choices = categorias, default = 'PARTICULAR')
    precio = models.DecimalField(max_digits=10, decimal_places=2)
    fecha_creacion = models.DateTimeField(auto_now_add=True)
    fecha_modificacion = models.DateTimeField(auto_now=True)
    
    class Meta:
        permissions = (
            ('visualizar_catalogo', 'Visualizar catálogo de Vehículos'),
        )
        
    def __str__(self):
        return f"{self.marca} {self.modelo} - ${self.precio}"
