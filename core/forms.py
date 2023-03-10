from django.forms import ModelForm
from .models import Funcao, Exame, Risco, TipoRisco, Setor, Grupo

class FuncaoForm(ModelForm):
    class Meta:
        model = Funcao
        fields = '__all__'

class ExameForm(ModelForm):
    class Meta:
        model = Exame
        fields = '__all__'

class TipoRiscoForm(ModelForm):
    class Meta:
        model = TipoRisco
        fields = '__all__'
        
class RiscoForm(ModelForm):
    class Meta:
        model = Risco
        fields = '__all__'

class SetorForm(ModelForm):
    class Meta:
        model = Setor
        fields = '__all__'

class GrupoForm(ModelForm):
    class Meta:
        model = Grupo
        fields = '__all__'
        

