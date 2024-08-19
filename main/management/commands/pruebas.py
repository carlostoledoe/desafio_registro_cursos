from django.core.management.base import BaseCommand
from main.services import *

class Command(BaseCommand):
    def handle(self, *args, **kwargs):
        imprime_estudiante_cursos('2-1')
        imprime_estudiante_cursos('2-2')
        imprime_estudiante_cursos('2-3')
        imprime_estudiante_cursos('2-5')
        print('Acción realizada')