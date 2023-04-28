from django.db import models


class Fotografia(models.Model):
    OPT = [
        ('NEBULOSA', "Nebulosa"),
        ('ESTRELA', "Estrela"),
        ('GALÁXIA', "Galáxia"),
        ('PLANETA', "Planeta")
    ]
    nome = models.CharField(max_length=100, null=False, blank=False)
    legenda = models.CharField(max_length=150, null=False, blank=False)
    categoria = models.CharField(max_length=100, choices=OPT, default='')
    descricao = models.TextField(null=False, blank=False)
    foto = models.CharField(max_length=100, null=False, blank=False)
    
    def __str__(self) -> str:
        return f"Fotografia [nome={self.nome}]"


# class FotografiaCategoria(models.Model):
#     id_categoria = models.ForeignKey("Categoria", on_delete=models.SET_NULL)
#     id_fotografia = models.ForeignKey("Fotografia", on_delete=models.SET_NULL)


#     def __str__(self) -> str:
#         return f'Categoria de Fotografia [id_f={self.id_fotografia}; id_c={self.id_categoria}]'
    
# class Categoria(models.Model):
#     nome = models.CharField(max_length=100, null=False, blank=False)

#     def __str__(self) -> str:
#         return f'Categoria de Fotografia [nome={self.nome}]'