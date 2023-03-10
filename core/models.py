from django.db import models

# Create your models here.
class Funcao(models.Model):
    nome = models.CharField(max_length=50, blank=False, null=False)
    
    def __str__(self):
        return self.nome
    
    class Meta:
        db_table = 'funcao'

class Setor(models.Model):
    nome = models.CharField(max_length=50, blank=False, null=False)
    
    def __str__(self):
        return self.nome
    
    class Meta:
        db_table = 'setor'

class TipoRisco(models.Model):
    nome = models.CharField(max_length=50, blank=False, null=False)
    
    def __str__(self):
        return self.nome
    
    class Meta:
        db_table = 'tiporisco'

class Risco(models.Model):
    nome = models.CharField(max_length=50, blank=False, null=False)
    tiporisco = models.ForeignKey('tiporisco', on_delete = models.CASCADE)
    
    def __str__(self):
        return self.nome
    
    class Meta:
        db_table = 'risco'

class Grupo(models.Model):
    nome = models.CharField(max_length=50, blank=False, null=False)
    
    def __str__(self):
        return self.nome
    
    class Meta:
        db_table = 'grupo'

class Exame(models.Model):
    nome = models.CharField(max_length=50, blank=False, null=False)
    validade = models.IntegerField(null=False, blank=False)
    
    def __str__(self):
        return self.nome
    
    class Meta:
        db_table = 'exame'

class TipoExame(models.Model):
    nome = models.CharField(max_length=50, blank=False, null=False)
    def __str__(self):
        return self.nome
    
    class Meta:
        db_table = 'tipoexame'