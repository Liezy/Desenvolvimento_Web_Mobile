# Generated by Django 5.0.4 on 2024-05-08 22:28

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('veiculo', '0003_veiculo_foto'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='veiculo',
            name='foto',
        ),
    ]
