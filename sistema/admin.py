from ministerio.sistema.models import congregacion
from django.contrib import admin

class congregacionAdmin(admin.ModelAdmin):
     list_display = ('nombre_cong', 'direccion_cong','comuna_cong')
#     exclude = ('id_cong')
#     ordering = ('nombre_cong')
#     search_fields = ('nombre_cong')    
	#pass
admin.site.register(congregacion,congregacionAdmin)
