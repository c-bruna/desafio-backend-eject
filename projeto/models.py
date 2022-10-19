from email.policy import default
from unittest.util import _MAX_LENGTH
from django.db import models

# Create your models here.

class Inicio(models.Model):
    image = models.ImageField (verbose_name = 'Imagem', upload_to = 'fotos', default = '')
    titulo = models.CharField(verbose_name = 'Tituo inicial', max_length=250)
    descricao = models.TextField(verbose_name = 'Mensagem de efeito', max_length=500, default='')
    text_button1 = models.CharField(verbose_name = 'Texto-Botao1', max_length=100)
    text_button2 = models.CharField(verbose_name = 'Texto-Botao2', max_length=100)

    def __str__ (self):
        return f'{self.titulo}'

class BoldFeatures(models.Model):
    titulo = models.CharField(verbose_name = 'Título de Bold features', max_length=250)

    titulo1 = models.CharField(verbose_name = 'Título do item 1', max_length=250)
    descricao1 = models.TextField(verbose_name = 'Descrição para o item 1', max_length=500, default='')

    titulo2 = models.CharField(verbose_name = 'Título do item 2', max_length=250)
    descricao2 = models.TextField(verbose_name = 'Descrição para o item 2', max_length=500, default='')

    titulo3 = models.CharField(verbose_name = 'Título do item 3', max_length=250)
    descricao3 = models.TextField(verbose_name = 'Descrição para o item 3', max_length=500, default='')

    titulo4 = models.CharField(verbose_name = 'Título do item 4', max_length=250)
    descricao4 = models.TextField(verbose_name = 'Descrição para o item 4', max_length=500, default='')

    titulo5 = models.CharField(verbose_name = 'Título do item 5', max_length=250)
    descricao5 = models.TextField(verbose_name = 'Descrição para o item 5', max_length=500, default='')

    titulo6 = models.CharField(verbose_name = 'Título do item 6', max_length=250)
    descricao6 = models.TextField(verbose_name = 'Descrição para o item 6', max_length=500, default='')

    def __str__ (self):
        return f'{self.titulo}'

class MeetLaurel(models.Model):
    titulo = models.CharField(verbose_name = 'Título de Meet Laurel', max_length=250)
    descricao = models.TextField(verbose_name = 'Descrição de Meet Laurel', max_length=500)
    video = models.CharField(verbose_name = 'Vídeo de Meet Laurel', max_length=250)

    def __str__ (self):
        return f'{self.titulo}'

class StayInTheKnow(models.Model):
    titulo = models.CharField(verbose_name = 'Título de Stay in the know', max_length=250)
    descricao = models.TextField(verbose_name = 'Descrição de Stay in the know', max_length=500)
    text_button = models.CharField(verbose_name = 'Texto-Botão de enviar e-mail', max_length=100, default="")

    def __str__ (self):
        return f'{self.titulo}'

class Contato(models.Model):
    facebook = models.CharField(verbose_name = 'Facebook', max_length=250)
    twitter = models.CharField(verbose_name = 'Twitter', max_length=250)
    google = models.CharField(verbose_name = 'Google', max_length=250, default='')

    def __str__ (self):
        return f'{self.facebook}'

class EnviarEmail(models.Model):
    email = models.EmailField()

    def __str__(self):
        return f'{self.email}'