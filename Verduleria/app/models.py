from django.db import models

# Create your models here.


class Producto(models.Model):
    nombre = models.CharField(max_length = 60)

    def __str__(self):
        return "nombre: {}".format(self.nombre)

class Factura (models.Model):
    cliente = models.CharField(max_length = 100)
    tipo = models.CharField(max_length = 1)
    numero = models.IntegerField(null = True)
    fecha_de_compra = models.DateField()

    def total (self):
        total= 0
        precio= 0
        compra= self.compras.all()
        for a in compra :
            precio= a.cantidad* a.precio
            total += precio
        return (total)

    def __str__(self):
        return "{} Num.{}".format(self.cliente, self.numero)

class Compra (models.Model):
    producto = models.ForeignKey(Producto, on_delete=models.CASCADE, related_name="producto")
    cantidad = models.IntegerField()
    precio = models.IntegerField(null = True)
    nrofactura = models.ForeignKey(Factura, on_delete=models.CASCADE, null=True, related_name="nrofactura")

    def totalxd (self):
        totalxd=0
        totalxd = self.precio * self.cantidad
        return (totalxd)

    def __str__(self):
        return "factura de {}".format(self.nrofactura)