from django.db import models
import math
import datetime

class Pessoa(models.Model):
    nome = models.CharField(max_length=100)
    endereco = models.CharField(max_length=200)
    telefone = models.CharField(max_length=20)

    def __str__(self):
        return (self.nome)

class Marca(models.Model):
    nome = models.CharField(max_length=50)

    def __str__(self):
        return (self.nome)


class Cor(models.Model):
    nomecor = models.CharField(max_length=50)

    def __str__(self):
        return (self.nomecor)


class Veiculo(models.Model):
    marca = models.ForeignKey(Marca, on_delete=models.PROTECT)
    placa = models.CharField(max_length=7)
    proprietario = models.ForeignKey(Pessoa, on_delete=models.PROTECT)
    cor = models.ForeignKey(Cor, on_delete=models.PROTECT)
    observacoes = models.TextField()


    def __str__(self):
        return self.marca.nome + '-' + self.placa

class Parametros (models.Model):
    valor_hora = models.DecimalField(max_digits=6, decimal_places=2)
    valor_mes =  models.DecimalField(max_digits=6, decimal_places=2)
    
    def __str__(self):
        return 'Parametros Gerais'


class MovimentoRotativo(models.Model):
    checkin = models.DateTimeField(auto_now = False)
    checkout = models.DateTimeField(auto_now = False, blank=True, null=True)
    valor_hora = models.DecimalField(max_digits=6, decimal_places=2)
    veiculo = models.ForeignKey(Veiculo, on_delete=models.PROTECT)
    pago = models.BooleanField(default=False)

    def __str__(self):
        return self.veiculo.placa

    def horas_total(self):
        if self.checkout is None:
            return 0
        else:
            frmt = '%Y-%m-%d %H:%M:%S' 
            seconds = 3600
            chkin = str(self.checkin)
            chkout = str(self.checkout)
            try:
                datecheckin =  datetime.datetime.strptime(chkin, frmt)
                datecheckout = datetime.datetime.strptime(chkout, frmt)
                return math.ceil((datecheckout - datecheckin).total_seconds() / seconds)
            except ValueError:
               return 0


    def total (self):
        if self.checkout is None:
            return 0.00
        else:
            return self.valor_hora * self.horas_total()



