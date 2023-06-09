# Generated by Django 4.0.6 on 2023-04-25 16:59

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('ponto', '0004_alter_registroponto_data_hora'),
    ]

    operations = [
        migrations.AlterField(
            model_name='registroponto',
            name='data_hora',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
        migrations.AlterField(
            model_name='registroponto',
            name='tipo',
            field=models.CharField(choices=[('Entrada', 'entrada'), ('Saída', 'saída'), ('Exceção(entrada)', 'exceçao(entrada)'), ('Exceção(saída)', 'exceçao(saída)')], max_length=20),
        ),
    ]
