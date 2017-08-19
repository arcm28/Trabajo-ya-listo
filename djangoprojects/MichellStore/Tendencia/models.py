from django.db import models

class provider(models.Model):
    name=models.CharField(max_length=50,help_text='')

class Product(models.Model):
	typeproduct=(
			('H','Hombre'),
			('M','Mujer'),
			('A','Accesorios'),
			('Z','Zapatos'),
			('C','Cosmeticos')
    )
	color=(
			('R','Rojo'),
			('A','Azul'),
			('M','Morado'),
			('E','Esmeralda'),
			('N','Negro')
	)
	description=models.CharField(max_length=50,help_text='Ingrese el nombre del producto')
	provider=models.CharField(max_length=50,help_text='MichellStore')
	typeproduct=models.CharField(max_length=1,help_text='Seleccione la Categoria del Producto',choices=typeproduct)
	color=models.CharField(max_length=1,help_text='Seleccione el Color del Producto',choices=color)
	date=models.DateField(auto_now=True)

