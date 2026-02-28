from django.test import TestCase
from django.contrib.auth import get_user_model
from .models import Team, Activity, Leaderboard, Workout

class ModelTests(TestCase):
    def test_create_team(self):
        team = Team.objects.create(name='Test Team')
        self.assertEqual(str(team), 'Test Team')

    def test_create_activity(self):
        activity = Activity.objects.create(user='testuser', type='run', duration=30)
        self.assertEqual(str(activity), 'testuser - run')

    def test_create_leaderboard(self):
        lb = Leaderboard.objects.create(user='testuser', score=100)
        self.assertEqual(str(lb), 'testuser: 100')

    def test_create_workout(self):
        workout = Workout.objects.create(name='Pushups', difficulty='Easy')
        self.assertEqual(str(workout), 'Pushups (Easy)')

    def test_create_user(self):
        User = get_user_model()
        user = User.objects.create_user(username='testuser', email='test@example.com', password='pass')
        self.assertEqual(user.email, 'test@example.com')
