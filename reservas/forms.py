from django import forms
from .models import Reserva
from django.core.exceptions import ValidationError


# Formulário baseado no modelo Reserva
class ReservaForm(forms.ModelForm):
    class Meta:
        model = Reserva  # Define que o formulário usa o modelo Reserva
        fields = ['laboratorio', 'data', 'horario_inicio', 'horario_fim']  
        
        # Personalização dos campos (widgets HTML)
        widgets = {
            'data': forms.DateInput(attrs={'type': 'date', 'class': 'form-control'}),
            'horario_inicio': forms.TimeInput(attrs={'type': 'time', 'class': 'form-control'}),
            'horario_fim': forms.TimeInput(attrs={'type': 'time', 'class': 'form-control'}),
        }




        # Validação personalizada do formulário
    def clean(self):
        cleaned_data = super().clean()
        laboratorio = cleaned_data.get('laboratorio')
        data = cleaned_data.get('data')
        inicio = cleaned_data.get('horario_inicio')
        fim = cleaned_data.get('horario_fim')

        # Verifica se o horário de início é maior ou igual ao horário de fim
        if inicio and fim and inicio >= fim:
            raise ValidationError("O horário de início deve ser menor que o horário de fim.")

        # Só faz a verificação se todos os dados estiverem preenchidos
        if laboratorio and data and inicio and fim:

            # Busca reservas que se sobrepõem ao horário informado
            conflitos = Reserva.objects.filter(
                laboratorio=laboratorio,
                data=data,
                horario_inicio__lt=fim,
                horario_fim__gt=inicio
            )
            # Se for uma edição, exclui ela mesma da verificação
            if self.instance.pk:
                conflitos = conflitos.exclude(pk=self.instance.pk)

                
            # Se existir conflito, lança erro de validação
            if conflitos.exists():
                raise ValidationError("Já existe uma reserva neste laboratório nesse horário.")

        return cleaned_data  # Retorna os dados validados
