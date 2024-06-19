from django import forms
from veiculo.models import Veiculo

class FormularioVeiculo(forms.ModelForm):
    """
    Formulário para o model Veiculo
    """

    class Meta:
        model = Veiculo
        exclude = []