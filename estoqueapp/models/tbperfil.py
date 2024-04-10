from estoqueapp.models.base import BaseModel
from django.db import models


class Perfil(BaseModel):
    linha = models.CharField(
        max_length=20, help_text="Inserir linha a qual pertence o perfil."
    )
    codigo_perfil = models.CharField(
        max_length=200, help_text="Código do perfil. ex: SU-001"
    )
    peso_kg_m = models.FloatField(help_text="Inserir peso por metro linear.")
    descricao = models.CharField(
        max_length=200,
        help_text="Descrição de uso do perfil. ex: MARCO SUPERIOR / 2 FOLHAS.",
    )
    quantidade = models.IntegerField(
        help_text="Inserir quantidade em estoque - Favor inserir somente barras inteiras.",
    )
    acabamento_cor = models.CharField(
        max_length=40, help_text="Inserir cor com Código. ex: BRANCO-RAL9003"
    )

    class Meta:
        abstract = False

    def __str__(self):
        return "{}: {}: {}: {}: {} - {}".format(
            self.codigo_perfil,
            self.linha,
            self.peso_kg_m,
            self.descricao,
            self.quantidade,
            self.acabamento_cor,
        )


def update_quantidade(self, value):
    try:
        self.balance = self.balance + float(value)
        return True
    except:
        return False


def get_(self):
    return self.balance
