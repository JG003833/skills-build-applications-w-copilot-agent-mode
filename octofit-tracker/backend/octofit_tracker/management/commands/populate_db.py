from django.core.management.base import BaseCommand
from django.contrib.auth import get_user_model
from djongo import models

from octofit_tracker.models import Team, Activity, Leaderboard, Workout

class Command(BaseCommand):
    help = 'Populate the octofit_db database with test data'

    def handle(self, *args, **kwargs):
        User = get_user_model()
        # Borrar datos existentes
        User.objects.all().delete()
        Team.objects.all().delete()
        Activity.objects.all().delete()
        Leaderboard.objects.all().delete()
        Workout.objects.all().delete()

        # Crear equipos
        marvel = Team.objects.create(name='Marvel')
        dc = Team.objects.create(name='DC')

        # Crear usuarios
        ironman = User.objects.create_user(username='ironman', email='ironman@marvel.com', password='1234', team=marvel)
        captain = User.objects.create_user(username='captain', email='captain@marvel.com', password='1234', team=marvel)
        batman = User.objects.create_user(username='batman', email='batman@dc.com', password='1234', team=dc)
        superman = User.objects.create_user(username='superman', email='superman@dc.com', password='1234', team=dc)

        # Crear actividades
        Activity.objects.create(user=ironman, type='run', duration=30)
        Activity.objects.create(user=batman, type='cycle', duration=45)
        Activity.objects.create(user=superman, type='swim', duration=60)
        Activity.objects.create(user=captain, type='run', duration=25)

        # Crear leaderboard
        Leaderboard.objects.create(user=ironman, points=100)
        Leaderboard.objects.create(user=batman, points=90)
        Leaderboard.objects.create(user=superman, points=80)
        Leaderboard.objects.create(user=captain, points=70)

        # Crear workouts
        Workout.objects.create(name='Cardio Blast', description='Rutina intensa de cardio', duration=40)
        Workout.objects.create(name='Fuerza Total', description='Entrenamiento de fuerza', duration=50)

        self.stdout.write(self.style.SUCCESS('Base de datos poblada con datos de prueba.'))
