from django.shortcuts import render
from visitors.forms import VisitorForm

# Create your views here.
def register_visitor(request):

    context = {
        "Nome_pagina": "register_visitors",
        "form": VisitorForm
    }

    return render(request, 'registrar_visitante.html', context)   