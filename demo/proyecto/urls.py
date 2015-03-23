from django.conf.urls import patterns, include, url

urlpatterns = patterns('proyecto.views',
  url(r'^$', 'view_index',name='vista_index'),
  url(r'^proyectos/$', 'view_lista_proyecto',name='vista_lista_proyectos'),
)


