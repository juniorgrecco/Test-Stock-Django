# Generated by Django 4.0.6 on 2022-08-11 01:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("estoqueapp", "0002_perfil_delete_account"),
    ]

    operations = [
        migrations.AlterField(
            model_name="perfil",
            name="acabamento_cor",
            field=models.CharField(
                help_text="Inserir cor com Código. ex: BRANCO RAL9003", max_length=40
            ),
        ),
    ]