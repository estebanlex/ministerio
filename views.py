from django.shortcuts import render_to_response
from django.template.loader import get_template
from django.template import Template, Context
from django.http import HttpResponse
import datetime
 
def pagina_index(request):
   html = "<html><body>Hola mundo en django</body></html>"
   return HttpResponse(html)
	
	
#def current_datetime(request):
  #now = datetime.datetime.now()
  #html = "<html><body>It is now %s.</body></html>" % now
  #return HttpResponse(html)

def current_datetime(request):
   now = datetime.datetime.now()
   nombre="Jimmy Palma"
   return render_to_response('current_datetime.html', {'current_date': now, 'nombre': nombre})   
   
def hours_ahead(request, offset):
   now = datetime.datetime.now()
   nombre="Jimmy Palma"
   offset = int(offset)
   dt = datetime.datetime.now() + datetime.timedelta(hours=offset)
   return render_to_response('hours.html', {'current_date': now, 'nombre': nombre}) #reemplaza los nombres de las variables con lo valores

   
#def current_datetime(request):
   #now = datetime.datetime.now()
   #t = Template("<html><body>It is now {{ current_date }}.</body></html>")
   #html = t.render(Context({'current_date': now}))
   #return HttpResponse(html)

   
#def current_datetime(request):
  #now = datetime.datetime.now()
  #t = get_template('current_datetime.html') 
  #html = t.render(Context({'current_date': now}))
  #return HttpResponse(html)
  
  
 #reemplaza los nombres de las variables con lo valores
