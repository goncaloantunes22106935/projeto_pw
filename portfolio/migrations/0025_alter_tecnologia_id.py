# Generated by Django 4.0.5 on 2022-06-17 16:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio', '0024_tecnologia'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tecnologia',
            name='id',
            field=models.BigAutoField(primary_key=True, serialize=False),
        ),
    ]
