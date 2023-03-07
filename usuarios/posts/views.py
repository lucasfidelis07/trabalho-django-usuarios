from django.shortcuts import render

usuarios = [
    {
        "id": 1,
        "nome": "Lucas"
    },
    {
        "id": 2,
        "nome": "Gabriel"
    },
    {
        "id": 3,
        "nome": "Fidelis"
    },
]

def listar_usuarios(request):
    context = {
        "usuarios": usuarios
    }
    return render(request, 'listar_usuarios.html', context)

def detalhe_usuario(request, id):
    usuario = usuarios[id-1]
    return render(request, 'detalhe_usuario.html', {"usuario": usuario})