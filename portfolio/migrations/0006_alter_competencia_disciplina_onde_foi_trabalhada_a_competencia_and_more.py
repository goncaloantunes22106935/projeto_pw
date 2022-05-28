# Generated by Django 4.0.4 on 2022-05-24 15:02

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio', '0005_projeto_imagem_do_projeto'),
    ]

    operations = [
        migrations.AlterField(
            model_name='competencia',
            name='disciplina_onde_foi_trabalhada_a_competencia',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='portfolio.cadeira'),
        ),
        migrations.AlterField(
            model_name='competencia',
            name='projeto_onde_foi_aplicada_a_competencia',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='portfolio.projeto'),
        ),
    ]