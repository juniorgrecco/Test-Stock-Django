from email import message
from django.shortcuts import render, get_object_or_404, redirect
from estoqueapp.models.tbperfil import Perfil
from estoqueapp.forms.perfis_form import PerfilForm
from django.contrib import messages


def lista(request):
    perfis = Perfil.objects.all()
    context = {"perfis": perfis}
    return render(request, "estoqueapp/lista_perfis.html", context)


def create(request):
    if request.method == "POST":
        form = PerfilForm(request.POST)
        if form.is_valid():
            form.save()
            form = PerfilForm()
            # LINHAS EM TESTE PARA RELOAD DO FORM, E FEEDBACK DE MSG DO SISTEMA PARA O USUÁRIO - LISTA_PERFIS
            #->messages.success(request, "ITEM ADICIONADO COM ÊXITO!")
            #->context = {"form": form}
            #->return render(request, "home.html", context)
            context = {"salvo": True, "form": form}
            return render(request, "home.html", context)
        else:
            print("Formulario invalido")
    else:
        form = PerfilForm()

    context = {"form": form}
    return render(request, "home.html", context)


def delete(request, rel_perfis_id):
    perfis = get_object_or_404(Perfil, pk=rel_perfis_id)
    try:
        perfis.delete()
        return redirect("estoqueapp:lista_perfis")
    except:
        context = {
            "message": "Erro ao deletar objeto."
        }
        return render(request, "estoqueapp/lista_perfis.html", context)

# LINHAS EM TESTE PARA RELOAD DO FORM, E FEEDBACK DE MSG DO SISTEMA PARA O USUÁRIO - LISTA_PERFIS
#def show_messages(request):
#    return render(request, 'home.html')

def update(request, rel_perfis_id):
    perfis = get_object_or_404(Perfil, pk=rel_perfis_id)
    try:
        if request.method == "POST":
            form = PerfilForm(request.POST, instance=perfis)
            if form.is_valid():
                form.save()
                return redirect('estoqueapp:lista_perfis')
        else:
            form = PerfilForm(instance=perfis)
            context = {
                "form": form,
                "rel_perfis_id": rel_perfis_id,
            }
            return render(request, "estoqueapp/editar_perfis.html", context)
    except:
            return redirect(request, 'estoqueapp:lista_perfis')
