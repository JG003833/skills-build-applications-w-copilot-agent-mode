from django.test import TestCase
from .models import User, Team, Activity, Leaderboard, Workout

class ModelTests(TestCase):
    def setUp(self):
        self.team = Team.objects.create(name='Test Team')
        self.user = User.objects.create_user(username='testuser', email='test@example.com', password='test', team=self.team)
        self.workout = Workout.objects.create(name='Test Workout', description='desc', duration=10)
        self.activity = Activity.objects.create(user=self.user, type='run', duration=20)
        self.leaderboard = Leaderboard.objects.create(user=self.user, points=50)

    def test_team(self):
        self.assertEqual(self.team.name, 'Test Team')

    def test_user(self):
        self.assertEqual(self.user.email, 'test@example.com')

    def test_workout(self):
        self.assertEqual(self.workout.name, 'Test Workout')

    def test_activity(self):
        self.assertEqual(self.activity.type, 'run')

    def test_leaderboard(self):
        self.assertEqual(self.leaderboard.points, 50)
