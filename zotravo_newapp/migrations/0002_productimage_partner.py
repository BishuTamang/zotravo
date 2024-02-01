# Generated by Django 4.2.2 on 2024-02-01 07:47

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('zotravo_newapp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='productimage',
            name='partner',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='images', to='zotravo_newapp.partner'),
            preserve_default=False,
        ),
    ]
