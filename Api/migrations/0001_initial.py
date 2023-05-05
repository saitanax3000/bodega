# Generated by Django 4.1.2 on 2023-05-05 16:31

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Producto',
            fields=[
                ('idProducto', models.CharField(max_length=20, primary_key=True, serialize=False, verbose_name='id')),
                ('nombre', models.CharField(max_length=25, verbose_name='Nombre producto')),
                ('categoria', models.CharField(max_length=20, verbose_name='Categoria')),
                ('imagen', models.URLField(blank=True, null=True, verbose_name='foto')),
            ],
            options={
                'verbose_name': 'Producto',
                'verbose_name_plural': 'Productos',
                'ordering': ['nombre'],
            },
        ),
    ]
