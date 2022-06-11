from django.forms import ModelForm
from .models import Publicacao
from .models import Final_Project
from .models import Quizz


class PublicacaoForm(ModelForm):
    class Meta:
        model = Publicacao
        fields = '__all__'


class TcfForm(ModelForm):
    class Meta:
        model = Final_Project
        fields = '__all__'


class QuizzForm(ModelForm):
    class Meta:
        model = Quizz
        fields = '__all__'