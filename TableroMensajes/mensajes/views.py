from django.shortcuts import render,redirect,get_object_or_404
from .models import Mensaje
from django.views import View
from django.urls import reverse_lazy
from django.views.generic.edit import CreateView
from .forms import MensajeForm

# crear menaje
class CrearMensajeView(CreateView):
    model = Mensaje
    template_name = 'mensajes/crearMensaje.html'
    fields = ['remitente', 'destinatario', 'texto']
    success_url = reverse_lazy('mensajes:lista_mensaje')


# Listar y buscar mensajes

class ListaViewMensajes(View):
  def get(self, request):
    remitente = request.GET.get('remitente', '')
    destinatario = request.GET.get('destinatario', '')
    
    mensajes = Mensaje.objects.all()

    if remitente:
        mensajes = mensajes.filter(remitente__icontains=remitente)
    if destinatario:
        mensajes = mensajes.filter(destinatario__icontains=destinatario)

    form = MensajeForm()  # Asegúrate de pasar el formulario a la plantilla
    return render(request, 'mensajes/vistasMensajes.html', {'mensajes': mensajes, 'form': form})


  def post(self, request):
      form=MensajeForm(request.POST)
      if form.is_valid():
          form.save()
          return redirect('mensajes:lista_mensaje')

#eliminar mensaje
class MensajeDeleteView(View):
    def post(self, request,pk):
        mensaje = get_object_or_404(Mensaje, pk=pk)
        mensaje.delete()
        return redirect('mensajes:lista_mensaje')




