from django.shortcuts import render_to_response
from django.template import RequestContext
from .models import proyecto
from .forms import formProyecto
from django.http import HttpResponse,HttpResponseRedirect
from django.contrib.auth.models import User
from datetime import datetime
import simplejson

mes = {
'1':'Enero',
'2':'Febrero',
'3':'Marzo',
'4':'Abril',
'5':'Mayo',
'6':'Junio',
'7':'Julio',
'8':'Agosto',
'9':'Septimbre',
'10':'Octubre',
'11':'Noviembre',
'12':'diciembre',
}





def view_index(request):
	return render_to_response('index.html',
		context_instance=RequestContext(request))




def view_lista_proyecto(request):
	if request.method == "POST":
		if request.is_ajax():
			if "product_id" in request.POST:
				print request.POST
				try:
					id_producto = request.POST['product_id']
					p = proyecto.objects.get(pk=id_producto)
					mensaje = {"status":"True","product_id":p.id}
					p.delete() # Elinamos objeto de la base de datos
					return HttpResponse(simplejson.dumps(mensaje),content_type='application/json')
				except:
					mensaje = {"status":"False"}
					return HttpResponse(simplejson.dumps(mensaje),content_type='application/json')
			if "nombre" in request.POST:
				form = formProyecto(request.POST)
				if form.is_valid():
					p = form.save(commit = False)
					p.user = User.objects.get(pk=request.user.id)
					p.fecha_creacion = fecha = datetime.now()
					p.save()
					msg = {'status':'true',
							'nombre':p.nombre,
							'id':p.id,
							'fecha':fecha.strftime("%d de  %B del %Y alas %H:%M"),
					
							}
					return HttpResponse(simplejson.dumps(msg),content_type='application/json')
				
				else:
					msg  = {'status':'false'}
					return HttpResponse(simplejson.dumps(msg),content_type='application/json')
		else:
			return HttpResponse("Error no se puede mostrar la pagina")
	else:
		lista_proyectos = proyecto.objects.all()
		form = formProyecto()
		ctx = {'form':form,
			  'lista_proyectos':lista_proyectos
		}
		return render_to_response('proyecto/lista.html',ctx,
			context_instance=RequestContext(request))


