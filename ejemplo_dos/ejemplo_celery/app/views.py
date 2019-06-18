# Django 
from django.shortcuts import render,HttpResponse, HttpResponseRedirect
from django.conf import settings
from django.http import JsonResponse

# Celery
from celery import task, current_task
from celery.result import AsyncResult
from time import sleep

@task()
def incrementar_uno(): #TODO Buscar un nombre mejor
    max_values = 20

    for i in range(0,max_values):
        porcentaje = i*100/(max_values)
        formato_porcentaje = format(porcentaje, '.2f')
        sleep(0.1)
        current_task.update_state(state='PROGRESS' ,meta={'current':formato_porcentaje})


def get_job_state(request):
    """
    Una vista para informar al usuario del avance o el estado del job celery
    """
    data={}
    if 'job_id' in request.GET:
        job = AsyncResult(request.GET['job_id'])

        #if (job.state == 'FAILURE'):
        if (job.failed()):
            data['errors'] = True
            error_descrip = job.get(propagate=False)
            data['error_descrip'] = str(error_descrip)

        #if (job.state == 'SUCCESS'):
        elif (job.ready()):
            data['success'] = True

        elif not (job.ready()):
            if job.state == 'PENDING':
                data['pending'] = True
            else:
                data['running'] = True
                data['progress'] = job.info

    return JsonResponse(data, safe=False)


def tarea(request):
    contexto = {}
    if request.method == 'POST':
        job = incrementar_uno.delay()
        contexto['job_id'] = job.id
    else:
        contexto['job_id'] = None
    return render(request, 'app/tarea.html',contexto)