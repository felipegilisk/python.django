from django.db import models
import datetime as dt


class Categoria(models.Model):
    nome = models.CharField(max_length=100, null=False, blank=False)
    ativo = models.BooleanField(default=True)

    def __str__(self) -> str:
        return self.nome


class Fotografia(models.Model):
    # OPT = Categoria.objects.filter(ativo=True)

    OPT = [
        ('Nebulosa', "Nebulosa"),
        ('Estrela', "Estrela"),
        ('Galáxia', "Galáxia"),
        ('Planeta', "Planeta"),
        ('Cometa', "Cometa")
    ]
    nome = models.CharField(max_length=100, null=False, blank=False)
    legenda = models.CharField(max_length=150, null=False, blank=False)
    categoria = models.CharField(max_length=100, choices=OPT, default='')
    descricao = models.TextField(null=False, blank=False)
    foto = models.ImageField(upload_to='fotos/%Y/%m/%d/', blank=True)
    ativo = models.BooleanField(default=False)
    data_fotografia = models.DateTimeField(default=dt.datetime.now())
    
    def __str__(self) -> str:
        return self.nome
