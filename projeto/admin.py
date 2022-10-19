from django.contrib import admin
from .models import Inicio
from .models import BoldFeatures
from .models import MeetLaurel
from .models import StayInTheKnow
from .models import Contato
from .models import EnviarEmail

# Register your models here.
class InicioAdmin(admin.ModelAdmin):
    list_display1 = ('id', 'titulo')

admin.site.register(Inicio)
admin.site.register(BoldFeatures)
admin.site.register(MeetLaurel)
admin.site.register(StayInTheKnow)
admin.site.register(Contato)
admin.site.register(EnviarEmail)
