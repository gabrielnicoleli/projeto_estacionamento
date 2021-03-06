from django.contrib import admin
from .models import (
    Marca, 
    Cor, 
    Veiculo, 
    Pessoa, 
    Parametros, 
    MovimentoRotativo
)

class movRotativoAdm(admin.ModelAdmin):
    list_display = ('checkin',
                    'checkout',
                    'valor_hora',
                    'veiculo',
                    'pago',
                    'total',
                    'horas_total')


admin.site.register(Marca)
admin.site.register(Cor)
admin.site.register(Veiculo)
admin.site.register(Pessoa)
admin.site.register(Parametros)
admin.site.register(MovimentoRotativo, movRotativoAdm)




