from django.db import models

class Categoria(models.Model):
    nombre = models.CharField(max_length=200)
    icono = models.CharField(max_length=200, blank=True, null=True)
    descripcion = models.CharField(max_length=200, blank=True, null=True, db_column='Descripcion')
    activo = models.BooleanField(default=True)
    fecha_modificacion = models.DateTimeField(auto_now=True, db_column='Fecha_modificacion')
    fecha_creacion = models.DateTimeField(auto_now_add=True, db_column='Fecha_creacion')

    class Meta:
        db_table = '"tienda"."categorias_producto"'

class Producto(models.Model):
    categoria = models.ForeignKey(Categoria, on_delete=models.SET_NULL, null=True)
    nombre = models.CharField(max_length=200)
    marca = models.CharField(max_length=200, blank=True, null=True)
    sabor = models.CharField(max_length=200, blank=True, null=True)
    precio = models.DecimalField(max_digits=10, decimal_places=2)
    precio_original = models.DecimalField(max_digits=10, decimal_places=2, null=True)
    impuesto = models.DecimalField(max_digits=10, decimal_places=2, null=True, db_column='Impuesto')
    porcion_g = models.IntegerField(null=True)
    porciones = models.IntegerField(null=True)
    descripcion = models.TextField(blank=True, null=True)
    imagen_url = models.CharField(max_length=500, blank=True, null=True)
    stock = models.IntegerField(default=0)
    es_nuevo = models.BooleanField(default=False)
    descuento_pct = models.IntegerField(default=0)
    calificacion_prom = models.DecimalField(max_digits=3, decimal_places=2, default=0)
    total_resenas = models.IntegerField(default=0)
    activo = models.BooleanField(default=True)
    fecha_modificacion = models.DateTimeField(auto_now=True, db_column='Fecha_modificacion')
    fecha_creacion = models.DateTimeField(auto_now_add=True, db_column='Fecha_creacion')

    class Meta:
        db_table = '"tienda"."productos"'

class Resena(models.Model):
    producto = models.ForeignKey(Producto, on_delete=models.CASCADE)
    usuario_id = models.IntegerField()
    calificacion = models.IntegerField()
    activo = models.BooleanField(default=True)
    fecha_modificacion = models.DateTimeField(auto_now=True, db_column='Fecha_modificacion')
    fecha_creacion = models.DateTimeField(auto_now_add=True, db_column='Fecha_creacion')

    class Meta:
        db_table = '"tienda"."resenas_producto"'

class Carrito(models.Model):
    usuario_id = models.IntegerField()
    activo = models.BooleanField(default=True)
    fecha_modificacion = models.DateTimeField(auto_now=True, db_column='Fecha_modificacion')
    fecha_creacion = models.DateTimeField(auto_now_add=True, db_column='Fecha_creacion')

    class Meta:
        db_table = '"tienda"."carrito"'

class CarritoItem(models.Model):
    id_carrito= models.AutoField(primary_key=True)
    carrito = models.ForeignKey(Carrito, on_delete=models.CASCADE)
    producto = models.ForeignKey(Producto, on_delete=models.CASCADE)
    cantidad = models.IntegerField(default=1)
    precio_unitario = models.DecimalField(max_digits=10, decimal_places=2)
    activo = models.BooleanField(default=True)
    fecha_modificacion = models.DateTimeField(auto_now=True, db_column='Fecha_modificacion')
    fecha_creacion = models.DateTimeField(auto_now_add=True, db_column='Fecha_creacion')

    class Meta:
        db_table = '"tienda"."carrito_items"'

class Pedido(models.Model):
    id_pedido = models.AutoField(primary_key=True)
    usuario_id = models.IntegerField()
    subtotal = models.DecimalField(max_digits=10, decimal_places=2)
    envio = models.DecimalField(max_digits=10, decimal_places=2)
    impuesto = models.DecimalField(max_digits=10, decimal_places=2)
    total = models.DecimalField(max_digits=10, decimal_places=2)
    metodo_pago = models.CharField(max_length=100)
    estado_pago = models.CharField(max_length=100)
    estado_pedido = models.CharField(max_length=100)
    nombre_receptor = models.CharField(max_length=200)
    apellido_receptor = models.CharField(max_length=200)
    email_receptor = models.CharField(max_length=200)
    telefono = models.CharField(max_length=50)
    direccion_envio = models.CharField(max_length=500)
    activo = models.BooleanField(default=True)
    fecha_modificacion = models.DateTimeField(auto_now=True, db_column='Fecha_modificacion')
    fecha_creacion = models.DateTimeField(auto_now_add=True, db_column='Fecha_creacion')

    class Meta:
        db_table = '"tienda"."pedidos"'

class PedidoItem(models.Model):
    pedido = models.ForeignKey(Pedido, on_delete=models.CASCADE)
    producto = models.ForeignKey(Producto, on_delete=models.CASCADE)
    cantidad = models.IntegerField(default=1)
    precio_unitario = models.DecimalField(max_digits=10, decimal_places=2)
    subtotal = models.DecimalField(max_digits=10, decimal_places=2)
    activo = models.BooleanField(default=True)
    fecha_modificacion = models.DateTimeField(auto_now=True, db_column='Fecha_modificacion')
    fecha_creacion = models.DateTimeField(auto_now_add=True, db_column='Fecha_creacion')

    class Meta:
        db_table = '"tienda"."pedido_items"'