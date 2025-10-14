from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Reserva
from .forms import ReservaForm

@login_required
def index(request):
    # Lista todas as reservas ordenadas
    reservas = Reserva.objects.all().order_by('data', 'horario_inicio')
    return render(request, 'index.html', {'reservas': reservas})

@login_required
def criar_reserva(request):
    # Cria nova reserva
    if request.method == 'POST':
        form = ReservaForm(request.POST)
        if form.is_valid():
            reserva = form.save(commit=False)
            reserva.professor = request.user
            reserva.save()
            return redirect('index')
    else:
        form = ReservaForm()
    return render(request, 'criar_reserva.html', {'form': form})

@login_required
def editar_reserva(request, id):
    # Edita reserva do usuário logado
    reserva = get_object_or_404(Reserva, id=id, professor=request.user)
    if request.method == 'POST':
        form = ReservaForm(request.POST, instance=reserva)
        if form.is_valid():
            form.save()
            return redirect('index')
    else:
        form = ReservaForm(instance=reserva)
    return render(request, 'editar_reserva.html', {'form': form})

@login_required
def excluir_reserva(request, id):
    # Exclui reserva do usuário logado
    reserva = get_object_or_404(Reserva, id=id, professor=request.user)
    if request.method == 'POST':
        reserva.delete()
        return redirect('index')
    return render(request, 'excluir_reserva.html', {'reserva': reserva})
