from dataclasses import fields
from django import forms
from estoqueapp.models import Perfil


# Listas para os "selects" do formulário
ESCOLHAS_LINHA = [
    ("SELECIONE LINHA DO PERFIL...", "SELECIONE LINHA DO PERFIL..."),
    ("SUPREMA", "SUPREMA"),
    ("GOLD", "GOLD"),
    ("LINHA 30", "LINHA 30"),
]

ESCOLHAS_COR_ACABAMENTO = [
    ("SELECIONE ACABAMENTO...", "SELECIONE ACABAMENTO..."),
    ("NATURAL", "NATURAL"),
    ("BRANCO-RAL9003", "BRANCO-RAL9003"),
    ("PRETO-RAL9005", "PRETO-RAL9005"),
    ("ANODIZADO FOSCO-1000", "ANODIZADO FOSCO-1000"),
]


class PerfilForm(forms.ModelForm):
    # Formulario que será persistido no banco de dados
    class Meta:
        model = Perfil
        fields = "__all__"
        widgets = {
            "linha": forms.Select(
                attrs={"class": "form-select"}, choices=ESCOLHAS_LINHA
            ),
            "acabamento_cor": forms.Select(
                attrs={"class": "form-select"}, choices=ESCOLHAS_COR_ACABAMENTO
            ),
            "codigo_perfil": forms.TextInput(
                attrs={"class": "form-control"}
            ),
            "quantidade": forms.TextInput(
                attrs={"class": "form-control"}
            ),
            "descricao": forms.TextInput(
                attrs={"class": "form-control"}
            ),
            "peso_kg_m": forms.TextInput(
                attrs={"class": "form-control"}
            ),
        }
