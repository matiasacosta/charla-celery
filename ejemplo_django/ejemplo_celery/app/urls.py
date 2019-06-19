from . import views as views
from django.conf.urls import url

urlpatterns = [
    url(r'^$', views.tarea, name="tarea"),
    url(r'^get_job_state/$', views.get_job_state, name='get_job_state'),
]