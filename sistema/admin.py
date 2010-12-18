from ministerio.sistema.models import congregacion ,Publicador
from django.contrib import admin

class congregacionAdmin(admin.ModelAdmin):
     list_display = ('nombre_cong', 'direccion_cong','comuna_cong','ciudad_cong')
#     exclude = ('id_cong')
#     ordering = ('nombre_cong')
#     search_fields = ('nombre_cong')    
	#pass
class PublicadorAdmin(admin.ModelAdmin):
     list_display = ('nombrep_pub', 'apellidop_pub','apellidom_pub')


admin.site.register(congregacion,congregacionAdmin)
admin.site.register(Publicador,PublicadorAdmin)
