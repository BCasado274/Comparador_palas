# Generated by Django 5.1.7 on 2025-04-02 12:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('palas', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='pala',
            name='marca',
            field=models.CharField(default='Desconocida', max_length=100),
            preserve_default=False,
        ),
    ]
