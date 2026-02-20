from django.shortcuts import render

# Create your views here.
def index(request):
    print(dir(request))
    print(f"User: {request.user}")

    if str(request.user) == "AnonymousUser":
        teste = "Usuário não logado"
    else:
        teste = "Usuário logado"
    context = {
        "curso": "Programação Web com Django Framework",
        "logado": teste
    }
    return render(request, 'index.html', context)

def contato(request):
    return render(request, 'contato.html')