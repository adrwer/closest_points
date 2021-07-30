from django.test import TestCase
from closestpoints.models import Points


class TestModels(TestCase):

    def setUp(self):
        self.points1 = Points.objects.create(
            input="(2, 3),(12, 30),(40, 50),(5, 1),(12, 10),(3, 4)",
            output="[(2, 3)]"
        )

    def test_points_model(self):
        self.assertEquals(self.points1.output, "[(2, 3)]")