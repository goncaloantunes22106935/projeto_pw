from django.contrib import admin
from .models import Cadeira
from .models import Professor
from .models import Competencia
from .models import Pessoa
from .models import Escola
from .models import Projeto
from .models import Publicacao
from .models import Jogador

# Register your models here.

admin.site.register(Cadeira)
admin.site.register(Professor)
admin.site.register(Competencia)
admin.site.register(Pessoa)
admin.site.register(Escola)
admin.site.register(Projeto)
admin.site.register(Publicacao)
admin.site.register(Jogador)