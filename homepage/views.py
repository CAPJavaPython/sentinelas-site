from django.shortcuts import render
from .forms import LoginForm
from .models import Integrante

# Create your views here.
def home(request):
    return render(request, 'homepage/home.html')


def login(request):
    first_name = request.GET.get('first_name', '')
    
    if request.method == 'POST':
        form = LoginForm(request.POST)
        integrante = None
        if form.is_valid():
            birth_date = form.cleaned_data.get('birth_date')
            phone_number = form.cleaned_data.get('telefone')
            
            
            # Busca baseada no que foi preenchido
            if phone_number:
                integrante = Integrante.objects.filter(telefone=phone_number).first()

            elif birth_date:
                integrante = Integrante.objects.filter(birth_date=birth_date).first()
            
            # Se encontrou o integrante, pega o nome e avança
            if integrante:
                first_name = integrante.first_name
                return render(request, 'homepage/name.html', {'first_name': first_name})
            else:
                # Se não encontrou no banco, devolve o form com erro
                message = 'Nenhum cadastro encontrado com esses dados.'
        
    else:
        form = LoginForm()
        
    return render(request, 'homepage/login.html', {'form': form, 'message': message if 'message' in locals() else ''})