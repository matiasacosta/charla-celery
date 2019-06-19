# Django 
from django.shortcuts import render,HttpResponse, HttpResponseRedirect
from django.http import JsonResponse

# Celery
from celery.result import AsyncResult
from .tasks import incrementar_uno

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