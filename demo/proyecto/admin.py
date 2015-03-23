from django.contrib import admin
from .models import tabla,campo,proyecto,configuracion


admin.site.register(tabla)
admin.site.register(campo)
admin.site.register(proyecto)
admin.site.register(configuracion)
