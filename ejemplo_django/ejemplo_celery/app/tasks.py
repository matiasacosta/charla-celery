from celery import task, current_task
from time import sleep

@task()
def incrementar_uno(): #TODO Buscar un nombre mejor
    max_values = 20

    for i in range(0,max_values):
        porcentaje = i*100/(max_values)
        formato_porcentaje = format(porcentaje, '.2f')
        sleep(0.5)
        current_task.update_state(state='PROGRESS' ,meta={'current':formato_porcentaje})