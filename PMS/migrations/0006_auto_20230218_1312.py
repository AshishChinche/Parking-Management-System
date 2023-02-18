# Generated by Django 3.2.7 on 2023-02-18 07:42

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('PMS', '0005_auto_20230218_1306'),
    ]

    operations = [
        migrations.AddField(
            model_name='rows',
            name='building_id',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='PMS.building'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='rows',
            name='total_rows',
            field=models.PositiveIntegerField(default=1),
            preserve_default=False,
        ),
    ]